---
layout: post
class: 'post-template'
subclass: 'post'
title: "Testing setTimeout & setInterval With Jasmine-Node"
date: 2015-10-30 22:38:16 +0000
slug: "testing-setinterval-with-jasmine-node"
image: "https://moondustwriter.files.wordpress.com/2011/06/salvador-dali.jpg"
description: "Ditch Jasmine's complicated mock clock and compare the difference between Node.js and window's setTimeout/setInterval."
meta_title: "Testing setInterval with Jasmine-Node"
ghost_id: 58
ghost_uuid: "60344d71-6638-4073-bc03-edbcaccdc0a9"
---

##Jasmine No~~de~~
Jasmine has a very complicated way of testing `setTimeout` and `setInterval` that I, frankly, don't understand very well. To add to the complication, my code is server-side, so I can't just `spyOn( window, 'setInterval' )`. Jasmine also gives a poor example with trivial code--not code someone (like myself) would actually be testing if they actually needed to refer to the docs.

![](/assets/images/2015/10/Screen-Shot-2015-10-30-at-2-53-07-PM.png)

##My Function
    var update = require( './update' ).update;

    exports.updateEveryMinute = function() {
      // Check every minute
      return setInterval( update, 1000 * 60 );
    };
    
This needs testing. Node.js [docs](https://nodejs.org/api/globals.html#globals_global_objects) explain really well that `setInterval` is not on the window, it's on a `globals` object:

>In browsers, the top-level scope is the global scope. That means that in browsers if you're in the global scope var something will define a global variable. In Node.js this is different. The top-level scope is not the global scope; var something inside an Node.js module will be local to that module.

##Test Me
####tl;dr:

    // require the function you're testing
    var updateEveryMinute = require( './intervals' ).updateEveryMinute;
    // require the function called by setInterval.
    var update = require( './update' ).update
    
    describe('updateEveryMinute', function() {
      var intervalId;

      afterEach(function() {
        clearInterval( intervalId );
      });

      it('should be defined as a function', function() {
        expect( typeof updateEveryMinute ).toBe( 'function' );
      });

      it('should set an interval to run update every minute', function() {
        spyOn( global, 'setInterval' ).andCallThrough();
        intervalId = updateEveryMinute();
        expect( global.setInterval ).toHaveBeenCalled();
        expect( global.setInterval ).toHaveBeenCalledWith( update, 60000 );
      });

      it('should return an interval id', function() {
        spyOn( global, 'setInterval' ).andCallThrough();
        intervalId = updateEveryMinute();
        expect( intervalId ).toBeDefined();
        expect( typeof intervalId ).toBe( 'object' );
      });
    });

##The Breakdown
	// see this in each test
	intervalId = updateEveryMinute();
    
	afterEach(function() {
      clearInterval( intervalId );
    });

`setInterval` and `setTimeout` return information when created so you can [clear them later](http://adam-back.azurewebsites.net/what-i-didnt-know-about-settimeout/). After each invocation of the tested function, I need to clear the interval so it doesn't actually call the `update` function.

---
	spyOn( global, 'setInterval' ).andCallThrough();
    
Since there is no `window` in Node.js, we'll create a spy on the `global` object. And, sure, let's call the real thing using `andCallThrough()`; no need to mock here!

---
	expect( global.setInterval ).toHaveBeenCalled();
    expect( global.setInterval ).toHaveBeenCalledWith( update , 60000 );
    
We expect `setInterval` to have been called, because that's basically all our function does. 

See that second test, though? It's jucy! 

I required the same function (`update`) in the test spec that I pass to the real function, so I can make a very real comparison without having to replicate all of the code for `update`. This won't save you time if you've passed `setInterval` an anonymous function--you'll just have to retype it.

---
	intervalId = updateEveryMinute();
    expect( intervalId ).toBeDefined();
    expect( typeof intervalId ).toBe( 'object' );
    
One more little thing. In the `window`, `setInterval` and `setTimeout` return numeric ids. However, in [Node.js](https://nodejs.org/api/globals.html#globals_setinterval_cb_ms):
> Returns an opaque value that represents the timer.

Huh? Excuse me? I didn't catch that. Let's actually go to the `timers`  [module](https://nodejs.org/api/timers.html#timers_setinterval_callback_delay_arg) for a better explanation.
> Returns a intervalObject for possible use with clearInterval().

Ok, so it's actually an object. Now, we're able to test the function's return value.

##Summary
- Ditch Jasmine's mock `setTimeout` and `setInterval`.
- Differences between `window` and Node.js:
	- `setTimeout` and `setInterval` are on the `global` object.
	- They return objects instead of just ids for clearing.
- Don't forget to clear the interval using the id object after each test.

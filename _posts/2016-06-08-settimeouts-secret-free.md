---
layout: post
class: 'post-template'
subclass: 'post'
title: "setTimeout's Secret Free"
date: 2016-06-08 17:06:14 +0000
slug: "settimeouts-secret-free"
description: "How to bind values to setTimeout, three different ways."
meta_title: "setTimeout's Secret Free"
ghost_id: 65
ghost_uuid: "2d066e57-1e1e-48ec-986a-dfc30a1d14e0"
---

Read the title how you wish, `setTimeout` has a secret it has been holding onto for `window.Infinity` milliseconds.

**tl;dr**: Solution 3.

#### The Problem
Because `setTimeout` is defined globally on the `window` object, the `this` binding frequently becomes an issue. Case in point:

```
// Goal: print 0, 1...8
for( var i = 0; i < 9; i++ ) {
  setTimeout(function() {
     console.log( i );
  }, 0);
}
```

Output:

![The number 9 printed 9 times](/assets/images/2016/06/Screen-Shot-2016-06-07-at-9-39-44-PM.png)

#### Solution 1
```
for( var i = 0; i < 9; i++ ) {
  setTimeout(function() {
     console.log( this );
  }.bind( i ), 0);
  // bind context
}
```

Output: 

![primitive values of 0 through 8 are printed](/assets/images/2016/06/Screen-Shot-2016-06-07-at-9-44-44-PM.png)

In this example, rather than binding a real context, we bind the only thing that matters to us--the variable `i`.

Now, why the weird PrimitiveValue output? You must bind to an object, not a primitive; as a result we bind to `new Number( i )`.*

#### Solution 2
```
for( var i = 0; i < 9; i++ ) {
  setTimeout(function( val ) {
     console.log( val );
  }.bind( null, i ), 0);
  // bind with args
}
```

Output: 

![ 0 through 8 are printed](/assets/images/2016/06/Screen-Shot-2016-06-07-at-9-52-06-PM.png)

In this example, we don't care about the context *thisArg* at all. Whatever is passed into `bind` after the *thisArg* becomes a parameter (`val`), which is fed into the anonymous function. 

#### Solution 3 (Personal Fave)
```
for( var i = 0; i < 9; i++ ) {
  setTimeout(function( val ) {
     console.log( val );
  }, 0, i);
  // Huh? The bind is gone!
}
```

Output: 

![ 0 through 8 are printed](/assets/images/2016/06/Screen-Shot-2016-06-07-at-9-55-33-PM.png)

A solution without `bind` and the namesake for this post. `setTimeout` doesn't just take a function and milliseconds as parameters, it also takes values which it will gladly pass to the function inside:

![documentation for setTimeout from MDN](/assets/images/2016/06/Screen-Shot-2016-06-07-at-10-01-21-PM.png)

###### Further Reading: 
- A quick review of JavaScripts's bind function can be found [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind).
- Read more about `setTimeout` at [MDN](https://developer.mozilla.org/en-US/docs/Web/API/WindowTimers/setTimeout).
- Learn the [difference](http://stackoverflow.com/questions/2381399/what-is-the-difference-between-new-number-and-number-in-javascript) between `new Number( 3 )` and `Number( 3 )`. 
- More on JavaScript [primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive).

*Thanks to [Andrew Teich](http://andrewteich.com/) for eloquently explaining binding, or lack-thereof, to primitives.

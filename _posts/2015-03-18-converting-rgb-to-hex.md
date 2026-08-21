---
layout: post
class: 'post-template'
subclass: 'post'
title: "toString()'s Hidden Power"
date: 2015-03-18 19:01:00 +0000
slug: "converting-rgb-to-hex"
ghost_id: 41
ghost_uuid: "d28151ca-4a26-4c63-95dd-842cd0ebacad"
---

#The Problem
Convert an RGB color to hexadecimal format. [RGB](http://en.wikipedia.org/wiki/RGB_color_model) has three values representing red, green, and blue. Hexadecimal is a [base-16 number system](http://en.wikipedia.org/wiki/Hexadecimal).

#My Solution
    var convertNumberToHex = function( num ) {
      var hexDigits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
      var current = ['0','0'];
      var hexCounter = 1;
      var placeValue = 1;

      for ( var i = 1; i <= num; i++ ) {
        // if number is not at F
        if( hexCounter !== 16 ) {
        // replace it with the next highest
          current.pop();
          current.push( hexDigits[hexCounter] );
          hexCounter++;
        // if number is maxed out at F
        } else {
      // if it's not time to increase place values
          if( current[placeValue - 1] !== 'F' ) {
            hexCounter = 0;
            // increase the value of the digit previous to the PV we're changing
            current[placeValue - 1] = hexDigits[ hexDigits.indexOf( current[placeValue - 1] ) + 1 ];
            current.pop();
            current.push( hexDigits[hexCounter] );
            hexCounter++;
          } else {
            // Highest colors go is FF
            return 'FF';
          }
        }
      };
      return current.join('');
    };

    var rgb = function(n1, n2, n3) {
      var output = [];

      for (var i = 0; i < arguments.length; i++) {
        output.push( convertNumberToHex(arguments[i]) );
      };

      return output.join('');
    };
    
#A Better Solution
(credit [zhenghu](http://www.codewars.com/users/zhenghu))

    function rgb(r, g, b){
      return toHex(r)+toHex(g)+toHex(b);
    };

    function toHex(d) {
        if(d < 0 ) {return "00";}
        if(d > 255 ) {return "FF";}
        return  ("0"+(Number(d).toString(16))).slice(-2).toUpperCase()
    };
    
So, first...what the hell.

Second...the first function is easy. He farmed-out the actual conversion work, like I did.

But, `toHex`? That's the, wait for it...

#Magic
Any RGB value greater than 255 is FF, so this solution doesn't have to convert numbers forever, luckily.

That last line, though.

    "0"+(Number(d).toString(16))).slice(-2).toUpperCase()
    
Create a new number using the `Number(#)` constructor. That's weird, because it would be like saying `String('Adam')` to create a new string.

The magic here is that `Number.toString` takes an [optional parameter](file:///Users/adamback/Library/Application%20Support/Dash/DocSets/JavaScript/JavaScript.docset/Contents/Resources/Documents/developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Number/toString.html) which defines what base you want to use for the number system!

![](/assets/images/2015/03/Screen-Shot-2015-03-13-at-10-19-14-PM.png)

Then, if the solution needs to, it removes the first 0 and makes everything uppercase.

Genius. And readable.

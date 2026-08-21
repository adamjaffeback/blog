---
layout: post
class: 'post-template'
subclass: 'post'
title: "Breaking Out (of Nested For-Loops)"
date: 2015-04-30 02:03:36 +0000
slug: "breaking-out-of-nested-for-loops"
ghost_id: 42
ghost_uuid: "c2499e94-b9f4-4fb5-b061-0bfc3c5b7ab8"
---

# (Interview) Question

How do you break out of nested for-loops? Let's say you have:

    for( var i = 0; i < 10; i++ ) {
         for( var j = 0; j < 15;j++ ) {
             if ( j === 2 ) {
                 // break out of everything!
             }
         }
    }


# Answer
Labels! Who knew you could label for-loops?

	a: for( var i = 0; i < 10; i++ ) {
        b: for( var j = 0; j < 15;j++ ) {
            if ( j === 2 ) {
                break a;
            }
        }
    }

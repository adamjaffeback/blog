---
layout: post
class: 'post-template'
subclass: 'post'
title: "Part 3: Wait for It...Unit Testing Sever-Side Promises"
date: 2016-05-27 20:16:08 +0000
slug: "part-3"
published: false
ghost_id: 63
ghost_uuid: "c4fd60f2-3b31-480a-a4a8-696ed8fe81c9"
---

We'll chain two promise-based functions together to get a user, then produce their lat-long coordinates using the [Geocoder npm module](https://www.npmjs.com/package/geocoder).

Here's what we start with in pinpointUser.js:
```
var user = require( './models' ).user;
var geocoder = require( 'geocoder' );
var Q = require( 'q' );

exports.getUserById = function( id ) {  
  return users.findById( id );
};

exports.geocodeAddress = function( address ) {
  var deferred = Q.defer();
  geocoder.geocode(address, function ( err, data ) {
  // do something with data 
});
};
```

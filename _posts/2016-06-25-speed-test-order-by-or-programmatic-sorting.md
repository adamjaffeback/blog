---
layout: post
class: 'post-template'
subclass: 'post'
title: "Speed Test: Database vs. Programmatic Sorting"
date: 2016-06-25 00:05:22 +0000
slug: "speed-test-order-by-or-programmatic-sorting"
image: "/assets/images/2016/06/13316857_10108239682352394_1749657195416456453_o.jpg"
description: "What's quicker?  Should we use JavaScript to programmatically sort database entries server-side or rely on ORDER BY?"
meta_title: "Speed Test: Database vs. Programmatic Sorting"
ghost_id: 66
ghost_uuid: "65614e12-ce0e-493c-894d-386ea549500a"
---

## Background
I want to get 100,000 rows from my database in a specific order. Here's the model:

```
var event = {
	id: 1,
    time_start: 2015-05-15 23:31:27.547+00,
    time_stop: 2015-05-15 23:45:27.522+00,
};
```

I know that databases quickly order pre-indexed values, for example, auto-incrementing ids and foreign keys. What if I want to sort by 'time_start'? Would I be better off sorting programically in JavaScript?

## Node.js' Helpers
This story is as much about database performance vs. programatic sorting as it is about how to objectively measure quickness. Everyone can talk about theoreticals and time complexity, but what about comparing milliseconds to milliseconds?

We all know `console.log`, but what about `console.time`? This [function](https://nodejs.org/api/console.html#console_console_time_label) has been included in Node.js since the beginning (v.0.1.104). It's super easy to use:

```
console.time( 'test' ); // name the start
for( var i = 0; i < 1000; i++ ) {
	continue;
    // do something
}
console.timeEnd( 'test' ); // tell the console which timer to report on
```

Here's the output:

![Duration of .049ms printed in console to complete test.](/assets/images/2016/06/Screen-Shot-2016-06-24-at-4-29-15-PM.png)

## Ready, Set, Go
Here's the code for database (PostgreSQL through Sequelize) ordering:

```
var getData = function() {
  console.time( 'database' );
  return event.findAll( { order: 'time_start' } )
  .then(function() {
    console.timeEnd( 'database' );
  });
};

getData();
```
![](/assets/images/2016/06/Screen-Shot-2016-06-24-at-4-42-22-PM.png)

Here's the code to get unordered rows, then order programmatically:
```
var getData = function() {
  console.time( 'order' );
  return models.charge_event.findAll()
  .then(function( events ) {
    events.sort(function( a, b ) {
      return a.time_start - b.time_start;
    });
    console.timeEnd( 'order' );
  });
};

getData();
```
![](/assets/images/2016/06/Screen-Shot-2016-06-24-at-4-47-42-PM.png)

## Results
The database sorting is quicker, no matter how many times I run the tests. Could we use a better algorithm than the native `Array.sort` or complicate things with join tables? That's another post. 

Moral of the story: don't be afraid to lean on your database's `ORDER BY` command like I was.

---
layout: post
class: 'post-template'
subclass: 'post'
title: "Protractor Magic Console.log"
date: 2015-02-18 01:01:34 +0000
slug: "protractor-magic-console-log"
description: "Protractor uses console.log magically."
ghost_id: 36
ghost_uuid: "6beb6666-66e9-4a21-8c65-cfb7f32d0738"
---

This (somehow) works:

![](/assets/images/2015/02/Screen-Shot-2015-02-02-at-4-13-15-PM.png)

Get all the elements that match.
For each one of them, get the outer html.
Then, console log the result.

Protractor just knows what you want to `console.log`. Does this happen elsewhere in JavaScript?

I found it in the [docs](http://angular.github.io/protractor/#/api?view=ElementArrayFinder.prototype.each) and thought, "This must be wrong."

![](/assets/images/2015/02/Screen-Shot-2015-02-02-at-4-15-14-PM.png)

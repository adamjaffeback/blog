---
layout: post
class: 'post-template'
subclass: 'post'
title: "Update Node With Npm"
date: 2015-07-10 22:45:08 +0000
slug: "update-node"
ghost_id: 56
ghost_uuid: "14676068-7804-4bcb-9297-724382b12613"
---

To check your current node version
`node -v`

To update it, follow this guy's genious.
http://davidwalsh.name/upgrade-nodejs

Some of your local folders may fail now on `npm start` like this:
![](/assets/images/2015/07/Screen-Shot-2015-07-10-at-4-23-05-PM.png)

Use `npm rebuild` to hopefully take care of that ([src](http://stackoverflow.com/questions/28486891/uncaught-error-module-did-not-self-register)).

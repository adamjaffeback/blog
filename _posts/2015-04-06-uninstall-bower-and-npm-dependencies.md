---
layout: post
class: 'post-template'
subclass: 'post'
title: "Uninstall Bower & NPM Dependencies"
date: 2015-04-06 20:10:08 +0000
slug: "uninstall-bower-and-npm-dependencies"
cover: "https://momland.files.wordpress.com/2012/08/sock-basket1.jpg"
meta_title: "Uninstall Bower and NPM Dependencies"
ghost_id: 44
ghost_uuid: "bdd79033-26e3-4948-ae20-f2f8e62e5990"
---

#You're Guilty
And so am I.

We install packages we think we need, only to find out we don't. But, like a sock on the floor, we think "It's just going to clean itself up" and forget about it. Some time later, we notice we're loading a lot of dependencies our project no longer needs. All those socks have piled up and it's time to clean.

#Clean Up The Hard Way

To get rid of unneeded packages, the rough way is to:

1. Delete the folder from `node_modules` or `bower_components`.
1. Physically delete the reference in `package.json` or `bower.json`.

#The Easy Uninstall
Use the `--save` flag.

`bower uninstall <module> --save`<br>
and
`npm uninstall <module> --save`

both get rid of the folder and the reference in the `.json` files.

####More Flags
More reading about [npm uninstall](https://docs.npmjs.com/cli/uninstall) and [bower uninstall](http://bower.io/docs/api/#uninstall).

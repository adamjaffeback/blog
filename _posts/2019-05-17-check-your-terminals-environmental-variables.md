---
layout: post
class: 'post-template'
subclass: 'post'
title: "Check Your Terminal's Environmental Variables"
date: 2019-05-17 23:16:02 +0000
slug: "check-your-terminals-environmental-variables"
description: "Use env and grep to quickly check your terminal's environmental variables."
meta_title: "Check Your Terminal's Environmental Variables"
ghost_id: 68
ghost_uuid: "793e6134-b0bb-48be-bc0a-5c4ee2accc65"
---

Working between Python environments, Node.js servers, and command line access to PostgreSQL allows us to be nimble and productive, but it also means that it can be really easy to get your environmental variables crossed. Luckily, there's an easy way to check what your terminal's variables are:

`env`

[Here's the Linux Man page.](http://man7.org/linux/man-pages/man1/env.1.html)

If you don't already know this trick, you're going to be so, so happy you learned it today.

Open up your terminal and type `env`. It will likely spit out quite a few environmental variables at you, especially if you recently `SOURCE`ed something.

My giant list of variables, redacted about as much as the Mueller Report:

<blockquote class="imgur-embed-pub" lang="en" data-id="a/FROpNph"><a href="//imgur.com/FROpNph"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

One of the ways I use `env` most frequently is to double check that I'm connected to my local database before connecting to PostgreSQL in my terminal to ensure I'm not altering our staging or production databases:

`env | grep PGHOST`

This command filters through the results of `env` to show what you're actually searching for; in my case, that's that PGHOST is set to localhost and not a hosted endpoint.

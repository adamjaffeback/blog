---
layout: post
class: 'post-template'
subclass: 'post'
title: "Force Azure to Reinstall Bower Dependencies"
date: 2015-01-21 23:01:38 +0000
slug: "bower-resolutions-on-azure"
description: "Your local changes to bower have worked, but it's not deploying on Azure correctly."
meta_title: "Force Azure to Reinstall Bower Dependencies"
ghost_id: 31
ghost_uuid: "1723c82b-2314-40de-91b9-4a87aac5f653"
---

#Background
I'm working on an internal app for our company built with Angular; let's call it JobSearch. As soon as I took over JobSearch, the automatic deployment from GitHub stopped working, as if my magic. And by magic I mean, "F#$2 you, Adam."

Through a rather unfortunate series of events, I don't even have access to the deployment or said logs.  The only clue I had was this:

<i>When I merged updates, the Angular templates would change, but not the new controller code.</i>

#Fast Forward Three Work Weeks
In order to fix the bug, I figured I would need access to the deployment logs. It was the last assumption that I couldn't test locally. After [deploying as skeleton version of my app to my own Azure account](http://www.adam-back.com/deploy-a-mean-app-on-azure/), I found the bug: multiple bower dependencies needed different versions of Angular.

![](/assets/images/2015/01/Screen-Shot-2015-01-13-at-3-36-28-PM.png)

Not reading too closely, I selected a resolution for Angular **1.3.8** and saved it to the bower.json file.

<i>For the first time in three weeks, deployment was working again.</i>

![](/assets/images/2015/01/Screen-Shot-2015-01-13-at-3-40-27-PM.png)

Do a little happy dance.

#A Show-Stopping Problem
The team which uses JobSearch found that they could not longer invite users to use the app. That's a huge problem, because there is no sign-up; it's by invitation only.

Long-story, short: I picked the wrong resolution. Look again:

![](/assets/images/2015/01/Screen-Shot-2015-01-13-at-3-36-28-PM.png)

The only dependency that doesn't resolve to 1.3.8 is the first one. It will only work with 1.2.28.

Ok, easy fix. Update the bower.json file to the new resolution.

If that worked, this wouldn't be a blog post.

#Blame Azure or Bower?
After merging that commit, the site redeployed, but had the same issue.

Using Azure's visual studio online, I could see that the bower file has indeed updated to the correct resolution version.

![](/assets/images/2015/01/Screen-Shot-2015-01-12-at-5-01-44-PM.png)

However, the version of Angular in the bower_components directory was still 1.3.8.

On deployment, Azure runs `bower install`, but says, "Hey, I already have Angular. I shan't download another," despite the resolution addition to the bower file.

I manually edited the bower.json resolution to 1.2.28 locally and tried `bower install`. 

*Nothing. Like I never changed the resolution. I still had Angular 1.3.8.*

Blame bower.

#Failures
I needed to force Angular to update to the correct version on Azure. Here's what I tried:

1. Added dependency I didn't need, hoping that it would reinstall all dependencies. It only installed the new dependency.
1. Decoupled source control from GitHub, then recoupled. This worked, but I do not have access to the production site's deployment to try this.
1. Changed Angular's version to match the version of the resolution. Still maintained incorrect, previous version.

#Success
Let's think: how did I solve this locally? 

I deleted the bower_components directory and reinstalled everything using `bower install`.

Thanks to [Andrew Teich](http://andrewteich.com) and a single line of bash scripting, we changed the deployment file to do just that.

![](/assets/images/2015/01/Screen-Shot-2015-01-13-at-4-18-06-PM.png)

Now, every time the site deploys, it wipes the existing bower_components directory:
`rm -rf public/bower_components`

Then, `bower install` starts everything fresh!

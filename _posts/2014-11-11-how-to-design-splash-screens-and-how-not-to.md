---
layout: post
class: 'post-template'
subclass: 'post'
title: "Go Far, Go Fast (iOS Design)"
date: 2014-11-11 20:05:27 +0000
slug: "how-to-design-splash-screens-and-how-not-to"
cover: "/assets/images/2014/11/Grand-Canal-Venise-1905.jpg"
description: "Ionic is great. Designing as a team is hard. Creating app splash screens and icons for every device known to man is impossible."
meta_title: "Go Far, Go Fast (iOS Design)"
ghost_id: 19
ghost_uuid: "224985c5-f6e7-4897-94df-9ccd93ec3cee"
---

<h5>Confessions Pt.1</h5>
I have a confession to make: I haven't always been good at collaborating.

The truth is, throughout years of schooling, I learned to loathe 'groupwork' because it meant I ended up doing more than my fare share. Emphasis on *more*.

Despite this negative feeling, I knew there was a bigger truth:
>"If you want to go fast, go alone. If you want to go far, go together." -African Proverb

During these last two months, I've made an enormous amount of progress learning to work together with groups. Coding is decidedly better when you've got people to bounce other ideas off.

My family back home is suprised that I'm not holed-up in some basement, Twinkie wrappers and Red Bull cans strewn about. **Coding is a team sport.** Don't pull a brain muscle.

Five times out of ten, when I ask a peer for help, I can't even replicate the problem. Magic. Problem solved!

Four times out of ten, when I ask a peer for help, the problem gets solved collaboratively in less than 20 minutes. All that grinding for 20 minutes!

Two brains are better than one in the same way two eyes are better than one. Cover the same intellectual ground, twice as fast, looking for the answer or fix.

One time out of then, they can't figure it out either, and we both grind through together like a Band of Brothers, knowing that 'war' has brought us closer in the end. We'd die for each other, or minimally, help each other out when the code gets tough.

---
<h5>Confessions Pt.2</h5>

Now, if there ever were a case when collaboration is not the way to go, it would be designing artistic elements.

Art is less iterative than code. When the designer presents a concept, it will pretty much be the final product with more polish. Programmers may think, "Oh, I don't like that font or those colors right now, but it'll get better." Because, frankly, that's how code works. You write and refactor. There isn't a lot of refactoring in art unless you're going to change the whole piece.

Point: trust your designer. Give clear, critical feedback early in the process or forever hold your peace (and your tounge)!

---
<h5>Confessions Pt. iOS</h5>

My team has been using Ionic to develop an app for the iOS App Store. Ionic has some good tutorials about adding a splash screen and editing the app tile, but they're lacking certain specifics.

Here are some things I've learned:
<ul>
	<li>Get really good at Photoshop.</li>
    <li>Make a huge(!) logo on a transparent background. Also make a light version of this logo for display on dark backgrounds </li>
    <li>Look for Photoshop scripts online to quicken your workflow. Instead of individually generating 20 different splash screen or icon sizes for different devices, let them do the work for you. I created one <a href='https://github.com/adam-back/PSScripts/blob/master/iconScripts.jsx'>here</a>. </li>
    <li>Icons are actually squares! <b>Those rounded edges are a lie!</b> Design a square icon, knowing iOS is going to make those round edges for you.</li>
    <li>I still don't understand 9-patch splash screens for Android, but there is a cool tool for it.</li>
    <li>For a splash screen to work in Ionic, you need to download a plugin. It's finicky. Sometimes it will work in the emulator, but break the app on a phone.</li>
</ul>

---
<h5>Additional Resources</h5>
**Splash Screen**
</br>
[Ionic: Customizing the Splash Screen](http://learn.ionicframework.com/formulas/splash-screen/)
</br>
[Android 9-patch Image Generator](http://romannurik.github.io/AndroidAssetStudio/nine-patches.html)
</br>
[Cordova Splash Screen Plugin](http://https://github.com/apache/cordova-plugin-splashscreen/blob/master/doc/index.md)

**Icons**
</br>
[Ionic: Adding an App Icon](http://learn.ionicframework.com/formulas/adding-an-icon/)
</br>
[Android Icon Generator](http://romannurik.github.io/AndroidAssetStudio/index.html)

**Documentation for Phonegap**
</br>
[Icon and Splash Screen Sizes](http://docs.phonegap.com/en/3.4.0/config_ref_images.md.html#Icons%20and%20Splash%20Screens)

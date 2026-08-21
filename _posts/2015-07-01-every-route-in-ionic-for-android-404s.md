---
layout: post
class: 'post-template'
subclass: 'post'
title: "Every Route in Ionic for Android 404's"
date: 2015-07-01 23:42:38 +0000
slug: "every-route-in-ionic-for-android-404s"
ghost_id: 55
ghost_uuid: "583f83f7-448a-4d6b-9f59-1d2550a4cfdf"
---

##Pick Your Poison
For JavaScript developers who want to develop a mobile app (like me), you have arguably three choices:
1) Learn two new languages: Java (Android) and Swift/Objective C (iOS)
2) Use Phonegap.
3) Use Ionic.

Ionic is cool because it allows you to use Angular.JS on top of Phonegap to keep code organized with an MVC-framework. In the six months I've used Ionic, it's come a long way. Using Cordova plugins almost never worked, not it's almost plug-and-play.

##404
After developing an app locally and creating a hosted server, I decided to try my app on my Galaxy Note 4. The process is pretty simple, unless the cable you're using magically doesn't allow data transfer. Mine didn't and it drove me crazy...I tried ever trick in the book except switching out the hardware.

One the app was finally on my phone, all I got from my server was 404's. 

Was it Elastic Beanstalk restricting access by IPs? No. 

Was the route correct in the app? Yes. 

Am I sure it was working locally? Yes.

Is it a bug that someone else has encountered before? Yes. 

Is it something that you could've, in your wildest dreams and imagination, thought of or fixed. No.

Of course not.

##Crosswalk
Aparently, Ionic started using something called [Crosswalk](http://blog.ionic.io/crosswalk-comes-to-ionic/) to improve browser performance in Android. It dramatically improves browser performance because nothing will load anymore. Very quick rejections.

Read this [post](http://forum.ionicframework.com/t/crosswalk-and-http-doesnt-work/20275/17) top-to-bottom. Some very smart people get together and determine that Crosswalk is making their apps break, then suggest a solution.

##Solution
1. Add Cordova Whitelist

        npm install cordova -g
    	cordova plugin add cordova-plugin-whitelist
        
2. Add these to `config.xml` in your Ionic project's root folder
	
        <access origin="*"/>
        <allow-intent href="*"/>
        <allow-navigation href="*"/>
        
	   ![](/assets/images/2015/07/Screen-Shot-2015-07-01-at-4-41-38-PM.png)

3. Rebuild and run the app on Android

        ionic build android
        ionic run android (with your device plugged in)
        
##Thanks
Thanks to the special people in this [post](http://forum.ionicframework.com/t/crosswalk-and-http-doesnt-work/20275/17). I wouldn't have figured this out on my own.

---
layout: post
class: 'post-template'
subclass: 'post'
title: "Geolocation in Mozilla OS"
date: 2014-12-18 00:35:41 +0000
slug: "geolocation-in-mozilla-os"
ghost_id: 26
ghost_uuid: "ffad7320-a43a-41d4-9763-62abdc77317b"
---

#Introduction
Why Adam, I didn't know you're developing mobile apps using Mozilla OS!

I'm not. 

I answered this [question](http://stackoverflow.com/questions/27396213/how-show-alert-for-enabling-gps-in-mozilla-os-app/27537186#27537186) on Stack Overflow in hopes of cold-hard ~~cash~~ karma:

![Stack Overflow GPS Question](/assets/images/2014/12/Screen-Shot-2014-12-17-at-4-19-55-PM.png)

Now, full-disclosure: I am a GPS geek. I was a [Geocacher](https://www.geocaching.com/play), which is like a giant treasure hunt. They're also critical to my use in [Search and Rescue](http://marinsar.org/).

Ok, I know you really came here for the
#Answer
###Clarifying the Question:
Here's the user flow which I understand from the asker:

 1. The user wants to use some part of your Mozilla OS app which requires GPS.
 2. The app should check if the GPS is on.
 3. If the GPS is off, prompt the user to turn their GPS on.
 
 
###Code
    // geolocation is available 
    if ("geolocation" in navigator) {
      
      // get position
      navigator.geolocation.getCurrentPosition(function(position) {
        do_something(position.coords.latitude, position.coords.longitude);
      });

      // geolocation IS NOT available
    } else {
      // Notify the user to turn their GPS on
      new Notification("Please enable your GPS"); 
      
      /*Disable whatever feature you were planning on using until user comes back
        with the GPS turned on and this logic runs again.*/
    }

###Explanation

In Mozilla OS, developers do not have direct access to the GPS. Here's the research that led me to this conclusion:
 
After no mention on the [Geolocation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) page, I looked on the ["App permissions page"](https://developer.mozilla.org/en-US/Apps/Build/App_permissions) near the bottom in the section titled "Internal (Certified) app permissions". There is access to bluetooth, camera, and  WiFi, but not GPS. Then I started looking at the Internal (Certified) [settings](https://developer.mozilla.org/en-US/docs/Web/API/Navigator.mozSettings) page, where I found some additional hardware, but nothing regarding the GPS. 

**He already found the workaround on the [Geolocation documentation page](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation):** you check to see if the Geolocation service will return a location. If it's `undefined`, then the GPS isn't turned on. Hacky, but that's what we've got.

If the GPS is off, you want to alert the user, asking to turn it on. According to the ["App permissions page"](https://developer.mozilla.org/en-US/Apps/Build/App_permissions), in app development, you can notify the user in this way without asking for permission ("Allow for all installed App types")
![App permission picture](/assets/images/2014/12/Screen-Shot-2014-12-17-at-3-55-47-PM.png)

In the browser, you would have to ask to show notifications first using [Notification.requestPermission()](https://developer.mozilla.org/en-US/docs/Web/API/notification).

The solution code given above is for [Firefox OS 1.2+ (or Gecko 22+)](https://developer.mozilla.org/en-US/docs/Web/API/notification#Browser_compatibility); if your app is using a earlier version, use `mozNotification`.


###Summary (Anik's Specific Questions)

> But this check only browser support GPS or not?

The same Geolocation service is used for browser *and* Mozilla OS apps. This is evidenced by the [App Permission](https://developer.mozilla.org/en-US/Apps/Build/App_permissions) geolocation link to the [Web API Interfaces Geolocation API page](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation) which says, "This allows a Web site **or app** to offer customized results based on the user's location." Regardless of the device type, ["For privacy reasons, the user is asked for permission to report location information."](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation)

> how can i do that ? Any Suggestions ?

See the code above and follow the many links to find sources for how to use the Geolocation service and create user notifications.

###Update
I got the bounty! Woo!

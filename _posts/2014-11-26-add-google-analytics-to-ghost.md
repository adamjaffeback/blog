---
layout: post
class: 'post-template'
subclass: 'post'
title: "Add Google Analytics to Ghost"
date: 2014-11-26 22:10:27 +0000
slug: "add-google-analytics-to-ghost"
description: "How to add Google Analytics to Ghost blogs hosted on Azure."
meta_title: "Add Google Analytics to Ghost"
ghost_id: 22
ghost_uuid: "4c9aab10-94b2-4d0f-b129-c447fb138f06"
---

Thanks to [Jon Henshaw](http://blog.henshaw.me/ghost-blogging-essentials/) for his tutorial on this topic.

#####Analytics
I enjoy writing this blog. It's satisfying to know that people like reading it. Aside from peers commenting on my blog in-person, I've been relying on Azure to tell me about my traffic.

![Azure Request Graph](/assets/images/2014/11/Screen-Shot-2014-11-26-at-1-16-24-PM.png)

---

#####Google Analytics
In order to learn more, you can add a service by Google to get more, and even real-time, information about visitors. For small websites like mine, this is "internet" free.

Even better, it's a relatively simple process to update your Ghost blog to give you more information using this service.

---

#####Step-by-Step
I deploy from source control on GitHub using [Kevin Meurer's](http://kevinmeurer.com/) cloned [repo](https://github.com/kmeurer/GhostAzureSetup). So the end of these steps will be specific to that kind of deployment.
<ol>
<li>Clone down a local copy of your Ghost code.</li>
<li>Navigate to [http://www.google.com/analytics/](http://www.google.com/analytics/). Log in using any gmail account.</li>
<li>Fill in the form with information about your blog.</li>
![How to create a new account](/assets/images/2014/11/Screen-Shot-2014-11-26-at-1-24-13-PM-1.png)
<li>Copy all of the code on the next screen.</li>![Copy the code on the next page](/assets/images/2014/11/Screen-Shot-2014-11-26-at-1-27-50-PM.png)
<li>Open the code for your ghost blog and open the default.hbs file. It should be at `/content/themes/casper/default.hbs`. If you're using a different theme, navigate to that theme instead of casper.</li>
<li>Past that script code at the bottom of you head tag.</li>
######Before
![Before, without script tag](/assets/images/2014/11/Screen-Shot-2014-11-26-at-1-45-29-PM.png)
######After
![After, with script tag](/assets/images/2014/11/Screen-Shot-2014-11-26-at-1-46-07-PM.png)
<li>Save, commit the change, then push it up to source control. Sit back and let it deploy!</li>

---

#####Next Steps
Make some posts, share with friends. Hopefully they're good friends and they read your blog.

Now to get meta: 
I'll update this blog with data I receive from Google Analytics...

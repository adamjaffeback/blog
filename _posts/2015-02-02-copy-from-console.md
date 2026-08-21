---
layout: post
class: 'post-template'
subclass: 'post'
title: "Copy From the Console"
date: 2015-02-02 19:37:55 +0000
slug: "copy-from-console"
description: "Copy and pasting won't work in the console. Learn how to copy logged data so you can paste it into your text editor."
ghost_id: 32
ghost_uuid: "2888b460-75ed-4711-b654-79e813637586"
---

##Problem
I'm working on a problem right now where I get large amounts of data back from a function.

That data might not be correct. 

I need to inspect it, so I log it to the console. Unforuntaly, I have to go through the nested array by hand. It's not very fun. 

![Large nested array in the console.](/assets/images/2015/01/Screen-Shot-2015-01-23-at-4-54-24-PM-1.png)

Wouldn't it be awesome if I could save that whole logged array and search it in  a text editor?

##How to:
<ol>
<li>Open your browser console.</li>
<li>Right click on the logged object. Click "Store as Global Variable".
![Box showing the options for right click](/assets/images/2015/01/Screen-Shot-2015-01-23-at-4-55-45-PM.png)
This saves the object to a temporary variable, which is returned in the console.
![Screenshot of temporary storage variable](/assets/images/2015/01/Screen-Shot-2015-01-23-at-4-56-16-PM.png)
<li>In my case, the temporary variable is named <code>temp1</code>. To copy it to the system-wide "clipboard", enter <code>copy(temp1)</code> in the console.
![Screenshot of copying storage variable](/assets/images/2015/01/Screen-Shot-2015-01-23-at-5-00-21-PM.png)
</li>
<li>Open your favorite text editor and paste (<code>Cmd-V</code>).
![5000 lines of code in sublime text editor](/assets/images/2015/01/Screen-Shot-2015-01-23-at-5-02-04-PM.png)
</li>
</ol>

##So Much Data!
As you can see in the screenshot above, there's a ton of data...almost 5000 lines! There's no way I could verify all of it myself. Now I have the data in a file and can write a quick script to do the checking for me.

---
layout: post
class: 'post-template'
subclass: 'post'
title: "The View is Grand"
date: 2014-09-27 04:15:44 +0000
slug: "the-view-is-grand"
description: "A (real) beginner's guide to Backbone.js."
meta_title: "The View Is Grant"
ghost_id: 5
ghost_uuid: "19e1df6e-2c17-4193-9d5d-cc195a2b9525"
---

![Women on The View TV show](/assets/images/2014/09/theview.jpg)
<h5>No, not that one.</h5>

![Diagram of how backbone click works](/assets/images/2014/09/FullSizeRender.jpg)

<h5>This one.</h5>

---
<h3>Backbone FAQ</h3>
In preparation for Hack Reactor, I completed both Backbone.js tutorials on <a href="https://www.codeschool.com/">Code School</a>. I didn't understand anything past the first activity.

What most Backbone references lack is a <u>really</u> basic introduction with no assumptions about previous technical knowledge.

**What is Backbone?**

Backbone is a way to organize code. When you're typing hundreds or thousands of lines, you can easily lose track of where different functions, variables, and classes are.

To the beginner (me), it appears as if Backbone causes far more trouble than it's worth due of the layers of abstraction involved. For example: instead of just inserting a new element onto the webpage (one step), you have to add the element to the model, which will register in the view, which in-turn renders the page with your new element.

I'm told using Backbone pays off in the long-run.

**What does MVC mean?**

Backbone is not the first of it's kind. Backbone belongs to a way of designing webpages ('architechture'), called Model-View-Controller.
![MVC tree](/assets/images/2014/09/500px-MVC-Process-svg.png)
"<a href="http://commons.wikimedia.org/wiki/File:MVC-Process.svg#mediaviewer/File:MVC-Process.svg">MVC-Process</a>" by <a href="//commons.wikimedia.org/wiki/User:RegisFrey" title="User:RegisFrey">RegisFrey</a> - <span class="int-own-work">Own work</span>. Licensed under Public domain via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.

MVC is a way of isolating tasks to reduce interdependability. It reduces (almost eliminates) all of the hardcoding one does to make interactive web applications.

**What is a model?**
A model is the basic storage device in the MVC model.

**What is a view?**
A view shows the model on the page. It is also listening to the model. When the model changes, the view updates your page with the new information.

**What is a controller?**
A controller sends updates to the model. <u>In Backbone, controllers do not exist independently as their own classes. They are part of the view.</u>

**What is a collection?**
Just like in plain English, a collection is a grouping of similar things. Backbone is similar: a collection is a group of models.
***
<h5>How does Backbone differ from what I'm used to?</h5>

I'm going to give an example in jQuery then explain how it would (kind of) translate to Backbone. It should follow the above diagram pretty closely.

When I first started moving things around on webpages, I was using jQuery . There is a button on a webpage and you click it. This click handler is behind the scenes, waiting to do something when you click on the button:
	`$('button').click(function() {
    friendList.push(this);
});`

This is pretty legible. When the button gets clicked, a function runs that adds a friend to your friend list.

In Backbone, the view is waiting for the user to click on the button. When they do, it calls a function (controller). The function emits an "click event" which echos through your code for anything that is listening. It's yodeling, basically.

You set "listeners" throughout your models: ` this.listenTo()`. The listerners wait to hear the click happen. In our case, the model may hear the click and adds a friend to your friend list.

When your friend is added to the model, the view attached to the model realizes there's been a change. You've added a friend that is not yet displayed on the screen. That's not right, so the view re-renders (displays stuff) and now your updated friend list is on the screen.
***
<h5>Why? A million times, why?</h5>
Because it's state of the art to have soft-connections between elements instead of hard-coding cause-and-effect relationships. I don't quite know what that means yet, either.

The picture below is an example of the thought process that goes behind one click and the two actions we want to accomplish as a result of that click

Click a song. As a result, add the song to the playlist and play it.

![Diagram of how a click echos through the system in Backbone](/assets/images/2014/09/FullSizeRender-1.jpg)

What I can tell you is this: the alternative, creating an event handling system from scratch is just as messy and equally difficult. You benefit from using Backbone because of the community of support arround it: there's probably an answer to your question somewhere on the internet.

*"Again, why?"* 

Besides the fact that it's listed on a lot of job applications as a necessary requirement...

A lot of smart people have already decided that Backbone is a good idea. They build their web apps with it. They leave their jobs for greater fame and fortune. You replace them as a junior engineer, meaning you will have to maintain their code. You do not get to rewrite their code from scratch without Backbone.

Sorry for the bad news.

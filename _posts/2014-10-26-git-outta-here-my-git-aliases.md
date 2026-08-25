---
layout: post
class: 'post-template'
subclass: 'post'
title: "Git Faster (My Git Aliases)"
date: 2014-10-26 06:23:02 +0000
slug: "git-outta-here-my-git-aliases"
cover: "/assets/images/2014/10/475535_10150866953388795_980256035_o.jpg"
description: "Commit frequently, but work quickly by setting git aliases."
meta_title: "Git Faster (My Git Aliases)"
ghost_id: 16
ghost_uuid: "5acda0d1-343f-4ebe-af6e-6f8194a8f75a"
---

<b>The Problem:</b>
Half tutorial, half work flow post.

I commit a lot, which is a best practice. If I make mistakes which aren't easily fixable, I can easily revert to a previous commit.

When [Laurie Voss](https://twitter.com/seldo) from npm spoke at Hack Reactor, he mentioned that there is a great amount of efficiency to be gained from optimizing frequent tasks.

<b>The Math:</b>
Let's estimate that each commit takes me 30 seconds from `git status` to saving the commit message.

If I commit 20 times per day, that's about 10 minutes gone. So for each week, that's 50 minutes I could be ~~making tea~~ writing more code. Just to hammer the point home, that's around 42 hours per work year.

<b>The Solution</b>
To make things quicker and reduce strain on my hands, I've added some aliases which allow me to make git commands more quickly.

There are many ways to accomplish this, all on Stack Overflow and the like, but here's how I do it.


<ol>
<li>First, I set an alias I took from <a href:'http://ianlunn.co.uk/articles/quickly-showhide-hidden-files-mac-os-x-mavericks/'>here</a> to quickly access hidden Mac files. I type <i>showFiles</i> in the terminal to show any hidden files I want to access. When I'm done, I type <i>hideFiles</i> and they're all gone. My Finder looks like this when I'm showing the hidden stuff:

![Mac Finder with hidden files visible](/assets/images/2014/10/Screen-Shot-2014-10-25-at-10-42-42-PM.png)
</li> 
<li>Open your <i>.bash_profile</i> file using your favorite text editor. My file is in my user folder near the top (see the picture above). Oh hey! Look what's there...the show and hide file aliases you've already created! 
![Aliases in bash profile file](/assets/images/2014/10/Screen-Shot-2014-10-25-at-10-45-40-PM.png)
</li>
<li>Add your alias. My favorite is shown below. First add to the global <i>.gitconfig</i> file in the terminal:
![Git config in terminal](/assets/images/2014/10/Screen-Shot-2014-10-26-at-12-18-21-AM.png)
Then add the alias to the bash profile. <u>Follow the example syntax dutifully!</u> Whitespace and single quotes matter here.
![](/assets/images/2014/10/Screen-Shot-2014-10-26-at-12-19-11-AM.png)

Save the file and restart the terminal. Now you can just type <i>gs</i> in the command line instead of <i>git status</i>. Magic.
</li>
</ol>

<b>Oh you fancy, huh?</b>
This alias will `git push origin {whatever branch you're currently on}`. (no need for editing the `.gitconfig` file)

![git push origin alias](/assets/images/2014/10/Screen-Shot-2014-10-25-at-11-05-28-PM.png)

On master branch? Type `po` and you have `git push origin master`.

On feat/SuperAwesomeFeature branch? 
Type `po` and you have `git push origin feat/SuperAwesomeFeature`. 

Super quick and awesome for all of those branches you've been cutting.

![Tree stands again after being cut by chainsaw](http://www.gifbin.com/bin/042014/1398183455_fallen_tree_stands_up_after_being_cut.gif)

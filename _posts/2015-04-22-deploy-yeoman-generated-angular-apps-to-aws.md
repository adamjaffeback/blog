---
layout: post
class: 'post-template'
subclass: 'post'
title: "Deploy Yeoman-Generated Angular Apps to AWS"
date: 2015-04-22 21:01:40 +0000
slug: "deploy-yeoman-generated-angular-apps-to-aws"
ghost_id: 46
ghost_uuid: "b5f11a86-6998-45b3-b553-fa7db686fd74"
---

##The Generator
I'm creating an app based off of the [Yeoman Angular fullstack generator](https://github.com/DaftMonk/generator-angular-fullstack).

It does a lot of cool things, like generating boilerplate, simplifying workflow with many Grunt tasks, and including lots of testing options.

I ran into two problems with it:
1) It doesn deploy to AWS out-of-the-box.
2) It isn't easy to use any database besides MongoDB.

This post deals with the former. I'll write another soon that deals with swapping-out MongoDB for sequelize.

##Why doesn't it work?
The docs for this generator make it easy to [deploy to heroku](https://github.com/DaftMonk/generator-angular-fullstack#heroku).
![](/assets/images/2015/04/Screen-Shot-2015-04-17-at-1-58-43-PM.png)
![](/assets/images/2015/04/Screen-Shot-2015-04-17-at-1-58-52-PM.png)

The way that [`grunt-build-control`](https://github.com/robwierzbowski/grunt-build-control) accomplishes this is by establishing a remote and pushing to it.

Elastic Beanstalk on AWS doesn't have remotes.

Not only that, but it *only* pushes the `dist/` directory.

`eb deploy` will push *everything*.


##The Workaround
Sadly, you won't be able to use `grunt`, but you'll be ok, I promise.

1. Remove any Elastic Beanstalk files in the repo. FYI, they're hidden.
1. Using the terminal, `cd dist/` from the project's root folder.
1. Run `git init` to create a local git repo within `dist/`.
1. Make an initial commit, because `dist/` has always been .gitignore-d.
1. Run 1eb init`, `eb create`, `eb deploy` as normal within `dist/`.
1. Set your environmental variables, if you need them.
1. `eb open`, with your fingers crossed.



#####Other reading
[Stack Overflow](http://stackoverflow.com/questions/18325510/how-to-deploy-a-yeoman-build-to-aws-node-js/29709031#29709031)

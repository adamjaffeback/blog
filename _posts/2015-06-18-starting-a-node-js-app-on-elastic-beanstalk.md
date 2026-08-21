---
layout: post
class: 'post-template'
subclass: 'post'
title: "Starting a Node.js App on Elastic Beanstalk"
date: 2015-06-18 17:08:11 +0000
slug: "starting-a-node-js-app-on-elastic-beanstalk"
ghost_id: 53
ghost_uuid: "f85f1b0e-c0f3-47e0-a2ef-1361324dbe0b"
---

Please have an AWS account and install the AWS-CLI.

##The Simple Stuff
1. In the root directory of your app, `eb init` then `eb create`.
1. Once the app is at a point where you want to deploy, `eb deploy`.
1. `eb open` will hopefylly launch your app in a web browser.

##When it Doesn't Go to Plan
####Download the Logs
On the logs tab, click the "Request Logs" button on the upper right.
![](/assets/images/2015/06/Screen-Shot-2015-06-03-at-1-22-01-PM.png)

You can view the last 100 in the browser, but the full logs need to be downloaded and unzipped.

Look for npm install fails and anything that looks out of the ordinary.

####Turn Off Proxy Server
I don't think I've ever deployed an Elastic Beanstalk app successfully the first time. There's nginx 502 "Bad Gateway" errors and the recently fun 503 "Server at Capacity" error.

My first step, when debugging, is to turn off the proxy. In the configuration tab on AWS:

![](/assets/images/2015/06/Screen-Shot-2015-06-03-at-1-12-43-PM.png)

Your app will restart and you can get better access to what is causing the 502.

####Custom Start Command
I create many apps with the [express-generator](http://expressjs.com/starter/generator.html). To start this server, you run `npm start`. This commmand actually runs `./bin/www` **not** `app.js`.

This causes a problem for Elastic Beanstalk because first it tries `app.js`, then `server.js`, and *finally* `npm start`. Well, it breaks when it runs `app.js` and doesn't actually continue.

Fix this on the configuration tab:


![](/assets/images/2015/06/Screen-Shot-2015-06-03-at-1-21-06-PM-1.png)

####Deploy It Somewhere Else
Try Heroku or Azure, they have better access to error logs. Fix any issues you find, then try to redeploy to AWS.

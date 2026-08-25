---
layout: post
class: 'post-template'
subclass: 'post'
title: "Deploy a MEAN app on Azure"
date: 2015-01-06 22:12:44 +0000
slug: "deploy-a-mean-app-on-azure"
cover: "http://blog.langoor.mobi/wp-content/uploads/2013/07/meanstack-624x250.jpg"
description: "Step-by-step for deploying a MEAN stack app on Azure."
ghost_id: 28
ghost_uuid: "b99f3d8c-fbf2-432a-9b07-049ec1f1dd89"
---

#The Need
Believe it or not, with the proliferation of [MEAN](http://en.wikipedia.org/wiki/MEAN)-stack apps on the web, I couldn't find a tutorial for how to deploy one on Azure. Or Heroku. Nor AWS. 

For this step-by-step, I'll be using code which has separate GitHub repos for the client and server.

There will be a lot  differences between your app and mine, which is one reason deployment tutorials aren't often written. They're too case-by-case. **My goal** is really to write a high-level answer to

#The Question
How do I deploy an app made with MongoDB, Express, Angular, and Node.js using Microsoft Azure?

Shouldn't be [too painful.](http://img3.wikia.nocookie.net/__cb20120405034816/creepypasta/images/6/6b/Squidward_headdesk.gif)

The bold headers are generalized steps to deploy any split MEAN-stack app:

<ul>
<li>Create a MongoDB with MongoLab</li>
<li>Deploy Your Server</li>
<li>Connect the Server to MongoDB</li>
<li>Deploy the Client</li>
<li>Set Environmental Variables</li>
</ul>
----

#Baby Steps

##Create a MongoDB with [MongoLab](https://mongolab.com/).
<ol>
<li>Log in to Azure.</li>
<li>Click <i>+New</i> at the bottom-left corner.</li>
<li>Open the Marketplace.</li>
<li>Find and select MongoLab then click the arrow to move to the next menu.
![](/assets/images/2015/01/Screen-Shot-2015-01-05-at-2-37-17-PM.png)
</li>
<li>Write a name for your database and select your service level. Move to the next menu.</li>
<li>Complete your purchase. (I just picked the free sandbox)</li>
</ol>


##Deploy Your Server
<ol>
<li>Click <i>+New</i> at the bottom-left corner.</li>
<li><i>Quick Create</i> a new website.
![](/assets/images/2015/01/Screen-Shot-2015-01-05-at-1-53-40-PM.png)
</li>
<li>Click on your newly-created "website" (it's really just the server).</li>
<li>To deploy code from the server repo, click <i>Integrate source control</i> near the bottom.
![Integrate source control](/assets/images/2015/01/Screen-Shot-2015-01-05-at-2-59-38-PM.png)
</li>
<li>Select GitHub, then sign in. Select the repo for your server. Don't forget to enter an alternative branch if you need to.</li>
<li>Confirm that your server deployed by navigating to the <i>Deployments</i> tab. You should see something like this:
![Successful deployment](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-17-26-PM.png)
</li>
</ol>

##Connect the Server to MongoDB
Most production code plans for hidden, environmental variables. The last step of this tutorial is dedicated to these variables. Here's an example from my server code:

![Connection info](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-34-10-PM.png)

My server looks for a database URL on Azure; if it doesn't find the environmental variable set, it assumes we're working locally. To find and set that environmental variable, follow these steps.
<ol>
<li>Using the left menu, navigate to the Marketplace tab.
![Marketplace tab](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-23-28-PM.png)
</li>
<li>Click on <i>Connection Info</i> and copy the MongoDB URI.
![](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-27-52-PM.png)
</li>
<li>Navigate back to your server by clicking <i>Websites</i> in the left menu. After opening the website, click on the <i>Configure</i> tab. Scroll down to <i>Connection Strings</i>.</li>
<li><code>DB_URL</code> will be the name of my string, per the example at the top of this section. The URI copied in step 2 is the value. Select <i>Custom</i> from the dropdown menu for the type of database. 

![Set connection string](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-39-47-PM.png)
</li>
<li>Click <i>Save</i> at the bottom menu bar.</li>
</ol>

##Deploy the Client
This will look *very* similar to the steps for deploying the server.

<ol>
<li>Click <i>+New</i> at the bottom-left corner.</li>
<li><i>Quick Create</i> a new website.
![Create client](/assets/images/2015/01/Screen-Shot-2015-01-05-at-3-53-17-PM.png)
</li>
<li>Click on your newly-created website.</li>
<li>To deploy code from the client repo, click <i>Integrate source control</i> near the bottom.
![Integrate source control](/assets/images/2015/01/Screen-Shot-2015-01-05-at-2-59-38-PM.png)
</li>
<li>Select the repo for your client. Don't forget to enter an alternative branch if you need to.</li>
<li>Confirm that your client deployed by navigating to the <i>Deployments</i> tab. You should see something like this:
![Successful deployment](/assets/images/2015/01/Screen-Shot-2015-01-06-at-1-17-14-PM.png)
</li>
</ol>

##Set Environmental Variables
In order for the client and server to know about each other, we need to set additional variables in Azure.

For example, the server expects us to define where we set the client so that it knows the 'base url':

![](/assets/images/2015/01/Screen-Shot-2015-01-06-at-1-24-06-PM.png)

####Set the Server Base Route
<ol>
<li>Open the server and navigate to the <i>Configure</i> tab.</li>
<li>Scroll down to <i>app settings</i>. Define the key and value appropriately given our code and deployed server. Here's the example from this tutorial.
![Create client](/assets/images/2015/01/Screen-Shot-2015-01-06-at-1-29-01-PM.png)
</li>
<li>Click <i>Save</i> at the bottom menu bar.</li>
</ol>

####Set the Server URL in the Client
Because the server is separated from the client, we need to tell the client where to make `http` requests.

![Set the server URL](/assets/images/2015/01/Screen-Shot-2015-01-06-at-1-59-37-PM.png)

<ol>
<li>Open the client and navigate to the <i>Configure</i> tab.</li>
<li>Scroll down to <i>app settings</i>. Define the key and value appropriately given what we named our server.
![Create client](/assets/images/2015/01/Screen-Shot-2015-01-06-at-2-00-27-PM.png)
</li>
<li>Click <i>Save</i> at the bottom menu bar.</li>
</ol>

#Additional Reading
[Azure - Why you gotta be so MEAN? (with apologies to Taylor Swift)](http://blogs.msdn.com/b/devfish/archive/2014/07/29/azure-why-you-gotta-be-so-mean-with-apologies-to-taylor-swift.aspx):
Great resource with many links for the mean stack.

[Node.js and MongoLab on Windows Azure](http://blog.mongolab.com/2013/02/node-js-and-mongolab-on-windows-azure/): MongoLab's tutorial for Azure.

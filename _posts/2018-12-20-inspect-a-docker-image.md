---
layout: post
class: 'post-template'
subclass: 'post'
title: "Inspect a Docker Image"
date: 2018-12-20 21:12:51 +0000
slug: "inspect-a-docker-image"
ghost_id: 67
ghost_uuid: "e7567e98-487d-4df8-8dd3-bfe9b563dceb"
---

I'm currently trying to dockerize my AngularJS Protractor tests. I kept getting a `File not found` error, but I was pretty sure I'd `COPY`ed everything to the image I needed. The easiest way to check is to get into the image yourself!

1. Find the image you want to inspect: `docker image`. Woa. That's a lot of images. Hopefully, you've been naming images, but you can see just how much bloat Docker can create. Copy the image name you want to inspect, but make a mental note to Google "remove unused Docker images."

2. Enter `docker run -it --rm <imagename> bash`. Run the image with interactive terminal (-it) and remove it when we exit out of bash (--rm). Now that you're in the image, you can `cd` and `ls` around to ensure you copied over all the files you wanted.

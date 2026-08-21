---
layout: post
class: 'post-template'
subclass: 'post'
title: "An Algorithmic Look at Lyft Line and UberPool"
date: 2015-02-24 21:35:27 +0000
slug: "an-algorithmic-look-at-lyft-line-and-uber-pool"
image: "/assets/images/2015/02/IMG_1578.JPG"
description: "Both of the algorithms match riders who are traveling to a similar destination, but this is where the similarity ends."
meta_title: "The Difference Between Lyft Line and UberPool"
ghost_id: 38
ghost_uuid: "873cdd41-93c9-4d42-a6c2-4ab6b17a4114"
---

##Context
Last Summer I worked as a Lyft driver for a few hours every morning commute in busy, downtown San Francisco. I was part of the first wave of drivers who implemented their new [Lyft Line](https://www.lyft.com/line) service. 

Within the last month, competitor Uber created its own spin on the share-your-rideshare option: [UberPool](http://blog.uber.com/uberpool).

##Similarities
Both of the algorithms match riders who are traveling to a similar destination. This allows you to share the cost of the ride with a stranger. 

The user experiece starts the same: open the app and select Line or Pool instead of the solo passenger options. Both apps fib a little to consumers by showing drivers within one-to-two minutes of pick-up from your current location. But, once you actually request the driver, that pickup time frequently increases to around ten minutes because you may not be picked-up first.

Once the driver arrives at your dropped pin or address, an in-app timer starts, giving you just over a minute to get into the car before the app asks the driver to leave you. If the driver marks you as a no-show, you get charged the company’s normal, five-dollar cancellation fee.

##Differences
When riders request a Lyft Line, they wait approximately one-to-two minutes while the app looks for a matching stranger, headed in the same direction. This is different from the normal experience, which normally places you with a driver within 30 seconds. Sometimes, no match is made; you get to pay the reduced cost of the Lyft Line, even though you’ll be traveling alone.

In Uber’s case, the algorithm designers decided to place all riders with a car immediately. As a result, you may be enroute to your destination, but the driver will receive an in-app notification that they need to make another pickup. 

##Summary
As a driver and a passenger, I prefer Lyft Line’s approach to the carpooling algorithm. You know ahead of time whether you will be with others and where those different pickup points are, allowing for better, more efficient route planning.

Uber’s algorithm, frankly, just meets users’ instant gratification needs by immediate placement with a driver. When the app inevitably alerts the driver to another pickup, the driver must redirect attention from the act of driving to accept the request and reroute. This reroute may also include backtracking. The driver must also accept this deviation under the scrutiny of passengers already in the car, possibly resulting in lower ratings for the driver.

As a result of these significant shortcomings in Uber’s algorithm, Lyft Line’s service outperforms in terms of safety and end-user satisfaction.

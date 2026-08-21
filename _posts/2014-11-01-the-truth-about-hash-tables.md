---
layout: post
class: 'post-template'
subclass: 'post'
title: "The Truth About Hash Tables"
date: 2014-11-01 03:21:50 +0000
slug: "the-truth-about-hash-tables"
image: "http://1.bp.blogspot.com/_eqGBdlhZB5k/S9NKHdomQ6I/AAAAAAAAAmk/Dl623RdNwzc/s1600/hashbrown.jpg"
description: "A basic overview of hash tables in JavaScript."
meta_title: "The Truth About Hash Tables"
ghost_id: 17
ghost_uuid: "3d101687-c658-458c-ad3b-82d84351b77c"
---

<h4>Let's Ask Google</h4>
Data structures were among the first things we learned at Hack Reactor. I knew what an array and object were, but not much else. Some of my classmates already knew binary search trees and graphs.

Arguably, the first difficult data structure you encounter in the curriculum is the Hash Table. A Google of "hash table" gives you this:
>In computing, a hash table (hash map) is a data structure used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the correct value can be found.

That doesn't help me one bit.

See what I did there?

"Bit"? Bazinga!

---
<h4>A Beginner's Definition</h4>

A hash table is an object. 

<center><u>Normal Object</u></center>
![rockStar Object](/assets/images/2014/11/Screen-Shot-2014-10-31-at-5-57-56-PM.png)

However, instead of just inserting a key-value pair, you're going to run the key through a hashing algorithm. A hashing algorithm takes an input, obliterates it, and returns a "hash".

![hashedKey is 1](/assets/images/2014/11/Screen-Shot-2014-10-31-at-5-59-45-PM.png)

In this example, our `hashFunction()` takes two parameters, 1) the key and 2) the maximum size of the hash table. You decide the maximum size. It will return a number (the hash) between one and two. We will use this hash in place of the key "Adam"; `insert` function will make use of this hash function.

![Insert function](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-03-00-PM.png)

<center><u>Hash Table</u></center>
![Hash Table](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-04-14-PM.png)
    
 ---
<h4>Why, for all things, why?</h4>
This is my common complaint in computer programming. The answer is generally, "Because it's a really good idea."

Hash tables are generally used to store sensitive data. The cool thing about hash functions is that they're one-way machines.

![hash comparison](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-05-43-PM-1.png)
 
There is a common misconception that hashing is the same as encryption. It is not. Encrypted data <b>can</b> be decrypted back to its original state. A hashed value cannot.
 
Hash tables are also pretty quick, with constant-time lookup as the goal.
 
 ---
 <h4>Collisions</h4>
 
![Basic hash table](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-07-18-PM.png)
 
In the hash table above, the key-value pair was stored as a nested array, but I never said why. It's to handle collisions.
 
This is a very small hash table; its maximum size is only two. It's bound to run out of room! What to do? Let's add some more items to the hash table first to find out.
 
![](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-09-22-PM.png)

So now the hash table looks like this:

![rockStars updated](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-11-49-PM.png)
    
The next insertion. Oh the next insertion.

![Add grandpa](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-12-56-PM.png)

I hid a complication in the insert function earlier. I ignored that a collision could ever happen. Let's fix that with pseudocode:

![Insert pseudocode](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-14-47-PM.png)
 
 In code:
 
 

![Insert code](/assets/images/2014/11/Screen-Shot-2014-10-31-at-8-17-29-PM.png)

So, now your hash table looks like this:
![Added grandpa to hash table](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-17-13-PM.png)
    
---
 <h4>What the internet won't tell you:</h4>
 (until now)
 
What do you do if you want to insert a key-value pair that has the same key:

![Add Adam Sandler](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-19-02-PM.png)

Adam will get hashed and be inserted into the 1 location.

![Added Adam](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-20-01-PM.png)

However, when you retrieve in a hash function, you only specify the key:
![Retrieve function](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-20-47-PM.png)

Which Adam will get returned? Which Adam are you even looking for?

<b>The truth!</b>
When you `insert` the same key, it should update the value. It doesn't replace the whole array or store a second Adam.

Let's update our code:
![Updated insert function](/assets/images/2014/11/Screen-Shot-2014-10-31-at-8-20-37-PM.png)
 
Now, when we add Adam Sandler, Adam Back will update to have a different last name.

![Updated key](/assets/images/2014/11/Screen-Shot-2014-10-31-at-6-37-27-PM.png)

Voila.

DISCLAIMER: While I've tried to cover a lot about hash tables, I still simplified some things. For example, when hash tables fill up, they can expand so less collisions occur.

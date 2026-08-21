---
layout: post
class: 'post-template'
subclass: 'post'
title: "How to Test Angular"
date: 2014-11-25 01:08:59 +0000
slug: "how-to-test-angular"
description: "How do I test all the Angular dependencies I injected? ionic? localStorageService? Services? Modals? Mock it."
meta_title: "How to Test Angular"
ghost_id: 21
ghost_uuid: "8403edec-03de-4412-8b99-864e19020768"
---

<figure>
<a href="https://imgflip.com/i/ejaw4"><img src="https://i.imgflip.com/ejaw4.jpg" title="One does not simply create an angular unit test"/></a>
</figure>
~~Give up.~~
Give it what it wants.
Fake it 'til you make it.

Now that you've exhausted technique one, you've begrudgingly realized you *do indeed* need to test your Angular app. My first production Angular app had 10 tests. I think they all asserted `true === true`. That's not helpful. For my current [Ionic/Phonegap, mobile-hybrid app](https://github.com/endevr-), I knew I actually needed to bite the bullet and test. 

Many of the resources I've found online say, 
> [Testing angular controllers is not hard...](http://angular-tips.com/blog/2014/06/introduction-to-unit-test-controllers/)

If that were true, you wouldn't likely be reading this blog. I find the examples often too simple and they never cover the most difficult things to test: spies, modals, local storage, and other random things that make Angular so awesome.

---
###1. Give it What it Wants (The Setup)
Use Karma with Jasmine. It was basically created to test Angular.

So you injected tons of dependencies into your Angular controller...
<figure>
![Controller injection](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-35-57-PM.png)
<figurecaption>Snippet 1a</figurecaption>
</figure>
<br/>
Providing you used all of them in your controller later, your tests are going to need access to these same dependencies. 

What do ya' know? You need to inject all of that stuff again when you're writing tests! Basically, you're going to create a new scope in the testing environment. This is accomplished with a **giant** `beforeEach` statement at the beginning of your tests:

<figure>
![Before each statement.](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-40-46-PM.png "Controllers")
<figurecaption>Snippet 1b</figurecaption>
</figure>
<br/>
Notice 2 things:
1. The \_underscores_. Angular has this built-in syntax to differentiate between injections and variable names in testing. Just trust me on this one, because I can't explain it any better.
2. Variable declaration is at the top, before the `beforeEach` statement.

---

###2. Start Easy
Just see if you set everything up correctly by seeing if there's a `$scope`.

<figure>
![Check if $scope is defined](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-45-05-PM.png)
<figurecaption>Snippet 2a</figurecaption>
</figure>
<br/>
*Please be defined, please be defined, please be defined.*

Here's the function we're testing:
<figure>
![closeNewItem modal function has a hide function inside](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-13-14-PM.png)
<figurecaption>Snippet 2b</figurecaption>
</figure>
<br/>

Let's makes sure it's defined and such:

<figure>
![Function is defined](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-51-38-PM.png)
<figurecaption>Snippet 2c</figurecaption>
</figure>
<br/>
*Please be true, please be true, please be true.*

---
###3. Your mission...
(if you choose to accept it).

One of the easiest ways I've found to keep unit tests as a unit, and not transcend into the world of integration tests, is to spy. Or, rather, to use spies.

For our example function above, this skill is critical, because it only calls another function. It makes no changes itself.

That's all it does.

Your test would look like this:
<figure>
![Spy test](/assets/images/2014/11/Screen-Shot-2014-11-24-at-2-55-40-PM.png)
<figurecaption>Snippet 3a</figurecaption>
</figure>
<br/>
1. Use the `spyOn` method. The first parameter is the object. The second parameter is the name of the method on that object as a string.
2. Call the wrapper function which contains the method you're spying on.
3. Set the expectation that your spy has been called. (Don't invoke `.hide`).

*Please be true, please be true, please be true.*

---

###4. Fake it 'Til You Make It (Mocking)
Not Mockingjay. Although at this point in Angular testing, it will probably feel like you're being hunted.

Not a funny joke. Although it may feel like the tests are laughing at your expense.

######Modals
In our Ionic app, we used modals for lots of user features. Modals don't navigate to a new endpoint, they simply pop up over the existing page. When you're on an app and they ask you to log in using Facebook, that's probably a modal.

Modals have native `modal.show()` and `modal.hide()` methods. Modal creation seems to be asynchronous, so when you try to test these methods, they fail, saying, 
>Cannot read property 'show' of undefined at Scope.$scope.showModal

So, bad news, the test we wrote above (Snippet 3a) actually fails. The way to fix this is to *fake it*. Again, whatever Angular wants, Angular gets. I don't think we're breaking the rules, we're just working within the confines of the framework.

**Since our modal seems to be undefined, let's define it.** 

Add a fake modal by the same name to the `beforeEach` statement. We'll also add `.show()` and `.hide()` methods to it. I used pseudoclassical instantiation.
<figure>
![How to mock a modal](/assets/images/2014/11/Screen-Shot-2014-11-24-at-3-10-36-PM.png)
<figurecaption>Snippet 4a</figurecaption>
</figure>
<br/>

The `void(0)` returns undefined, because we don't want these methods to actually do anything, we just want to `spyOn` if they've been called.

Here's the actual placement in the `beforeEach` statement, at bottom:
<figure>
![Where to add modal in before each statement, at bottom](/assets/images/2014/11/Screen-Shot-2014-11-24-at-3-12-16-PM.png)
<figurecaption>Snippet 4b</figurecaption>
</figure>
<br/>
Now, when you run the test, modal is defined and has the method `.hide`.

######Services
We wrote maintainable, modular code by using a service named `profileService`; now we're being punished for it in testing. It gets and updates the user's profile from the server.

Let's say the user was going to make some edits to their profile, but then decided otherwise, canceling the changes.
<figure>
![cancel changes function](/assets/images/2014/11/Screen-Shot-2014-11-24-at-3-30-56-PM.png)
<figurecaption>Snippet 4c</figurecaption>
</figure>
<br/>

We've already learned how to mock the modal and the `$scope` variables can be treated like any other 'normal' variables. 

What if we want to test if `profileService.getProfile` has been called?
<figure>
![Spy on cancel changes test](/assets/images/2014/11/Screen-Shot-2014-11-24-at-3-34-52-PM.png)
<figurecaption>Snippet 4d</figurecaption>
</figure>
<br/>

Just like before, `profileService` will be undefined. We'll have to fake it by creating a fake service in the before each statement. Hang on, the `beforeEach` statement is getting **HUGE!**
<figure>
![Mock profile service in before each](/assets/images/2014/11/Screen-Shot-2014-11-24-at-3-38-08-PM.png)
<figurecaption>Snippet 4e</figurecaption>
</figure>
<br/>

The service was mocked on lines 9-13. Also, note that the service was added to the controller on line 23.

Now `profileService` is defined and it a method. The test from Snippet 10 will pass.

---
###5. Local Storage
Did you notice that the last function has a reference to local storage? How do we test that? Since we're not actually calling the `profileService.getProfile` method in our mock controller, it won't set local storage, so let's practice a different way:
<figure>
![Set profile function](/assets/images/2014/11/Screen-Shot-2014-11-24-at-4-07-41-PM.png)
<figurecaption>Snippet 5a</figurecaption>
</figure>
<br/>
Luckily, we were smart and totally already injected the localStorageService in our `beforeEach` statement at the start of this mess. If you didn't, look at lines 7 and 17 in snippet 4e above.

Testing is relatively straightforward; use the `localStorageService.get` method to see if you successfully set what you wanted.
<figure>
![Local storage test](/assets/images/2014/11/Screen-Shot-2014-11-24-at-4-10-20-PM-1.png)
<figurecaption>Snippet 5b</figurecaption>
</figure>
<br/>

Watch out! The number for age was stringified in local storage and `.toBe()` is equivalent to `===`.

---

###6. Random Extra
One of my functions uses `$ionicListDelegate`. Not surprisingly, it has some built-in Ionic functionality regarding creating lists of information.

Here's one of my controller functions which makes use of it:
<figure>
![closeItemModal](/assets/images/2014/11/Screen-Shot-2014-11-24-at-4-14-19-PM.png)
<figurecaption>Snippet 6a</figurecaption>
</figure>
<br/>

*Oh God, another modal!* 

That's old news. Refer to section 4.

This time, we don't need to mock the delegate or create a fake `.closeOptionButtons` method, as long as your remembered to inject `$ionicListDelegate` in the `beforeEach` statement. 

See the theme yet?
<figure>
<a href="https://imgflip.com/i/ejh9f"><img src="https://i.imgflip.com/ejh9f.jpg" title="made at imgflip.com"/></a>
</figure>
<br/>

Forgot? Trudge on up to Snippet 4e to look at lines 7 and 18.

Here's your test:
<figure>
![Test for ionic list delegate](/assets/images/2014/11/Screen-Shot-2014-11-24-at-4-22-05-PM.png)
<figurecaption>Snippet 6b</figurecaption>
</figure>
<br/>

---
###Summary
If you want lots of examples, to [Team endevr's](https://github.com/endevr-) Ionic GitHub [repo](https://github.com/endevr-/endevr/tree/master/app/www/test). 

(You can also copy any paste from there.)

Remember:
Angular is needy. 
Give it what it wants.
When in doubt, fake stuff.
Lastly, "[Never give up, never surrender](https://www.youtube.com/watch?v=9fdcIwHKd_s)."

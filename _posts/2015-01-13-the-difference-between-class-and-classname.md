---
layout: post
class: 'post-template'
subclass: 'post'
title: "The Difference Between Class and ClassName"
date: 2015-01-13 23:25:44 +0000
slug: "the-difference-between-class-and-classname"
description: "Class is an attribute. ClassName is a method to get the value of that attribute. But, there's more..."
ghost_id: 30
ghost_uuid: "fb2debca-e95c-4056-8c06-a49dd3f8910a"
---

#Question
From Stack Overflow:

![Question asking the difference between class and class name](/assets/images/2015/01/Screen-Shot-2015-01-06-at-5-02-37-PM.png)


#Answer(s)
Let's break this into answerable parts:

#####Q1:

>What is the difference between class and classname in javascript?

The title question.

####A1: Attribute v. Property

Class is an attribute in an html element `<span class='classy'></span>`

While, on the other hand, `.className` is a property that can by called on an element to get/set its class.

    var element = document.createElement('span');
    element.className = 'classy'
    // element is <span class='classy'></span>

Setting the class can also be accomplished with `.setAttribute('class', 'classy')`. We manipulate classes so often, however, that it merited its own `.className` method.

---
####Q2:

>However when I replace className above by class in the function above, the code doesn't work. So I am naturally wondering what the difference is between class and className.

####A2: element.class is not a property.

Class may be an attribute of an element, but you can't call it like `el.class`. The way you do it is by `el.className`, like the original question had already figured out. If you look at the [MDN for Element](https://developer.mozilla.org/en-US/docs/Web/API/Element.className), you'll see that elements have many properties and methods, but `.class` isn't one.

![Screenshot of MDN element properties class name](/assets/images/2015/01/0qrFD.png)

---

####Q3:

>Also what's the best way to return a list of children of a particular class name for a generic object?

####A3: Use .getElementsByClassName

Rather than using a purpose-made function, people frequently "chain" methods one-after-another to achieve the desired end-effect.

Based on the question's needs, I think he's asking for the `.getElementsByClassName` method. Here are the [full docs](https://developer.mozilla.org/en-US/docs/Web/API/Element.getElementsByClassName) and an excerpt:

>The Element.getElementsByClassName() method returns returns a live HTMLCollection [array] containing all child elements which have all of the given class names.

To reuse the example from the question:

    var li = document.createElement('li');
    var input = document.createElement('input');
    input.setAttribute('class','answer_input');
    li.appendChild(input);
    console.log(li.getElementsByClassName("answer_input")[0]);
    // would return the <input class='answer_input'> as the first element of the HTML array

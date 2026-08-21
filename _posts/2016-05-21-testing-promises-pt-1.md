---
layout: post
class: 'post-template'
subclass: 'post'
title: "Part 1: Wait for It...Unit Testing Sever-Side Promises"
date: 2016-05-21 04:46:32 +0000
slug: "testing-promises-pt-1"
description: "The short answer for how to construct asynchronous unit tests: fake a lot of stuff."
meta_title: "Testing Server-Side Promises, Part 1"
ghost_id: 60
ghost_uuid: "a1bf8e50-a6ac-468d-bad3-1d020817bb5e"
---

*This is the first installment of a four-part series. Find more advanced tests:*

- [Part 2: Easy](http://adam-back.azurewebsites.net/testing-promises-pt-2/)

Unit testing asynchronous code requires a lot of setup because we don't want anything to actually hit our databases. How do we keep unit tests from becoming integration tests? The short answer: fake a lot of stuff.

Fake sounds bad, so everyone calls it a *mock*. Frameworks like [AngularJS](https://docs.angularjs.org/api/ngMock/service/$httpBackend) provide synchronous mocks as part of their testing suite. [Sinon](http://sinonjs.org/docs/) exists as a library to provide this functionality as well, although they call them *stubs*.

Existing examples online almost always use `setTimeout` to fake asynchronicity. That's not real life. Real life is querying your database. Real life is calling another microservice or external API. Real life is chaining multiple promises together. How do we test when life gets complicated?

Wait for it...

####Setup
First of all, I'm talking about testing Node.js functions. Sure, you can have asynchronous calls on the client (AJAX), but almost everything on the server is asynchronous by comparison.

I frequently use a grunt module called [grunt-jasmine-node-coverage](https://github.com/jribble/grunt-jasmine-node-coverage) because it does everything I need at once. The only downside: it's currently using Jasmine 1.3, the oldest supported version. The main differences between old and new versions are syntactical:

    // Jasmine 1.3, what we're using
    spyOn( obj, 'method' ).andReturn( something );
    
    // Jasmine 2.0
    spyOn( obj, 'method' ).and.returnValue( something );
    
We'll have two files: `userHelpers.js` and its tests `userHelper.spec.js`.

Here's what we start with in `userHelpers.js`:
```
var user = require( './models' ).user;

exports.getAllUsers = function() {
  return users.findAll();
};
```

This is pretty [common syntax](http://sequelize.readthedocs.io/en/latest/docs/models-usage/#findall-search-for-multiple-elements-in-the-database) for database ORMs like [Sequelize](http://sequelize.readthedocs.io/en/latest/) and [Bookshelf.js](http://bookshelfjs.org/). We require the model which has a slew of helper functions to abstract away SQL statements. Functions like `findAll` already returns promises.

Here is the basic setup for our tests:
```
// require the fns you want to test
var helpers = require( './userHelpers' );

describe('getAllUsers', function() {
  var getAllUsers = helpers.getAllUsers;
  
  it('should be defined as a function', function() {
    expect( typeof getAllUsers ).toBe( 'function' );
  });
});
```

The first test reads "getAllUsers should be defined as  a function" and serves as a quick check to make sure everything's been set up correctly. Testing configuration is another (long) blog post.
    
#### Basic Example
This may be a basic example, but it provides a lot of needed background.

Ask yourself: what does our function `getAllUsers` return?

If you thought, "Well, it returns all the users in the database," you'll be right eventually, but not now.

The truth is, this function returns a promise. The promise will *eventually* give you the users.

Here are our goals for testing this function:

1. Prevent `findAll` from hitting the database
1. `getAllUsers` should return a promise
1. `findAll` should get called
1. When `getAllUsers` is successful, it should return a list of users
1. When it fails, it should propagate the error

**Goal 1**: Here's where we start mocking things. To prevent the function from calling the database, we'll need to `spyOn` it. Jasmine creates a fake, blank function which matches its target, so that you have complete control. Now `user.findAll` only does what you tell it to. Goal 1 complete.

Notice I've required the `user` object at this point. You'll almost always need all the same require statements in your tests which you use in your original function.

```
var helpers = require( './userHelpers' );
var user = require( './models' ).user;

describe('getAllUsers', function() {
  var getAllUsers = helpers.getAllUsers;
	
  spyOn( user, 'findAll' );
  
  it('should be defined as a function', function() {
    expect( typeof getAllUsers ).toBe( 'function' );
  });
});
```

**Goal 2:** Write a test which tests the output of the function (a promise). 

In order to do this, we'll need a promise library like [q](https://github.com/kriskowal/q/) or [Bluebird](https://github.com/petkaantonov/bluebird). I like q for its simplicity here.

```
var helpers = require( './userHelpers' );
var user = require( './models' ).user;
var Q = require( 'q' );

describe('getAllUsers', function() {
  var getAllUsers = helpers.getAllUsers;
  var fakePromise = Q.defer(); // 1
  spyOn( user, 'findAll' ).andReturn( fakePromise.promise ); // 2
  
  it('should be defined as a function', function() {
    expect( typeof getAllUsers ).toBe( 'function' );
  });
  
  it('should return a promise', function() {
    var result = getAllUsers();
    expect( Q.isPromise( result ) ).toBe( true ); // 3
  });
});
```

We generate our own promise (1) using [q's API](https://github.com/kriskowal/q/wiki/API-Reference#promise-creation). When our fake `user.findAll` gets called, we still want it to return a promise, just *our* promise (2). We use a q helper function to check the validity of the returned promise (3).

**Goal 3:** `findAll` should be called. 

We can reuse a lot code, just add another test, and use Jasmine's built-in spy helpers.

```
  expect( Q.isPromise( result ) ).toBe( true );
});

it('should call user.findAll', function() {
  getAllUsers();
  expect( user.findAll ).toHaveBeenCalled();
  expect( user.findAll ).toHaveBeenCalledWith(); // 1
});
```

I want to really lock-down the `findAll` call, making sure we're not passing any parameters (1).

**Goal 4:** When `getAllUsers` is successful, it should return a list of users. 

Before we go on, we should do some refactoring to keep our code DRY. Every new test ('it'), we should be returning a new promise, never touched before; this is a good use-case for Jasmine's `beforeEach` block.

```
var helpers = require( './userHelpers' );
var user = require( './models' ).user;
var Q = require( 'q' );

describe('getAllUsers', function() {
  var getAllUsers = helpers.getAllUsers;
  var fakePromise; // 1
  
  beforeEach(function() {
    fakePromise = Q.defer();
    spyOn( user, 'findAll' ).andReturn( fakePromise.promise );
  });
  
  it('should be defined as a function', function() {
    expect( typeof getAllUsers ).toBe( 'function' );
  });
  
  it('should return a promise', function() {
    var result = getAllUsers();
    expect( Q.isPromise( result ) ).toBe( true );
  });
  
  it('should call user.findAll', function() {
    getAllUsers();
    expect( user.findAll ).toHaveBeenCalled();
    expect( user.findAll ).toHaveBeenCalledWith();
  });
});
```

<u>Take note!</u> The variable declaration for the `fakePromise` is outside of the `beforeEach` function scope so that the individual tests have access to it (1).

This is where the testing gets interesting in my opinion. We get to fake a successful resolution of our promise.
```
it('should resolve an array of users', function( done ) {
  var listOfUsers = [ { id: 1 }, { id: 2 } ];
  fakePromise.resolve( listOfUsers ); // 1
  
  getAllUsers()
  .then(function( result ) {
    // 2
    expect( Array.isArray( result ) ).toBe( true );
    expect( result.length ).toBe( 2 );
    expect( result ).toEqual( listOfUsers );
    done(); // 3
  })
  .catch(function( error ) {
    expect( error ).not.toBeDefined(); // 4
    done();
  });
});
```

Create a set of fake values whicb more-or-less approximates what you would expect to get in return from a real function call. q's promises have a few methods, `resolve` being the signal for success (1)! We've resolve the promise before we even call the function...this helps our code run pseudo-synchronously; as soon as the function is called, it will resolve.

We expect to finish in the `.then` block (2). We can check the result just as if we were testing synchronous code. Notice the addition of the done function (3). If you look in the callback at the top of the 'it' statement, I passed `done` as a parameter. Invoke this function whenever your asynchronous test is done to avoid making Jasmine time out (hang).

In the unfortunate even that your code is changed and the test fails, you should add a `.catch` block. An error will propagate and throw the test into a tizzy, rather than just failing silently or hanging (4). Don't forget to call `done()` here too.

**Goal 5:** When it fails, it should propagate the error. 

This should be tested explicitly and will look very similar to the previous test.

```
it('should propagate an error', function( done ) {
  var testError = new Error( 'Test' ); 
  fakePromise.reject( testError ); // 1
  
  getAllUsers()
  .then(function( result ) {
    expect( result ).not.toBeDefined(); // 2
    done();
  })
  .catch(function( error ) {
    expect( error ).toEqual( testError ); // 3
    done();
  });
});
```

Instead of resolving the promise, we will reject it with a real error (1). As long as you don't use the `throw` keyword, the test will continue. This time we expect not to reach the `.then` block, but we have a failsafe, just in case we do (2). In the `.catch`, ensure the correct error was passed along without alteration (3).

#### Finished Suite
```
var helpers = require( './userHelpers' );
var user = require( './models' ).user;
var Q = require( 'q' );

describe('getAllUsers', function() {
  var getAllUsers = helpers.getAllUsers;
  var fakePromise;
  
  beforeEach(function() {
    fakePromise = Q.defer();
    spyOn( user, 'findAll' ).andReturn( fakePromise.promise );
  });
  
  it('should be defined as a function', function() {
    expect( typeof getAllUsers ).toBe( 'function' );
  });
  
  it('should return a promise', function() {
    var result = getAllUsers();
    expect( Q.isPromise( result ) ).toBe( true );
  });
  
  it('should call user.findAll', function() {
    getAllUsers();
    expect( user.findAll ).toHaveBeenCalled();
    expect( user.findAll ).toHaveBeenCalledWith();
  });
  
  it('should resolve an array of users', function( done ) {
    var listOfUsers = [ { id: 1 }, { id: 2 } ];
    fakePromise.resolve( listOfUsers );
  
    getAllUsers()
    .then(function( result ) {
      expect( Array.isArray( result ) ).toBe( true );
      expect( result.length ).toBe( 2 );
      expect( result ).toEqual( listOfUsers );
      done();
    })
    .catch(function( error ) {
      expect( error ).not.toBeDefined();
      done();
    });
  });
  
  it('should propagate an error', function( done ) {
    var testError = new Error( 'Test' ); 
    fakePromise.reject( testError );
  
    getAllUsers()
    .then(function( result ) {
      expect( result ).not.toBeDefined();
      done();
    })
    .catch(function( error ) {
      expect( error ).toEqual( testError );
      done();
    });
  });
});
```

#### Summary and Final Tips
Testing asynchronous code requires some additional setup and mocking so that unit tests don't reach out to the database or other APIs (integration). Control is key. Fake promises by creating them manually so you have the choice to resolve or reject them.

Some tips:

* If your tests timeout (>5000ms Jasmine), did you remember the `done` callback?
* It's not enough just to `spyOn` a function, you have to mock the output with `.andReturn( fake.promise )`.
* If the promise you created is `undefined` in each test, check that you declared the variable in the correct scope.
* If your tests fail silently, don't forget to provide a failsafe `.then` or `.catch` block.
* Remember to `require` all of your libraries and objects in the testing file.

Move beyond the basic tests in [part 2](http://adam-back.azurewebsites.net/testing-promises-pt-2/)!

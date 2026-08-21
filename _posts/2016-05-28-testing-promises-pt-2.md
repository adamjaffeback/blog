---
layout: post
class: 'post-template'
subclass: 'post'
title: "Part 2: Wait for It...Unit Testing Sever-Side Promises"
date: 2016-05-28 02:44:18 +0000
slug: "testing-promises-pt-2"
description: "Test functions using Q.all by resolving and rejecting multiple promises in particular order."
meta_title: "Testing Server-Side Promises, Part 2"
ghost_id: 62
ghost_uuid: "eb06c739-e266-4d4c-9996-c6dacace18dd"
---

*This is the second installment of a four-part series. [Click here](http://adam-back.azurewebsites.net/testing-promises-pt-1/) to explore the basics in part one.*

#### Setup
We'll use the same promise-based function twice to call an external API with two different inputs. In this case, the [API will return 1) the current weather for a location and 2) the five day forecast.](http://openweathermap.org/api)

Here's what we start with in weatherReport.js:
```
var request = require( 'request' );
var Q = require( 'q' );

// calls the external API
exports.getWeatherFromAPI = function( city, timePeriod ) {
  var deferred = Q.defer();

  request( 'api.openweathermap.org/data/2.5/' + timePeriod +'?q=' + city, function( error, response, body ) {
    if ( !error && response.statusCode == 200 ) {
      deferred.resolve( body );
    } else {
      deferred.reject( error );
    }
  });
  
  return deferred.promise;
};

// uses the helper above to get current and future weather data
exports.generateWeatherReport = function( cityName ) {
  var promises = [];
  promises.push( exports.getWeatherFromAPI( cityName, 'weather' ) );
  promises.push( exports.getWeatherFromAPI( cityName, 'forecast' ) );
  return Q.all( promises );
};
```

The Request module is difficult, because it isn't doesn't match Node.js patterns exactly and, therefore, isn't a great candidate for [`Q.denodeify`](https://github.com/kriskowal/q/wiki/API-Reference#qnfbindnodefunc-args) or the like. For readability, in the absense of Request generating its *own* promise, I like using the Q API to explicitly generate my own promise; I find that this also makes the testing more logical.

The testing file will need Q. We're just going to test `generateWeatherReport`, because there's some additional complexity when testing functions which include the Request module:
```
var Q = require( 'q' );
var weather = require( './weatherReports.js' );

describe('generateWeatherReport', function() {
  var generateWeatherReport = weather.generateWeatherReport;

  it('should be defined as a function', function() {
    expect( typeof generateWeatherReport ).toBe( 'function' );
  });

  it('should return a promise', function() {
    var result = generateWeatherReport();
    expect( Q.isPromise( result ) ).toBe( true );
  });
});
```

#### Easy Example
We've already written the basic tests above. Make sure the function is defined and it returns a promise.

Here are some additional goals for testing this function:

1. Prevent the `getWeatherFromAPI` from contacting the internet
1. Check that `getWeatherFromAPI` was called
  - Confirm it was called twice
  - Check the parameters for each of those calls
1. When `generateWeatherReport` is successful, it should return an array of weather data
1. When it fails, it should propagate the error

**Goal 1**: Keep this unit test from becoming an integration test. Start the mock: `spyOn` will completely replace the functionality of `getWeatherFromAPI` and do whatever we tell it. HINT: we're NOT going to tell it to call the internet.

```
var Q = require( 'q' );
var weather = require( './weatherReports.js' );

describe('generateWeatherReport', function() {
  var generateWeatherReport = weather.generateWeatherReport;
  var currentWeather, forecastWeather;
  
  beforeEach(function() {
    currentWeather = Q.defer();
    forecastWeather = Q.defer();
    spyOn( weather, 'getWeatherFromAPI').andCallFake(function( city, type ) {
      if ( type === 'weather' ) {
        return currentWeather.promise;
      } else {
        return forcastWeather.promise;
      }
    });
  });
});
```

In a simple example when you're only going to call the same function once, I'd use `.andReturn( promise )`, but in this case, we want to return a different promise for each call.

Now, when `getWeatherFromAPI` gets called, it doesn't call the written code, it calls our fake anonymous function.

**Goal 2**: Confirm `getWeatherFromAPI` was called.

```
it('should call getWeatherFromAPI', function( done ) {
  currentWeather.reject( new Error( 'Test' ) ); // 1

  generateWeatherReport( 'San Francisco' )
  .then(function( value ) {
    expect( value ).not.toBeDefined();
    done();
  })
  .catch(function( error ) {
    expect( weather.getWeatherFromAPI ).toHaveBeenCalled(); // 2
    expect( error.message ).toBe( 'Test' );
    done();
  });
});
```

First, we reject the future call to the API (1). When we invoke `generateWeatherReport`, it should end in the catch block; don't forget to put a `.then` statement, just in case it doesn't. We can use Jasmine's built-in `toHaveBeenCalled()` to check that `getWeatherFromAPI` was called. 

To be more specific, however, we should ensure that the function gets called twice and we should check the parameters. Here's the refactored test to do just that:

```
it('should call getWeatherFromAPI', function( done ) {
  currentWeather.resolve( true ); // 1
  forecastWeather.reject( new Error( 'Test' ) );

  generateWeatherReport( 'San Francisco' )
  .then(function( value ) {
    expect( value ).not.toBeDefined();
    done();
  })
  .catch(function( error ) {
    expect( weather.getWeatherFromAPI.calls.length ).toBe( 2 ); // 2
    expect( weather.getWeatherFromAPI.calls[ 0 ].args[ 0 ] ).toBe( 'San Francisco' );
    expect( weather.getWeatherFromAPI.calls[ 0 ].args[ 1 ] ).toBe( 'weather' );
    expect( weather.getWeatherFromAPI.calls[ 1 ].args[ 0 ] ).toBe( 'San Francisco' );
    expect( weather.getWeatherFromAPI.calls[ 1 ].args[ 1 ] ).toBe( 'forecast' );
    expect( error.message ).toBe( 'Test' );
    done();
  });
});
```

It's important to allow the first promise to pass (1). If you fail it, there's no guarantee it will coninute to the second promise, which is what we want to test. 

The `spyOn` API with `toHaveBeenCalled` and `toHaveBeenCalledWith` is great when the spy is only being called once (2). You can drill down into the raw data of a spy by checking the `.calls` array. Each `.calls[ i ]` also has `.args`.

**Goal 3**: Test `generateWeatherReport`'s success case. Easy: resolve both of the calls to the external API.

```
it('should resolve an array of weather data', function( done ) {
  currentWeather.resolve( '1' ); // 1
  forecastWeather.resolve( '2' );

  generateWeatherReport( 'San Francisco' )
  .then(function( value ) {
    expect( Array.isArray( value ) ).toBe( true );
    expect( value ).toEqual( [ '1', '2' ] ); // 2
    done();
  })
  .catch(function( error ) {
    expect( error ).not.toBeDefined();
    done();
  });
});
```

Both promises to the API are resolved (1). Also, notice that I feed back fake data. There's some debate about this practice; it boils down to two options:

1. Return an exact replica of the data you expect. 
1. Return token, easily testable data.

In this case, there's no manipulation of the data before resolving it; I don't see the ROI on spending time (or space) to represent the data with fidelity in the test.

Since `Q.all()` takes an array of promises as a parameter, it returns an array of values when those promises resolve (2).

**Goal 3.5** Spread your wings--there's a second way to write the test above with the [`Q.spread` method](https://github.com/kriskowal/q/wiki/API-Reference#promisespreadonfulfilled-onrejected). It takes an array of resolved values and spreads them across multiple parameters in the callback.

So instead of
```
generateWeatherReport( 'San Francisco' )
.then(function( value ) {
  expect( Array.isArray( value ) ).toBe( true );
  expect( value ).toEqual( [ '1', '2' ] );
```

you get this:
```
generateWeatherReport( 'San Francisco' )
.spread(function( currentData, forecastData ) {
  expect( currentData ).toBe( '1' );
  expect( forecastData ).toBe( '2' );
```

I think `.spread` is most useful when you're going to be manipulating data sets which are dissimilar. For example, the current weather won't have a high and low...it will have a current temperature for right now. In contrast, `forecastData` will probably be an array of five days. Using `.spread` also makes the code more readable.

**Goal 4**: Propagate errors. Honestly, I do generally write an explicit test for this, even though I've tested the `.catch` block throroughly in test 2 (when we rejected the promises to exit early).

#### Finished Suite
```
var Q = require( 'q' );
var weather = require( './weatherReports.js' );

describe('generateWeatherReport', function() {
  var generateWeatherReport = weather.generateWeatherReport;
  var currentWeather, forecastWeather;

  beforeEach(function() {
    currentWeather = Q.defer();
    forecastWeather = Q.defer();
    spyOn( weather, 'getWeatherFromAPI').andCallFake(function( city, type ) {
      if ( type === 'weather' ) {
          return currentWeather.promise;
        } else {
          return forcastWeather.promise;
        }
    });
  });

  it('should be defined as a function', function() {
    expect( typeof generateWeatherReport ).toBe( 'function' );
  });

  it('should return a promise', function() {
    var result = generateWeatherReport();
    expect( Q.isPromise( result ) ).toBe( true );
  });

  it('should call getWeatherFromAPI', function( done ) {
    currentWeather.resolve( true );
    forecastWeather.reject( new Error( 'Test' ) );

    generateWeatherReport( 'San Francisco' )
    .then(function( value ) {
      expect( value ).not.toBeDefined();
      done();
    })
    .catch(function( error ) {
      expect( weather.getWeatherFromAPI.calls.length ).toBe( 2 );
      expect( weather.getWeatherFromAPI.calls[ 0 ].args[ 0 ] ).toBe( 'San Francisco' );
      expect( weather.getWeatherFromAPI.calls[ 0 ].args[ 1 ] ).toBe( 'weather' );
      expect( weather.getWeatherFromAPI.calls[ 1 ].args[ 0 ] ).toBe( 'San Francisco' );
      expect( weather.getWeatherFromAPI.calls[ 1 ].args[ 1 ] ).toBe( 'forecast' );
      expect( error.message ).toBe( 'Test' );
      done();
    });
  });

  it('should resolve an array of weather data', function( done ) {
    currentWeather.resolve( '1' );
    forecastWeather.resolve( '2' );

    generateWeatherReport( 'San Francisco' )
    .then(function( value ) {
      expect( Array.isArray( value ) ).toBe( true );
      expect( value ).toEqual( [ '1', '2' ] );
      done();
    })
    .catch(function( error ) {
      expect( error ).not.toBeDefined();
      done();
    });
  });

  it('should catch an error', function( done ) {
    currentWeather.reject( new Error( 'Test' ) );

    generateWeatherReport( 'San Francisco' )
    .then(function( value ) {
      expect( value ).not.toBeDefined();
      done();
    })
    .catch(function( error ) {
      expect( error.message ).toBe( 'Test' );
      done();
    });
  });
});
```

#### Summary and Final Tips
It can be difficult to test when the same function gets called multiple times. Rather than returning the same promise for multiple calls, you have to differentiate using `.andCallFake` instead of `andReturn`. Normally, `toHaveBeenCalled` is very helpful, but not when you're invoking the same promise-based helper method multiple times.

Some tips:

* `Q.spread` is an easy substitute for `Q.then`; it provides more clarity about what data being returned.
* Sometimes you have to resolve every promise except the last one to ensure the internal function gets called enough times.
* The `calls` key on the `spyOn` is critical for accessing complex and multiple calls to the same spy.


Part 3 next week! On to medium difficulty!

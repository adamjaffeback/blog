---
layout: post
class: 'post-template'
subclass: 'post'
title: "Accidentally Deleting Your Angular App Is Easier Than You Think"
date: 2015-06-24 01:30:44 +0000
slug: "accidentally-deleting-your-angular-app-is-easier-than-you-think"
ghost_id: 54
ghost_uuid: "89035420-54e4-4b8d-81d4-b747dc6f6510"
---

##Good News
Well, not the whole app and not forever. That's the good news. 

The bad news: it's an easy, simple, easily missable mistake.

For some context, I started an Ionic app which has all of the controllers in the same `controller.js` file. I started by refactoring the three controllers into their own files.

Here's the offender, `controllers.js`:
    
    angular.module('starter.controllers', [])
    .controller('AppCtrl', function($scope, $ionicModal, $timeout) {
  
  	// Form data for the login modal
  	$scope.loginData = {};

  	// Open the login modal
  	$scope.login = function() {
    	$scope.modal.show();
  	};
	})
	.controller('PlaylistsCtrl', function($scope) {
 	 $scope.playlists = [];
	})
	.controller('PlaylistCtrl', function($scope, $stateParams) {
	});

##Spot the Mistake
After my refactor, here's `AppCtrl.js`:

 	angular.module('starter.controllers', [])
    	.controller('AppCtrl', function($scope, $ionicModal, $timeout) {
  
  		// Form data for the login modal
  		$scope.loginData = {};

	  	// Open the login modal
  		$scope.login = function() {
    		$scope.modal.show();
  		};
	})
And `PlaylistsCtrl.js`:

	angular.module('starter.controllers', [])
	.controller('PlaylistsCtrl', function($scope) {
 		$scope.playlists = [];
	})
    
Each file has been added to `index.html`, but only the last one will load. 

Ponder, but don't rip you hair out.

##Simple Fix
This creates a module:
`angular.module('starter.controllers', [])`

This accesses a module which has already been created:
`angular.module('starter.controllers')`

So, each time I called `angular.module('starter.controllers', [])`, it would create the module, then wipe it clean to start a brand new one for each successive file. Hence, only the last file in index.html would be accessible to the app.

![Head Bang Kit](https://s-media-cache-ak0.pinimg.com/736x/88/4f/f1/884ff1733dad77bb140db9dbf2917658.jpg)

# twork

**twork** is a **T**ornado Application Frame**Work**, it supports business module injection, the module called TworkApp.

## Features

### Web App Framework

+ Control(WebApplication)/Model(RequestHandler) separation, users simply writing Handler Model
+ Web RequestHandler should be Inherited from twork.web.action.base.BaseHandler

### Unified Infrastructure

+ Web access logging
+ Status statistics
+ Overload protection
+ IP checking
+ Others

### Open Design

+ Not only for web application framework
+ Can be directly embedded other control model, like that the custom protol server-app
+ Custom Logging Support

### Scaffold Support

+ Build your own Tornado Application
+ As a app module injected to twork

### Easy Maintainable

+ Script Tools: log cut, log reopen, tworkd kill and others
+ Consistent process name: twork::$APP/$VERSION

## Easy To Use

### Environment

**virtualenv** is recommend.

+ [virtualenv](http://www.virtualenv.org/en/latest/) is a tool to create
  isolated Python environments
+ Initialize and enter the app virtualenv
+ For example, creating the **hello** application here

### Install twork

+ pip install [twork](https://pypi.python.org/pypi/twork)
+ easy_install [twork](https://pypi.python.org/simple/twork/)

### TworkApp Build

Create your own tornado application based on twork.

+ twork-admin -app=hello -prefix=~/workspace
+ cd ~/workspace

#### Web Handler(Optional)
+ write your web request handler in hello/hello/web/action directory, the handler should be Inherited from twork.web.action.base.BaseHandler
+ add uri:handler map to HANDLERS in hello/hello/app.py

### Run TworkApp with tworkd
 
+ make install
+ tworkd --app_module=hello.twork_injection

### Check the web server

+ http://localhost:8000/v1.0/hello/stats
+ http://localhost:8000/v1.0/twork/stats

## Requirements
The following libraries are required

+ tornado==2.4.1
+ setproctitle==1.1.8
+ nose==1.3.3

## Issues

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)

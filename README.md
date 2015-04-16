# twork

[![Join the chat at https://gitter.im/bufferx/twork](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/bufferx/twork?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Pypi package](https://badge.fury.io/py/twork.png)](http://badge.fury.io/py/twork) [![Pypi downloads](https://pypip.in/d/twork/badge.png)](https://crate.io/packages/twork?version=latest)

**twork** is a Tornado Application FrameWork, it supports plug-in module injection, the module called TworkApp.

## Features

### Plug-in

+ TworkApp as a plug-in injected to Twork

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
+ Can be directly embedded other control model, like that the custom protcol server-app
+ Custom Logging Support

### Scaffold Support

+ Build your own Tornado Application
+ As a app module injected to twork

### Easy Maintainable

+ Script Tools: log cut, log reopen, tworkd kill and others
+ Consistent process name: twork::hello/1.0.0.0

## Usage

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

### Run TworkApp within twork
 
+ make install
+ tworkd -app_module=hello.twork_injection OR tworkd -config_file=conf/twork.conf

### Access the web server

+ http://localhost:8000/v1.0/hello/stats
+ http://localhost:8000/v1.0/twork/stats

### Check Htpp Response
+ Server: TWS/2.0.0.5
+ TworkApp: HELLO/1.0.0.0

## Requirements
The following libraries are required

+ tornado==2.4.1
+ setproctitle==1.1.8
+ nose==1.3.3

## Issues

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)

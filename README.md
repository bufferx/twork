# twork

**twork** is a server-app framework based on **tornado**

## Features

### Web App Framework

Control/Model separation, users simply writing Application Model

### Unified Infrastructure

access logging, status statistics, overload protection, IP checking and so on

### Open Design

Not only for web framework, can be directly embedded other control model, like
that the custom protocol server-app.

## Install

+ pip install [twork](https://pypi.python.org/pypi/twork)
+ easy_install [twork](https://pypi.python.org/pypi/twork)

## TworkApp Builder
Create your own project based on twork, **virtualenv** is recommend.

+ twork-admin -app=$APP -prefix=~/workspace
+ write your web request handler in $APP/$APP/web/action, and should be Inherited
  from twork.web.action.BaseHandler

### Environment
+ [virtualenv](http://www.virtualenv.org/en/latest/) is a tool to create
  isolated Python environments

## Usage
Enter your virtualenv first
 
+ cd ~/workspace/$APP
+ make install
+ tworkd --app_module=$APP.twork_injection

## Case
Check the web server

+ http://localhost:8000/v1.0/twork/stats

## Requirements
The following libraries are required

+ tornado==2.4.1
+ setproctitle==1.1.8
+ nose==1.3.3

## Issues

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)

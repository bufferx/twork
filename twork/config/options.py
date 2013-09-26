# -*- coding: utf-8 -*-
#
# Copyright 2012 Zhang ZY<http://idupx.blogspot.com/> 
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

'''
@feature: Config Options
'''

import sys
import os

import assembly

import pyutil.lib.tornado as tornado
from pyutil.lib.tornado.options import define, options

DEFAULT_OPTIONS_PORT              = 8000 
DEFAULT_OPTIONS_LOG_ROOT_PATH     = \
    os.path.realpath(os.path.join(assembly.PROJECT_PATH, 'log'))

def define_options():
    # 日志
    define("log_level", default = 'DEBUG', 
            help = "Set Log Level")

    define('log_root_path', default = DEFAULT_OPTIONS_LOG_ROOT_PATH, 
            help = 'Log file stored root path')

    define("app_name", default = 'twork',
            help = "Set Log Level")

    define("v", default = False,
            help = "verbose, print debug info", type = bool)

    define("bind_ip", default = '0.0.0.0',
            help = "Run server on a specific IP")

    define("port", default = DEFAULT_OPTIONS_PORT,
            help = "Run server on a specific port", type = int)

    define("backlog", default = 128,
            help = "the same meaning as for socket.listen", type = int)

    define("env", default="dev", help="service run environment")
    
    define("timer_interval", default = 30,
            help = "Timer Interval, TimeUnit: seconds", type = int)
    
    define("config", default = '%s/etc/twork.conf' % assembly.PROJECT_PATH,
            help = "Configuration file specifying options")

def _usage():
    print 'Usage: ./service -log_root_path=SpecifiedFile -port=SpecifiedPort'
    sys.exit()

def _check_dir_tail(dir_name):
    if not dir_name or '' == dir_name:
        return dir_name
    _len = len(dir_name) - 1
    if '/' == dir_name[_len:]:
        dir_name = dir_name[0:_len]

    return dir_name

def _mkdir(file_dir):
    real_path = os.path.realpath(file_dir)
    if not os.path.exists(real_path):
        os.makedirs(real_path)
        pass

def init_options():
    define_options()
    # maybe some options will be use before load config file
    tornado.options.parse_command_line()
    if os.path.exists(options.config):
        tornado.options.parse_config_file(options.config)
    if not options.log_root_path or not options.port:
        _usage()
    options.log_root_path = _check_dir_tail(options.log_root_path)
    options.log_path = '%s/%d' % (options.log_root_path, options.port)
    _mkdir(options.log_path)

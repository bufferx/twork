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

'''feature: Config Options
'''

import os

import assembly

import bf4x_pyutil.lib.tornado as tornado
from bf4x_pyutil.lib.tornado.options import define, options

DEFAULT_OPTIONS_LOG_ROOT_PATH     = \
    os.path.realpath(os.path.join(assembly.PROJECT_PATH, 'log'))

def define_options():
    define("app_name", default = 'twork',
            help = "Set Log Level")

    define("app_version", default = '',
            help = "The Application version")

    define("log_level", default = 'DEBUG',
            help = "Set Log Level")

    define('deploy_path', default = DEFAULT_OPTIONS_LOG_ROOT_PATH,
            help = 'Log file stored root path')

    define("config_file", default = '%s/etc/twork.conf' % assembly.PROJECT_PATH,
            help = "Configuration file specifying options")

def _usage():
    print 'Usage: ./service -deploy_path=SpecifiedFile -port=SpecifiedPort'
    os._exit(0)

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
    if os.path.exists(options.config_file):
        tornado.options.parse_config_file(options.config_file)
    if not options.deploy_path or not options.port:
        _usage()
    options.deploy_path = _check_dir_tail(options.deploy_path)
    options.log_path = '%s/log/%d' % (options.deploy_path, options.port)
    _mkdir(options.log_path)

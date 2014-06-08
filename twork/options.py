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

import tornado
from tornado.options import define, options

from twork import assembly


define("config_file", default='%s/conf/twork.conf' % assembly.PROJECT_PATH,
        help = "Configuration File Specifying Options")
define("log_config", default='%s/conf/log.conf' % assembly.PROJECT_PATH,
        help = "Logging Config File Options")


def _usage():
    print 'Usage: ./service -log_root=SpecifiedFilePath -port=SpecifiedPort'
    os._exit(0)

def setup_options():
    # maybe some options will be use before load config file
    tornado.options.parse_command_line()

    if os.path.exists(options.config_file):
        tornado.options.parse_config_file(options.config_file)

    if not options.log_root:
        _usage()

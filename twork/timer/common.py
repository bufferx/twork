#!/usr/bin/env python
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

import functools
import time
import tornado.web

from util import options
from util import g_logger

class CommonTimer(object):
    '''Common Timer'''

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__scheduler = None

    def __callback(self, web_app):
        g_logger.debug('WEB_APPLICATION: %d', id(web_app))
    
    def start(self, web_app):
        assert options.timer_interval > 0

        if self.__scheduler is not None:
            return

        __callback = functools.partial(self.__callback, web_app)

        tornado.ioloop.IOLoop.instance().add_timeout(time.time(), __callback)

        self.__scheduler = \
            tornado.ioloop.PeriodicCallback(__callback,
                    options.timer_interval * 1000)
        self.__scheduler.start()
        pass

    def stop(self):
        if self.__scheduler is not None:
            self.__scheduler.stop()
        pass
    pass

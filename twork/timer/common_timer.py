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

from tornado.ioloop import PeriodicCallback
from tornado.options import define, options

from twork.util import g_logger

define("timer_interval", default = 30,
        help = "Timer Interval, TimeUnit: seconds", type = int)


class CommonTimer(object):
    '''Common Timer'''

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__scheduler = None

    def start(self, callback):
        assert options.timer_interval > 0

        if self.__scheduler is not None:
            return

        self.__scheduler = \
            PeriodicCallback(callback,
                    options.timer_interval * 1000)
        self.__scheduler.start()

    def stop(self):
        if self.__scheduler is not None:
            self.__scheduler.stop()

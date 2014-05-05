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
import logging
import time

logger = logging.getLogger('twork')

log_time = lambda f, t: 'Function[%s] Consume %.3fms' % (f, (time.time() - t) * 1000)


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        r = func(*args, **kwargs)
        logger.info('%s\t%s\t%s', args, kwargs,
                log_time(func.__name__, start_time),
                extra={'version': 'v1.0'})
        return r
    return wrapper


def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

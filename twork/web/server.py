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

''' tornado web application 
'''

import time

import tornado.httpserver
import tornado.web
from tornado.ioloop import IOLoop

import assembly

import action

from util import options
from util import g_logger

from timer.common import CommonTimer


class TApplication(tornado.web.Application):

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    @property
    def stat_info(self):
        fd_all = len(IOLoop.instance()._handlers)
        return {'fd': {'all': fd_all}, 'uptime': '%.3f' % (time.time() -
            self._start_time)}

    def __init__(self):
        debug = options.env == "debug"
        app_settings = { 
                'gzip': 'on',
                'static_path': assembly.STATIC_PATH,
                'debug':debug,
                }

        handlers = [
            (r'^/v1.0/twork/stat$', action.StatInfoHandler,
                {'version': (1, 0)}),
        ]

        self._start_time = time.time()
        
        tornado.web.Application.__init__(self, handlers, **app_settings)

class HTTPServer(object):

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def start(self):
        sockets_list = []
        for bind_ip in options.bind_ip.split(','):
            sockets = tornado.netutil.bind_sockets(options.port,
                    address=bind_ip,
                    backlog=options.backlog)
            sockets_list.append(sockets)

        CommonTimer.instance().start(TApplication.instance())

        self.http_server =  \
            tornado.httpserver.HTTPServer(xheaders=True,
                    request_callback=TApplication.instance())
        for sockets in sockets_list:
            self.http_server.add_sockets(sockets)

    def stop(self):
        CommonTimer.instance().stop()

        if hasattr(self, 'http_server'):
            self.http_server.stop()

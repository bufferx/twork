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

import tornado.web
import tornado.httpserver

import assembly

from domain.object.db import DB
from util import options
from util import g_logger
from timer.common import CommonTimer

import action

class TApplication(tornado.web.Application):

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = DB()
            if __debug__:
                g_logger.debug('initial application.db: %s', self._db)
            pass
        return self._db

    def __init__(self):
        debug = options.env == "debug"
        app_settings = { 
                'gzip': 'on',
                'static_path': assembly.STATIC_PATH,
                'debug':debug,
                }

        handlers = [
            # say hi 
            (r'/sayhi', action.HelloHandler, dict(_db=self.db)),
            (r'/asyncread', action.AsyncReadHandler, dict(_db=self.db)),
        ]
        
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

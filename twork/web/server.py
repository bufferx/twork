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

from hashlib import md5
import os
import time

import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.options import define, options
import tornado.web

from twork.web import action
from twork.web import assembly
from twork.util import g_logger
from twork.timer.common_timer import CommonTimer

define("bind_ip", default='0.0.0.0',
        help="run server on a specific ip")
define("port", default=8000,
        help="run server on a specific port", type=int)
define("backlog", default=128,
        help="the same meaning as for socket.listen", type=int)
define("env", default="debug", help="service run environment")


class TApplication(tornado.web.Application):

    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    @property
    def stat_info(self):
        def calcu():
            for handler, st in self._handler_st.iteritems():
                for method, _st in st.iteritems():
                    _st['rt_avg'] = _st['rt'] / _st['requests']
        calcu()
        fd_all = len(IOLoop.instance()._handlers)
        return {'fd': {'all': fd_all}, 'uptime': '%.3f' % (time.time() -
            self._start_time), 'handler': self._handler_st}

    def __init__(self):
        self.init_app_info()

        debug = options.env == "debug"
        app_settings = { 
                'gzip': 'on',
                'static_path': assembly.STATIC_PATH,
                'debug':debug,
                }
        handlers = [
            (r'^/v1.0/twork/stats$', action.StatInfoHandler,
                {'version': (1, 0)}),
        ]

        self._start_time = time.time()
        self._handler_st = {}
        
        tornado.web.Application.__init__(self, handlers, **app_settings)

        self.timer_callback()

    def timer_callback(self):
        g_logger.debug('WEB_APPLICATION: %d', id(self))

    def update_handler_st(self, st_item, method, request_time):
        if st_item not in self._handler_st:
            self._handler_st[st_item] = {}

        if method not in self._handler_st[st_item]:
            self._handler_st[st_item][method] = {}
            self._handler_st[st_item][method]['requests'] = 0
            self._handler_st[st_item][method]['rt'] = 0

        self._handler_st[st_item][method]['rt'] += request_time
        self._handler_st[st_item][method]['requests'] += 1

    def init_app_info(self):
        self.app_version = ''
        self.app_hash = ''

        for root, dirs, files in \
            os.walk(os.path.join(os.path.realpath(options.log_root), \
                'dist')):
            for f in files:
                if f[-3:] != 'egg':
                    continue
                self.app_version = '%s; %s' % (f[:-4], options.app_version)
                app_egg = '%s/%s' % (root, f)

        if not self.app_version:
            return

        with open(app_egg, 'r') as f:
            self.app_hash = md5(f.read()).hexdigest()

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

        CommonTimer.instance().start(TApplication.instance().timer_callback)

        self.http_server =  \
            tornado.httpserver.HTTPServer(xheaders=True,
                    request_callback=TApplication.instance())
        for sockets in sockets_list:
            self.http_server.add_sockets(sockets)

    def stop(self):
        CommonTimer.instance().stop()

        if hasattr(self, 'http_server'):
            self.http_server.stop()

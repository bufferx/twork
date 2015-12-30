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
from tornado import process
import tornado.web

from twork.timer.common_timer import CommonTimer
from twork.web import action
from twork.web import assembly
from twork.utils import gen_logger
from twork.utils import common as common_util

define("bind_ip", default='127.0.0.1,',
        help="run http server on a specific address")
define("port", default=8000,
        help="run http server on a specific port")
define("backlog", default=128,
        help="the same meaning as for socket.listen", type=int)
define("env", default="debug", help="service run environment")
define("num_processes", default=-1,
        help="number of processes to fork, 0 for the number of cores", type=int)


class _TApplication(tornado.web.Application):

    @property
    def stat_info(self):
        def calcu():
            for handler, st in self._handler_st.iteritems():
                for method, _st in st.iteritems():
                    _st['rt_avg'] = _st['rt'] / _st['requests']
        calcu()

        fd_all = len(IOLoop.instance()._handlers)

        return {'fd': {'all': fd_all, 'requests': self._requests}, 'uptime': '%.3f' % (time.time() -
            self._start_time), 'handler': self._handler_st}

    @property
    def APP_INFO(self):
        return self._app_info

    def __init__(self, handlers=None, app_info=None, **settings):
        self._start_time = time.time()
        self._handler_st = {}
        self._requests = 0

        self._app_info = app_info if app_info is not None else 'No-Set'

        debug = options.env.lower() == 'debug'
        app_settings = {
                'static_path': assembly.STATIC_PATH,
                'debug':debug,
                }

        if settings:
            app_settings = settings

        _handlers = [
            (r'^/v1.0/twork/stats$', action.StatHandler,
                {'version': (1, 0)}),
        ]

        if handlers is None:
            handlers = _handlers
        else:
            handlers.extend(_handlers)

        tornado.web.Application.__init__(self, handlers, **app_settings)

    def update_handler_st(self, st_item, method, request_time):
        if st_item not in self._handler_st:
            self._handler_st[st_item] = {}

        if method not in self._handler_st[st_item]:
            self._handler_st[st_item][method] = {}
            self._handler_st[st_item][method]['requests'] = 0
            self._handler_st[st_item][method]['rt'] = 0

        self._handler_st[st_item][method]['rt'] += request_time
        self._handler_st[st_item][method]['requests'] += 1

    def __init_app_info(self):
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


@common_util.singleton
class HTTPServer(object):
    """Decorator Singleton, can't be inherited
    """
    def start(self, handlers=None, app_info=None, twork_module=None, **settings):
        sockets_list = []
        for bind_ip in options.bind_ip.split(','):
            if not bind_ip:
                break

            sockets = tornado.netutil.bind_sockets(
                    options.port,
                    address=bind_ip,
                    backlog=options.backlog)
            sockets_list.append(sockets)

        if options.num_processes >= 0:
            process.fork_processes(options.num_processes)

        if twork_module is not None:
            twork_module.setup()

        if options.timer_start:
            CommonTimer().start(twork_module.timer_callback)

        self.http_server =  \
            tornado.httpserver.HTTPServer(xheaders=True,
                    request_callback=_TApplication(handlers=handlers,
                                                   app_info=app_info,
                                                   **settings))

        for sockets in sockets_list:
            self.http_server.add_sockets(sockets)

    def stop(self):
        if hasattr(self, 'http_server'):
            self.http_server.stop()

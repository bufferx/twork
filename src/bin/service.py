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

''' tornado server
'''

import sys
import time
import signal
import socket

import tornado.web
import tornado.httpserver

import assembly

import config.options

from util import options
from util import g_logger
from domain.object.db import DB

from www.web import TApplication
from timer.common import CommonTimer

def update_global_data():
    current_hour = int(time.strftime('%H', time.localtime(time.time())))
    if current_hour == options.scheduler_wakeup_hour: 
        g_logger.info('Scheduler: update_global_data')
    else:
        g_logger.info('Scheduler: No Operation')
    pass

def handle_signal_kill(sig, frame):
    g_logger.warning( 'Catch SIG: %d' % sig )

    CommonTimer.instance().stop()
    tornado.ioloop.IOLoop.instance().stop()

def main():
    ''' main function
    '''
    # 忽略Broken Pipe信号
    signal.signal(signal.SIGPIPE, signal.SIG_IGN);
                        
    # 处理kill信号
    signal.signal(signal.SIGINT, handle_signal_kill)
    signal.signal(signal.SIGQUIT, handle_signal_kill)
    signal.signal(signal.SIGTERM, handle_signal_kill)
    signal.signal(signal.SIGHUP, handle_signal_kill)

    g_logger.info('START TORNADO WEB SERVER ...')

    for key, option in options.iteritems():
        g_logger.info('Options: (%s, %s)', key, option.value())

    try:
        if sys.version_info[:3] >= (2, 5, 2):
            #pycurl minimum supported version is 7.18.2
            tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
            pass

        sockets_list = []
        for bind_ip in options.bind_ip.split(','):
            sockets = tornado.netutil.bind_sockets(options.port,
                    address=bind_ip,
                    backlog=128)
            sockets_list.append(sockets)
        #tornado.process.fork_processes(0)

        web_app     = TApplication()
        CommonTimer.instance().start(web_app)

        http_server =  \
            tornado.httpserver.HTTPServer(xheaders=True, request_callback=web_app)
        for sockets in sockets_list:
            http_server.add_sockets(sockets)

        tornado.ioloop.IOLoop.instance().start()

        http_server.stop()
        tornado.ioloop.IOLoop.instance().close()

        g_logger.info('STOP TORNADO WEB SERVER ...')
    except socket.error as e:
        g_logger.warning('Socket Error: %s', e, exc_info=True)
    except KeyboardInterrupt as e:
        g_logger.warning('Gently Quit')
    except Exception as e:
        g_logger.error('UnCaught Exception: %s', e, exc_info=True)

if __name__ == '__main__':
    main()

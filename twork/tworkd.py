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

import tornado
from tornado.httpclient import AsyncHTTPClient

import sys
import signal

from tornado.options import options

import assembly

from twork.options import init_options
from twork.util import init_logger, g_logger
from twork.web.server import HTTPServer


def handle_signal_kill(sig, frame):
    g_logger.warning( 'Catch SIG: %d' % sig )

    tornado.ioloop.IOLoop.instance().stop()

def main():
    ''' main function
    '''
    init_options()
    init_logger()

    # 忽略Broken Pipe信号
    signal.signal(signal.SIGPIPE, signal.SIG_IGN);
                        
    # 处理kill信号
    signal.signal(signal.SIGINT, handle_signal_kill)
    signal.signal(signal.SIGQUIT, handle_signal_kill)
    signal.signal(signal.SIGTERM, handle_signal_kill)
    signal.signal(signal.SIGHUP, handle_signal_kill)

    g_logger.info('START TORNADO SERVER ...')

    for key, option in options.iteritems():
        g_logger.info('Options: (%s, %s)', key, option.value())

    try:
        if sys.version_info[:3] >= (2, 5, 2):
            #pycurl minimum supported version is 7.18.2
            AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

        HTTPServer.instance().start()
        tornado.ioloop.IOLoop.instance().start()

        HTTPServer.instance().stop()
        tornado.ioloop.IOLoop.instance().close(all_fds=True)

        g_logger.info('STOP TORNADO SERVER ...')
    except KeyboardInterrupt as e:
        g_logger.warning('Gently Quit')
    except Exception as e:
        g_logger.error('UnCaught Exception: %s', e, exc_info=True)

if __name__ == '__main__':
    main()

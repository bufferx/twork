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

import sys
import signal

from tornado.options import options

import assembly

from twork.options import init_options
from twork.util import init_logger, g_logger
from twork.web.server import HTTPServer


def _quit():
    if not tornado.ioloop.IOLoop.instance().running():
        return

    HTTPServer.instance().stop()
    tornado.ioloop.IOLoop.instance().stop()
    tornado.ioloop.IOLoop.instance().close(all_fds=True)

    g_logger.info('STOP TORNADO SERVER ...')

def _handle_signal(sig, frame):
    g_logger.warning('Catch SIG: %d, Gently Quit', sig)
    _quit()

def _reopen_log(sig, frame):
    g_logger.warning('Catch SIG: %d, ReOpen Log', sig)
    init_logger()

def _setup_signal():
    # 忽略Broken Pipe信号
    signal.signal(signal.SIGPIPE, signal.SIG_IGN);

    # 处理kill信号
    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGQUIT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)
    signal.signal(signal.SIGHUP, _handle_signal)

    signal.signal(signal.SIGUSR1, _reopen_log)

def _log_options():
    if tornado.version_info < (3, 0, 0, 0):
        for key, option in options.iteritems():
            g_logger.info('Options: (%s, %s)', key, option.value())
    else:
        for key, option in options.items():
            g_logger.info('Options: (%s, %s)', key, option)

def main():
    ''' main function
    '''
    init_options()
    init_logger()

    _setup_signal()

    _log_options()

    g_logger.info('START TORNADO SERVER ...')

    try:
        HTTPServer.instance().start()

        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        g_logger.error('UnCaught Exception: %s', e, exc_info=True)
    finally:
        _quit()

if __name__ == '__main__':
    main()

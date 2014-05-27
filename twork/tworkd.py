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

"""tworkd
"""

import tornado

import sys
import signal

from tornado.options import define
from tornado.options import options
from tornado.util import import_object

import assembly

from twork.options import init_options
from twork.utils import setup_log, gen_logger
from twork.web.server import HTTPServer


define("setup_module", default=None,
        help="setup module is injected to twork.tworkd when main function execute")


def _quit():
    if not tornado.ioloop.IOLoop.instance().running():
        return

    HTTPServer.instance().stop()
    tornado.ioloop.IOLoop.instance().stop()
    tornado.ioloop.IOLoop.instance().close(all_fds=True)

    gen_logger.info('STOP TORNADO SERVER ...')

def _handle_signal(sig, frame):
    gen_logger.warning('Catch SIG: %d, Gently Quit', sig)
    _quit()

def _reopen_log(sig, frame):
    gen_logger.warning('Catch SIG: %d, ReOpen Log', sig)
    setup_log()

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
            gen_logger.info('Options: (%s, %s)', key, option.value())
    else:
        for key, option in options.items():
            gen_logger.info('Options: (%s, %s)', key, option)

def main():
    """main function
    """
    init_options()

    WebApplication = None
    if options.setup_module is not None:
        try:
            _module = import_object(options.setup_module)
            _module.setup()
            WebApplication = _module.WebApplication
        except (ImportError, AttributeError) as e:
            gen_logger.error(e, exc_info=True)

    setup_log()

    _setup_signal()

    _log_options()

    gen_logger.info('START TORNADO SERVER ...')

    try:
        HTTPServer.instance().start()

        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        gen_logger.error('UnCaught Exception: %s', e, exc_info=True)
    finally:
        _quit()

if __name__ == '__main__':
    main()

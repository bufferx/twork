"""twork_app setup
"""

from tornado.options import options

from twork.options import setup_options

from twork_app.constants import RUN_ENV_DEBUG
from twork_app.web import assembly
from twork_app.module import Module

import twork_app.app.options


__all__ = ['setup', 'SETTINGS']


SETTINGS = {
        'static_path': assembly.STATIC_PATH,
        'debug': options.env == RUN_ENV_DEBUG,
        }

def setup():
    setup_options()
    Module()

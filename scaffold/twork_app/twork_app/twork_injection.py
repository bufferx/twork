from twork.utils import gen_logger
from twork.options import setup_options

from twork_app import APP_NAME, APP_INFO
from twork_app.web.app import HANDLERS

__all__ = ['timer_callback', 'setup', 'APP_INFO', 'HANDLERS', 'SETTINGS']

SETTINGS = {}

def timer_callback():
    gen_logger.debug('time callback')

def setup():
    setup_options()

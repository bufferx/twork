from twork.utils import gen_logger

from twork_app import APP_NAME, APP_INFO
from twork_app.web.app import HANDLERS

__all__ = ['timer_callback', 'setup', 'APP_INFO', 'HANDLERS']

def timer_callback():
    gen_logger.debug('time callback')

def setup():
    pass

"""twork_app injection entrance
"""

from twork_app.app.handlers import HANDLERS
from twork_app.app.info import APP_INFO
from twork_app.app.timer import timer_callback
from twork_app.app._setup import setup, SETTINGS

__all__ = ['timer_callback', 'setup', 'APP_INFO', 'HANDLERS', 'SETTINGS']

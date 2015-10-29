"""Define Your Timer Callback
"""

import logging


gen_logger = logging.getLogger('twork.general')


def timer_callback():
    gen_logger.debug('time callback')

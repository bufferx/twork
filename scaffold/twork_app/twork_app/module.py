"""twork_app module

One process, one Module instance. Global variables can be defined within.
"""

import logging

from tornado.options import options

from twork.utils.common import singleton


gen_logger = logging.getLogger('twork.general')


@singleton
class Module(object):
    '''Defined as a Single Object
    '''
    def __init__(self):
        gen_logger.info('Module Initialization')

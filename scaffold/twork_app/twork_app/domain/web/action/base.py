"""Base Action For WebHandler
;wa
"""

import logging
import time

from twork_app.module import Module


gen_logger = logging.getLogger('twork.general')


class BaseAction(object):
    """Base Action
    """
    INPUT_ARGUMENTS = ('queryid', )
    INNER_ARGUMENTS = ('query_id', )

    ACTION_MAP = {
            (1, 0): {
                'foo': 'bar',
                },
            }

    @property
    def module(self):
        if not hasattr(self, '_module'):
            self._module = Module()

        return self._module

    @property
    def rsp_json(self):
        """Action Response
        """
        if not hasattr(self, '_RSP_JSON'):
            return None

        return self._RSP_JSON

    def __init__(self, web_input, rsp_json=None):
        """
        """
        assert rsp_json is not None

        self.input = ObjectLikefy(web_input)
        self._now = int(time.time())

        self._RSP_JSON = rsp_json

    def execute(self):
        """Perform Action
        """
        raise NotImplementedError

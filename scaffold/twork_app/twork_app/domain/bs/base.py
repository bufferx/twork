"""Base BS
"""

import logging
import time

from twork.errors import ArgumentEmptyError
from twork.utils.object_likefy import ObjectLikefy

from twork_app.module import Module

gen_logger = logging.getLogger('twork.general')


class BaseBS(object):
    """Base BS
    """
    INPUT_ARGUMENTS = ('queryid', )
    INNER_ARGUMENTS = ('query_id', )

    EMPTY_ARGUMENTS_ALLOWS = ()

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

    def __init__(self, web_input=None, rsp_json=None):
        """
        """
        assert rsp_json is not None
        assert web_input is not None

        self.input = ObjectLikefy(web_input)
        self._now = int(time.time())

        self._RSP_JSON = rsp_json

    def execute(self):
        """Perform Action
        """
        self._common_check()
        self._setup_response()

    def _common_check(self):
        """Checking Arguments
        """
        def _check_empty(k, v):
            """Check Argument Whether Is Empty
            """
            if not v:
                raise ArgumentEmptyError(k)

        #Checking Custom Arguments
        for idx, inner_argu in enumerate(self.INNER_ARGUMENTS):
            if inner_argu in self.EMPTY_ARGUMENTS_ALLOWS:
                continue

            input_argu = self.INPUT_ARGUMENTS[idx]
            _check_empty(input_argu, getattr(self.input, inner_argu))

    def _setup_response(self, *args):
        """Setup Response
        """
        raise NotImplementedError

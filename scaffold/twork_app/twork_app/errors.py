# -*- coding: utf-8 -*-

'''Error Defining
'''

from twork.errors import BaseError


class TworkAppBaseError(BaseError):
    """Twork App Base Error, Customized Error
    """
    ERROR = (40000, 'Twork App Error')

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

'''Error Defining 
'''


class ErrorCode(object):
    DEFAULT = 0xff
    SUCCESS = 0x00
    # 参数
    ARGUMENTS = 100
    ARGUMENTS_EMPTY = 101
    ARGUMENTS_TYPE = 102
    ARGUMENTS_DATE = 103
    # 网络IO
    TCP = 500
    HTTP = 501
    # 业务逻辑
    DB_ERROR = 301
    DB_EMPTY = 302
    # others
    TOO_MANY_REQUEST = 429


class ErrorMessage(object):
    SUCCESS = 'SUCCESS'
    DEFAULT = 'ERROR'
    NO_DATA = 'NO_DATA'
    DB = 'ERROR_DB'
    DB_INTERFACE = 'ERROR_DB_INTERFACE'
    DB_TOOMANYCONNECTIONS = 'ERROR_DB_TOOMANYCONNECTIONS'
    DB_DATABASEERROR = 'DB_DATABASEERROR'
    PARAMS = 'ERROR_PARAMS'


class BaseError(Exception):
    ERROR = (0XFF, 'UNCAUGHT ERROR')

    def __init__(self, code=None, msg=None):
        self.e_code = self.__class__.ERROR[0] if code is None else code
        self.e_msg = self.__class__.ERROR[1] if msg is None else msg

    def __str__(self):
        return '({0}, {1})'.format(self.e_code, self.e_msg)


class TooManyRequestError(BaseError):
    ERROR = (429, 'Too Many Requests')


class ArgumentError(BaseError):
    ERROR = (4000, 'INVALID ARGUMENT')

    def __init__(self, argument_name):
        self.e_code = self.ERROR[0]
        self.e_msg  = '{0}: {1}'.format(self.ERROR[1],
                argument_name)

    def __str__(self):
        return '({0}, {1})'.format(self.e_code, self.e_msg)


class ArgumentNotFoundError(ArgumentError):
    """
    """
    ERROR = (4001, 'Argument Not Found')


class ArgumentEmptyError(ArgumentError):
    """
    """
    ERROR = (4002, 'Argument Can\'t Be Empty')


class ArgumentTypeError(ArgumentError):
    """Bad Argument Type
    """
    ERROR = (4003, 'Argument Type Invalid')


class BizBaseError(BaseError):
    """Business Base Error

    Twork Module May Need To Inherit This Class.
    """
    ERROR = (40000, 'Biz Error')


class ServiceError(BaseError):
    """
    """
    ERROR = (50000, 'Serivce ERROR')


class DBError(BaseError):
    """
    """
    ERROR = (50010, 'DB ERROR')


class DBAuthError(BaseError):
    """
    """
    ERROR = (50011, 'DB Auth ERROR')

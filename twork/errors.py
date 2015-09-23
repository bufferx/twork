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
    TOO_MANY_REQUEST = 400


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


class TooManyRequest(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.TOO_MANY_REQUEST
        self.e_msg = 'Too Many Requests: %s' % msg

    def __str__(self):
        return self.e_msg


class ArgumentError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.ARGUMENTS
        self.e_msg = 'Invalid Argument: %s' % msg

    def __str__(self):
        return self.e_msg 


class ArgumentEmptyError(BaseError):
    def __init__(self, argument_name=''):
        self.e_code = ErrorCode.ARGUMENTS
        self.e_msg = 'Argument[%s] Can\'t Be NULL' % argument_name.upper()

    def __str__(self):
        return self.e_msg 


class ArgumentTypeError(BaseError):
    def __init__(self, argument_name=''):
        self.e_code = ErrorCode.ARGUMENTS
        self.e_msg = 'Argument[%s]\'type Is Invalid' % argument_name.upper()

    def __str__(self):
        return self.e_msg 


class ArgumentDateError(ArgumentError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.ARGUMENTS_DATE
        self.e_msg = 'Invalid Date: %s' % msg

    def __str__(self):
        return self.e_msg 


class DBError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_ERROR 
        self.e_msg = 'DB Error: %s' % msg

    def __str__(self):
        return self.e_msg 


class DBEmpty(DBError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_EMPTY 
        self.e_msg = 'DB Empty: %s' % msg

    def __str__(self):
        return self.e_msg 

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

'''Define Error 
'''

class ErrorCode(object):
    DEFAULT = 0xff
    SUCCESS = 0x00
    # 参数
    PARAMETERS = 100 
    PARAMETERS_EMPTY = 101 
    PARAMETERS_TYPE = 102 
    PARAMETERS_DATE = 103 
    PARAMETERS_HOTELIDS = 104
    # 网络IO
    TCP = 500 
    HTTP = 501 
    # 业务逻辑
    DB_ERROR = 301 
    DB_EMPTY = 302 

class ErrorMessage(object):
    SUCCESS = 'SUCCESS'
    pass

class BaseError(Exception):
    def __init__(self, msg='Default'):
        self.e_code = ErrorCode.DEFAULT
        self.e_msg = 'Uncaught Exception: %s' % Exception.message

    def __str__(self):
        return self.e_msg 
    pass

class ParameterError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Invalid Parameter: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterEmptyError(BaseError):
    def __init__(self, parameter_name=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Parameter[%s] Can\'t Be NULL' % parameter_name.upper()
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterTypeError(BaseError):
    def __init__(self, parameter_name=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Parameter[%s]\'type Is Invalid' % parameter_name.upper()
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterDateError(ParameterError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.PARAMETERS_DATE 
        self.e_msg = 'Invalid Date: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class DBError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_ERROR 
        self.e_msg = 'DB Error: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class DBEmpty(DBError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_EMPTY 
        self.e_msg = 'DB Empty: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

# -*- coding: utf-8 -*-
#
# Copyright 2015 Zhang ZY<http://idupx.blogspot.com/> 
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


import functools
import logging

from tornado import gen

from twork.errors import BaseError


gen_logger = logging.getLogger('twork.general')


def web_method_wrapper(func):
    @functools.wraps(func)
    @gen.coroutine
    def wrapper(self, *args, **kwargs):
        self.init_rsp_json()

        try:
            yield func(self, *args, **kwargs)
        except BaseError as e:
            self.rsp_json['code']  = e.e_code
            self.rsp_json['msg']  = e.e_msg

            self.api_response(self.rsp_json)
            gen_logger.error(e, exc_info=True)
        except StopIteration as e:
            raise e
        except Exception as e:
            self.api_response(self.rsp_json)
            gen_logger.error(e, exc_info=True)

    return wrapper

coroutine_engine = web_method_wrapper

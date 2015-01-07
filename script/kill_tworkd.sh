#!/bin/bash
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

USAGE="${0} -m[TWORK_APP] -v[TWORK_APP_VERSION] -n[APP_ENV]";

if [ $# -lt 1 ]; then
    echo $USAGE;
    exit 1;
fi


while getopts "m:v:n:h" opt;
do
    case $opt in
        m)
            TWORK_APP=$OPTARG;
            ;;
        v)
            APP_VERSION=$OPTARG;
            ;;
        n)
            APP_ENV=$OPTARG;
            ;;
        h)
            echo $USAGE;
            exit;
            ;;
        ?)
            echo $USAGE;
            exit 1;
            ;;
        :)
            echo "Option [$OPTARG] requires an argument";
            exit 1;
            ;;
    esac
done


RPOC_TITLE="[t]work::${TWORK_APP}/${APP_VERSION}#${APP_ENV}";

ps aux |  grep ${RPOC_TITLE} | awk '{print $2}' | xargs kill -15

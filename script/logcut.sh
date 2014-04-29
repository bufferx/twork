#!/bin/bash
#
# Copyright 2012 Zhang ZY<http://github.com/bufferx>
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


USAGE="${0} -f[LOG_PATH]";

if [ $# -lt 1 ]; then
    echo $USAGE;
    exit 1;
fi

while getopts ":f:" opt;
do
    case $opt in
        f)  
            LOG_PATH=$OPTARG;
            ;;  
        ?)  
            echo $USAGE;
            exit 1
            ;;  
        :)  
            echo "Option -$OPTARG requires an argument";
            exit 1;
            ;;  
    esac
done

YESTERDAY=`date +'%Y-%m-%d' --date="yesterday"`;
#echo $LOG_PATH;

arr=$(echo $LOG_PATH | tr "," "\n")

for x in $arr
do
    mv ${x} "${x}.${YESTERDAY}"
done

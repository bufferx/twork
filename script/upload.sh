#!/bin/bash
# Author: Bufferx(idup2x@gmail.com)

#上线脚本

echo -e "....pull & push....\n"

git checkout master
git pull origin master
git push origin master

echo -e "upload begin.....\n"

echo -e "\tupload for server_0.....\n"
#ssh -A www-data@server_0 "cd $project_path; git checkout master; git pull origin master;"
echo -e "\n"

echo -e "upload over....."

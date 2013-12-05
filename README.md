twork
==========

twork is a neTwork server framework based on tornado

Environment
------------
* [virtualenv](http://www.virtualenv.org/en/latest/)

Requirements
------------
The following libraries are required

* [tornado](http://github.com/facebook/tornado)
* [bf4x-pyutil](https://github.com/bufferx/pyutil)

Usage & Debug
------------
* source $VIRTUALENV/bin/activate
* cd $TORNADO_PATH && python setup.py install
* cd $PYUTIL_PATH && python setup.py install
* python twork/tworkd.py -bind_ip=localhost -port=8000
* or tworkd -bind_ip=localhost -port=8000

Deploy
------------
* source $VIRTUALENV/bin/activate
* cd $TORNADO_PATH && python setup.py install
* cd $PYUTIL_PATH && python setup.py install
* python setup.py build_py -O2 bdist_egg --exclude-source-files
* easy_install dist/twork-VERSION-PYTHON.egg

Supervisor
------------
* [supervisord](http://supervisord.org/)
* [conf-template](https://github.com/bufferx/supervisor_conf_tpl)
* command: python -OO $VIRTUALENV/bin/tworkd -config_file=$TWORK_CONFIG_PATH

Publish
* bash script/deploy.sh

Case
------------
* http://localhost:8000/v1.0/twork/stats

Fork
------------
* fork the specified project from twork and create the git repo
* python script/forkme.py

Issues
------

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)

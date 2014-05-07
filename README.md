twork
==========

twork is a neTwork server framework based on tornado

Environment
------------
* [virtualenv](http://www.virtualenv.org/en/latest/) is a tool to create
  isolated Python environments

Requirements
------------
The following libraries are required

* [tornado](http://github.com/facebook/tornado)

Usage
------------
* source $VIRTUALENV/bin/activate
* cd $TWORK_PATH && python setup.py install
* tworkd -bind_ip=localhost -port=8000

Supervisor
------------
* [supervisord](http://supervisord.org/)
* [conf-template](https://github.com/bufferx/supervisor_conf_tpl)
* command: python -OO $VIRTUALENV/bin/tworkd -config_file=$TWORK_CONFIG_PATH

Case
------------
* http://localhost:8000/v1.0/twork/stat

Publish
------------
Build your local [PyPI Server](https://pypi.python.org/pypi/pypiserver) first

* make publish

Deploy
------------

* easy_install -U -i http://localhost:8080/simple twork

Project Builder
------------
Create your own project based on twork

* python twork-admin.py -project=$PROJECT -prefix=~/workspace

Issues
------

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)

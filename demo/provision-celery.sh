#!/bin/bash

export LANG=C
export LC_ALL=C
[[ $(whoami) == 'vagrant' ]] || exec runuser - vagrant $0

sudo apt-get update \
&& sudo apt-get -y upgrade \
&& sudo apt-get -y install python3 python3-pip python3-virtualenv virtualenv \
&& virtualenv -p python3 venv \
&& source venv/bin/activate \
&& pip install celery \
&& cp -p /vagrant/*.{sh,py} . \
&& sudo cp /vagrant/hosts /etc/hosts



#!/bin/bash

export LANG=C
export LC_ALL=C
source venv/bin/activate
celery -A myapp worker -n "$(hostname)@$(hostname)" -l info -c1


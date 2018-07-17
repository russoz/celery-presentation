#!/bin/bash

export LANG=C
export LC_ALL=C
source venv/bin/activate

[[ -z "$1" ]] && { echo 'Must pass an app name!' >&2; exit 1; }

celery -A "$1" worker -n "$(hostname)@$(hostname)" -l info -c1


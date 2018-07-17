#!/bin/bash

source venv/bin/activate

count="${1:-30}"
maxrand="${2:-10}"

exec python add2next.py "$count" "$maxrand"


#!/bin/bash

python test/testcase.py

# flake8 --format=pylint --max-line-length=120 --ignore=F403 --builtins=_ \
# $(find src/timeago/ -name "*.py" -print)
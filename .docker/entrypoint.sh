#!/bin/bash

pdm install
eval "$(pdm --pep582)"
python src/manage.py runserver 0.0.0.0:8000
tail -f /dev/null
#!/bin/bash

pdm install
# python manage.py migrate
# python src/manage.py runserver 0.0.0.0:8000
tail -f /dev/null
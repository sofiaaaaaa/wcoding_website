#!/usr/bin/env bash

workon wcoding_website
cd ~/webapps/wcoding_website
git pull
python manage.py migrate
python manage.py collectstatic

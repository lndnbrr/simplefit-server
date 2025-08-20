#!/bin/bash

rm db.sqlite3
rm -rf ./simplefitapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations simplefitapi
python3 manage.py migrate simplefitapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens


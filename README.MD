This is an assignment from instawork.

Install python3 virtual environment:

python3 -m pip install --user virtualenv

Create vrtual envirnment folder which uses python3 by default:

python3 -m virtualenv env3

Install django:

pip3 install django

Install requirements from requirements.txt

ADD below e lines inside instawork/instawork/__init__.py

import pymysql

pymysql.install_as_MySQLdb()

Go to mysql and create a database called 'instawork_db'

Change your USER and PASSWORD inside settings.py file according to what you gave while creating database.




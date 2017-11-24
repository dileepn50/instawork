This is an assignment from instawork.

1: Install python3 virtual environment:

python3 -m pip install --user virtualenv

2: Create vrtual envirnment folder which uses python3 by default:

python3 -m virtualenv env3

3: Install django:

pip3 install django

4: Install requirements from requirements.txt

5: ADD below  lines inside instawork/instawork/__init__.py

import pymysql

pymysql.install_as_MySQLdb()

6: Go to mysql and create a database called 'instawork_db'

Change your USER and PASSWORD inside settings.py file according to what you gave while creating database.




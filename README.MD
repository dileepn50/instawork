This is an assignment from instawork.

1: Install python3 virtual environment:

	python3 -m pip install --user virtualenv

2: Create vrtual envirnment folder which uses python3 by default:

	python3 -m virtualenv env3

3: Inside virtual environment install requirred packages :
	pip3 install -r requirements.txt 


4: ADD below  lines inside instawork/instawork/__init__.py

	import pymysql

	pymysql.install_as_MySQLdb()

5: Go to mysql and create a database called 'instawork_db'

6: Change your USER and PASSWORD inside settings.py file according to what you gave while creating database.




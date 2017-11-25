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

7: Go inside instawork directory where manage.py file is present and run 
	i: python manage.py makemigraions 
	ii: python manage.py makemigrations app
    iii: python manage.py migrate

8: Import the db by running the command:
		/usr/local/mysql/bin/mysql -u username -p instawork_db < /Users/dileepn/temp/instawork/mysql_database_dump.sql 

9: Run the server:
   		python manage.py runserver

10: To list team member list and to add new member:

	http://127.0.0.1:8000/api/team/team_list

	sample input:
		{
    "first_name": "deepak",
    "last_name": "pm",
    "phone_number": 99867793090,
    "email": "deepka@gmail.com",
    "role": "regular"
}

11: To edit or remove particualr team member:

	http://127.0.0.1:8000/api/team/team_member_edit/id 				#id should be replaced by id of the team member

	example: http://127.0.0.1:8000/api/team/team_member_edit/20/
	 


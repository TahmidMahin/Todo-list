import sqlite3

def get_password(username):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select password
		from users
		where username = '{username}';
		''')
	password = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()

	return password

def find_user(username):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select *
		from users
		where username = '{username}';
		''')
	exist = cursor.fetchone()

	connection.commit()
	cursor.close()
	connection.close()

	if exist is None:
		return False
	return True

def add_user(username, password):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Insert into users(username, password)
		Values('{username}', '{password}');
		''')

	connection.commit()
	cursor.close()
	connection.close()


def find_activity(username, activity):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select *
		from acitvity
		where username = '{username}' and activity = '{activity}';
		''')
	exist = cursor.fetchone()

	connection.commit()
	cursor.close()
	connection.close()

	if exist is None:
		return False
	return True

def get_activity(username):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select activity, status
		From activity
		Where username = '{username}';
		''')

	activity = cursor.fetchall()
	connection.commit()
	cursor.close()
	connection.close()
	return activity

def add_activity(username, activity, status):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Insert into activity(username, activity, status)
		Values('{username}', '{activity}', '{status}');
		''')
	connection.commit()
	cursor.close()
	connection.close()

def remove_activity(username, activity):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Delete From activity
		Where username = '{username}' and activity = '{activity}';
		''')
	connection.commit()
	cursor.close()
	connection.close()

def update_activity(username, activity, status):
	remove_activity(username, activity)
	add_activity(username, activity, status)
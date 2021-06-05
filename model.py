import sqlite3


#For users table
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

def get_users():
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select username
		From users;
		''')

	users = cursor.fetchall()
	connection.commit()
	cursor.close()
	connection.close()

	return users

def get_totalUser():
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select Count(*)
		from users;
		''')
	totalUser = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()

	return totalUser

def get_newUser():
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select Count(*)
		from users
		where created < Datetime('now') and created >= Datetime('now', '-24 hours');
		''')
	newUser = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()

	return newUser

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
		Insert into users(username, password, created)
		Values('{username}', '{password}', Datetime('now'));
		''')

	connection.commit()
	cursor.close()
	connection.close()

def remove_user(username):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Delete from users
		Where username = '{username}'
		''')

	connection.commit()
	cursor.close()
	connection.close()


#For activity table
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

def get_totalList():
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select count(distinct username)
		From activity;
		''')

	totalList = cursor.fetchone()[0]
	connection.commit()
	cursor.close()
	connection.close()

	return totalList

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


#For admins table
def get_admin_password(admin):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select password
		from admins
		where admin = '{admin}';
		''')
	password = cursor.fetchone()[0]

	connection.commit()
	cursor.close()
	connection.close()
	
	return password

def find_admin(admin):
	connection = sqlite3.connect('userinfo.db', check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute(f'''
		Select *
		from admins
		where admin = '{admin}';
		''')
	exist = cursor.fetchone()

	connection.commit()
	cursor.close()
	connection.close()

	if exist is None:
		return False
	return True

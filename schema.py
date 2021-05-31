import sqlite3

connection = sqlite3.connect('userinfo.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
	'''Create Table users(
		username Varchar(16) Primary Key,
		password Varchar(32) Check(length(password) > 6)
		);'''
	)

cursor.execute(
	'''Create Table activity(
		username Varchar(16),
		activity Varchar(100),
		status Varchar(20) Check(status in ('Due', 'In progress', 'Done')),
		Primary Key (username, activity),
		Foreign Key (username) references users(username)
	);'''
	)

connection.commit()
cursor.close()
connection.close()

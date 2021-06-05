import sqlite3

connection = sqlite3.connect('userinfo.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute('''
	Create Table if not exists users(
		username Varchar(16) Primary Key,
		password Varchar(32) Check(length(password) > 5),
		created Datetime
		);'''
	)

cursor.execute('''
	Create Table if not exists activity(
		username Varchar(16),
		activity Text,
		status Varchar(20) Check(status in ('Due', 'In progress', 'Done')),
		Primary Key (username, activity),
		Foreign Key (username) references users(username)
		on Delete Cascade
	);'''
	)

cursor.execute('''
	Create Table if not exists admins(
		admin Varchar(16) Primary Key,
		password Varchar(32) Check(length(password) > 5)
	);'''
	)

connection.commit()
cursor.close()
connection.close()

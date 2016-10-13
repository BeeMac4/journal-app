import sqlite3

conn = sqlite3.connect ('journalDB')
c = conn.cursor()
user_ID = 1

'''
def user_write(username):
	global user_ID
	user_ID += 1
	c.execute ("INSERT INTO users (user_ID, user_name) VALUES (?, ?)",
		(user_ID, username)) 
	conn.commit()'''


def user_login(username):
	row = c.execute('SELECT * FROM users')
	print (row)
	rows = c.fetchall()
	for row in rows:
		if username in row:
			return	row[0]

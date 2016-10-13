import sqlite3
import random

conn = sqlite3.connect ('journalDB')
c = conn.cursor()
user_ID = 1

def user_login(username):
	row = c.execute('SELECT * FROM users')
	print (row)
	rows = c.fetchall()
	for row in rows:
		if username in row:
			return	row[0]

def user_write(username):
	global user_ID
	user_ID = random.randint(1,10)
	c.execute ("INSERT INTO users (user_ID, user_name) VALUES (?, ?)",
		(user_ID, username)) 
	conn.commit()

def user_store(user_ID, title, content):
        
        row = c.execute('INSERT INTO journal_entries (journal_ID, user_ID, journal_title, journal_content) VALUES (?,?,?,?)',(1,int(user_ID), title, content))
        print ('Added successfully')

def journal_read(user_ID):
        
        row = c.execute('SELECT * FROM journal_entries WHERE user_ID = user_ID')
        print (row.fetchall())

while True:
        user_name = input ('Please input your mane to login. Or nothing to exit: ')
        #print (user_name)
        user_ID = user_login(user_name)
        #print (user_ID)
        if (user_ID):
                print ('Login successful. Welcome ' + user_name)

                journal_purpose = input ("To read your entries, type 'R'. = To add an entry, type 'W'.").lower()

                if (journal_purpose == 'r'):
                        journal_read(user_ID)
                
                elif (journal_purpose == 'w'):
                        title = input ('Please enter the title')
                        content = input ('Please enter content')
                        user_store(user_ID, title, content)


        elif (user_name == ''):
                break
        else:
                print ('\nNo such username found')




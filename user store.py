
import sqlite3 
from user_login.py import user_login


con = sqlite3.connect('journalDB')
c = conn.cursor()


import sqlite3

conn = sqlite3.connect ('journalDB')
c = conn.cursor()
user_ID = 1


def user_store(username):
	row = c.execute('INSERT INTO journal_entries' (journal_ID, user_ID, journal_title, journal_content) VALUES (?, ?, ?, ? )' (random.randint(1,100000),user_ID,title, content))
	print ('added successfully')
	
	
	
#/usr/bin/python

import MySQLdb
import MySQLdb.cursors


host = 'localhost'
username = 'marc'
password = ''
Error = MySQLdb.Error

def connectdb (host = 'localhost', username =  'marc', password = '', db ='nginStatLog'):
    db = MySQLdb.connect (host, username ,password, db)
    c = db.cursor()
    return db, c
	
def sconnect():	
    return None



        

#!/usr/bin/python
import MySQLdb


db = MySQLdb.connect(host='localhost',user='root',passwd='maksat',db='my_db') # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 
query=("insert into temperature values (NULL,44.4,56,'2098-01-19 03:14:07')")
# Use all the SQL you like
#cur.execute("SELECT * FROM temperature")
cur.execute(query)
db.commit()
db.close()



# print all the first cell of all the rows
#for row in cur.fetchall() :
 #   print row[1]
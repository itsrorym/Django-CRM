import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root1',
	passwd = 'yourpasswd',
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE rmvadb")

print ("All Done!")

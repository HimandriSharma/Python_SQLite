import sqlite3

conn = sqlite3.connect("Lib1.db")

print("Opened database Lib1.db here!")


conn.execute('''CREATE TABLE BOOKS (ID INT PRIMARY KEY NOT NULL,NUMBER_AVAILABLE INT NOT NULL);''')

print("Table BOOKS is created successfully")



conn.close()
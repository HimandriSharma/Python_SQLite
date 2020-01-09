import sqlite3

conn = sqlite3.connect("Lib1.db")

print("Opened database Lib1.db here!")

conn.execute("INSERT INTO BOOKS (ID,NUMBER_AVAILABLE) \
             VALUES(001,5)")
conn.execute("INSERT INTO BOOKS (ID,NUMBER_AVAILABLE) \
     VALUES(002,5)")
conn.execute("INSERT INTO BOOKS (ID,NUMBER_AVAILABLE) \
    VALUES(003,5)")
conn.execute("INSERT INTO BOOKS (ID,NUMBER_AVAILABLE) \
    VALUES(004,5)")

cursor = conn.execute("SELECT ID,NUMBER_AVAILABLE from BOOKS")
for row in cursor:
   print( "ID = ", row[0])
   print ("NUMBER_AVAILABLE = ", row[1])
print ("Operation done successfully")

conn.close()
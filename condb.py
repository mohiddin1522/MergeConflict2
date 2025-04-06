import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Mohiddin@Sri1319",
)

print(myDB)

cursor = myDB.cursor()

cursor.execute("select * from pydb.marks")
for row in cursor:
    print(row)
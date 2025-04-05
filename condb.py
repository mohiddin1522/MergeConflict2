import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Mohiddin@Sri1319",
)

print(myDB)
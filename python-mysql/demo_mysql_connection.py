import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root123@"
)

print(mydb)
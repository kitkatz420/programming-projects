import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Potato123'
)
print(mydb)

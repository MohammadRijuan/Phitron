import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="987654321"
)

print(my_db)
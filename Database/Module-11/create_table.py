import mysql.connector

db_name = "python_test_db"

my_db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="987654321",
    database=db_name
)

mycursor = my_db_connection.cursor()

sql_query =  f"""
        create table Student(
        Roll char(4),
        Name varchar(50)
    );
"""
mycursor.execute(sql_query)
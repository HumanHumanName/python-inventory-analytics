# Requires MqSQL connector
import mysql.connector as conn

user_name = str(input("Please enter your MySQL username: "))
user_password = str(input("Please enter your MySQL password: "))
print("Running locally...")

conn_obj = conn.connect(host = "localhost", user = user_name, passwd = user_password)

if conn_obj.is_connected() == True:
    print("Connected successfully")

cursor = conn_obj.cursor()

# Working under a database called test_database; Setup
# Replace test_database with real name later

#cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")

# cursor.execute("""CREATE TABLE test_database.inventory
#                 (
#                     item_id int(10) not null,
#                     item_name varchar(20) not null,
#                     item_count int(10) not null
#                 );""")


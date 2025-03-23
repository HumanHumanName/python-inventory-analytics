# Requires MqSQL connector
import mysql.connector as conn
import setup

user_name = str(input("Please enter your MySQL username: "))
user_password = str(input("Please enter your MySQL password: "))
print("Running locally...")

# TO ADD try catch with from mysql.connector import errorcode for failure to connect
conn_obj = conn.connect(host = "localhost", user = user_name, passwd = user_password)

if conn_obj.is_connected() == True:
    print("Connected successfully")

cursor = conn_obj.cursor()

setup.initialise_tables(cursor)

#cursor.execute("USE test_database;") #Debug

# cursor.execute("SHOW COLUMNS FROM inventory;") #Debug
# for i in cursor: #Debug
#     print(i) #Debug

# cursor.execute("SHOW COLUMNS FROM orders;") #Debug
# for i in cursor: #Debug
#     print(i) #Debug
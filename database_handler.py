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

# margin is in percentages
# cursor.execute("""CREATE TABLE test_database.inventory
#                 (
#                     item_id int(10) not null AUTO_INCREMENT,
#                     item_name varchar(20) not null,
#                     item_cost decimal(8,2) not null,
#                     item_margin decimal(5,2) not null,
#                     item_stock int(10) not null,
#                     item_manufacturer_name varchar(40) not null,
#                     item_manufacturer_incharge varchar(20) not null,
#                     item_manufacturer_contact_no int(10) not null,
#                     PRIMARY KEY (item_id)
#                 );""")


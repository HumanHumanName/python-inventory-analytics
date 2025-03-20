# Requires MqSQL connector
import mysql.connector as conn

conn_obj = conn.connect(host = "localhost", user = "kores",passwd = '0.314159')

if conn_obj.is_connected() == True:
    print("Connected successfully")
import mysql.connector as conn

conn_obj = conn.connect(host = "localhost", user = "kis", password = "youbettergetthisrightfirstry",database = "test")

if conn_obj.is_connected() == True:
    print("Connected successfully")

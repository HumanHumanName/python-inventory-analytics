# Requires MqSQL connector
import mysql.connector as conn
import setup

conn_obj = "" # this is used to create the connection to mysql via enter_mysql()

def enter_mysql():
    global conn_obj

    correct_credentials = False
    while correct_credentials != True:
        try:
            user_name = str(input("Please enter your MySQL username: "))
            user_password = str(input("Please enter your MySQL password: "))
            print("Running locally...")

            conn_obj = conn.connect(host = "localhost", user = user_name, passwd = user_password)
            correct_credentials = True
        except:
            print("There was a mistake with the username/password; Please try again \n")

    if conn_obj.is_connected() == True:
        print("Connected successfully")

    cursor = conn_obj.cursor()
    setup.initialise_tables(cursor)
    cursor.close() # CC Remember to close the connection later as well

def initialise_new_items(values):

    # values is a list of tuples; each tuple describes an item in the format: (item_name,item_cost,item_gst,item_discount,item_final_cost,item_margin,item_stock,item_manufacturer_name,item_manufacturer_incharge,item_manufacturer_contact_no)
    command = """INSERT INTO inventory (item_name,item_cost,item_gst,item_discount,item_final_cost,item_margin,item_stock,item_manufacturer_name,item_manufacturer_incharge,item_manufacturer_contact_no)
                VALUES
            """

    for i in values:
        command += str(i) + ","

    command = command[:-1] + ";" # as last element ends with colon not comma

    cursor = conn_obj.cursor()
    cursor.execute(command)
    cursor.execute("commit")
    cursor.close()

def initialise_new_orders(values):

    # values is a list of tuples; each tuple describes an order in the format: (order_item_name,order_initial_cost,order_gst,order_discount,order_final_cost,order_quantity,order_customer_name,order_customer_contact_no)
    command = """INSERT INTO orders (order_item_name,order_initial_cost,order_gst,order_discount,order_final_cost,order_quantity,order_customer_name,order_customer_contact_no)
                 VALUES
              """

    for i in values:
        command += str(i) + ","

    command = command[:-1] + ";" # as last element ends with colon not comma

    cursor = conn_obj.cursor()
    cursor.execute(command)
    cursor.execute("commit")
    cursor.close()
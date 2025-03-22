
# Only run once on initialisation

def initialise_tables(cursor):
  # Working under a database called test_database; Setup
  # Replace test_database with real name later
  cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")

  cursor.execute("USE test_database;")
  # margin, discount is in percentages
  cursor.execute("""CREATE TABLE IF NOT EXISTS test_database.inventory
                  (
                      item_id int(10) not null AUTO_INCREMENT,
                      item_name varchar(20) not null,
                      item_cost decimal(8,2) not null,
                      item_gst decimal(8,2) not null,
                      item_discount decimal(5,2) not null,
                      item_final_cost decimal(8,2) not null,
                      item_margin decimal(5,2) not null,
                      item_stock int(10) not null,
                      item_manufacturer_name varchar(40) not null,
                      item_manufacturer_incharge varchar(20) not null,
                      item_manufacturer_contact_no int(10) not null,
                      PRIMARY KEY (item_id)
                  );""")

  # discount is in percentages
  cursor.execute("""CREATE TABLE IF NOT EXISTS test_database.orders
                  (
                      order_id int(10) not null AUTO_INCREMENT,
                      order_item_name varchar(20) not null,
                      order_initial_cost decimal(8,2) not null,
                      order_gst decimal(8,2) not null,
                      order_discount decimal(5,2) not null,
                      order_final_cost decimal(8,2) not null,
                      order_quantity int(10) not null,
                      order_customer_name varchar(20) not null,
                      order_customer_contact_no int(10),
                      PRIMARY KEY (order_id)
                  );""")



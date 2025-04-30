import tkinter as tk
from tkinter import ttk
import database_handler

def run_GUI():
  root = tk.Tk()
  root.title("Test view")
  root.geometry("600x385")
  root.resizable(False, False)

  # setting style
  style=ttk.Style()
  style.theme_use('clam')

  database_label = tk.Label(root,text = "Database Viewer", relief = "raised")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 10,
                     pady = 10,
                     sticky = "nesw"
                     )

  other_functions_label = tk.Label(root, text = '                            Other Functions                            ', relief = "raised")
  other_functions_label.grid(row = 0,
                            column = 1,
                            pady = 10,
                            sticky = "e"
                            )

  button_frame = tk.Frame(root)
  button_frame.grid(row = 1,
                    column = 1,
                    sticky = "nsew"
                    )

  #CC insure the ordering of the properties in tk brackets is consitant and add icons to buttons
  modelling_view_button = tk.Button(button_frame,
                                    text = "Modelling \n View",
                                    height = 5,
                                    width = 10
                                    )

  modelling_view_button.grid(row = 0,
                            column = 0,
                            padx = 3,
                            pady = 5
                            )

  refresh_database_button = tk.Button(button_frame,
                                     text = "Refresh \n Database",
                                     height = 5,
                                     width = 6,
                                     )

  refresh_database_button.grid(row = 0,
                              column = 1,
                              pady = 5,
                              sticky = "e"
                             )

  import_database_button = tk.Button(button_frame,
                                    text = "Import \n Database",
                                    height = 5,
                                    width = 6,
                                    )

  import_database_button.grid(row = 0,
                             column = 2,
                             pady = 5,
                             sticky = "w"
                             )
  # Notebook to contain the two tables in our database
  tables_notebook = ttk.Notebook(root)
  tables_notebook.grid(row = 1,
                       column = 0,
                       padx = 10
                       )

  inventory_tab= ttk.Frame(tables_notebook)
  tables_notebook.add(inventory_tab, text= "    Inventory    ")

  orders_tab= ttk.Frame(tables_notebook)
  tables_notebook.add(orders_tab, text= "    Orders    ")

  # inventory viewer code
  inventory_data = database_handler.retrieve_via_sql_query("item_id,item_name,item_cost,item_final_cost,item_stock","inventory")

  inventory_viewer = ttk.Treeview(inventory_tab,
                                  columns = ("item_id","item_name","item_cost","item_final_cost","item_stock"),
                                  show = 'headings',
                                  height = 13
                                  )
  inventory_viewer.grid(row = 1,
                       column = 0,
                       sticky = "e"
                       )

  # creating the scrollbar
  scrollbar = ttk.Scrollbar(inventory_tab, orient = "vertical", command = inventory_viewer.yview)
  scrollbar.grid(row = 1,
                 column = 1,
                 sticky="nswe"
                 )
  inventory_viewer.configure(yscrollcommand=scrollbar.set)

  # initialising columns
  inventory_viewer.column("item_id", anchor="center", width=40)
  inventory_viewer.heading('item_id', text = 'S.No')

  inventory_viewer.column("item_name", anchor="center", width=80)
  inventory_viewer.heading('item_name', text = 'Name')

  inventory_viewer.column("item_cost", anchor="center", width=55)
  inventory_viewer.heading('item_cost', text = 'Cost')

  inventory_viewer.column("item_final_cost", anchor="center", width=55)
  inventory_viewer.heading('item_final_cost', text = 'Total')

  inventory_viewer.column("item_stock", anchor="center", width=50)
  inventory_viewer.heading('item_stock', text = 'Stock')

  inventory_viewer.grid(row = 1,column = 0)

  # insert values into inventory_viewer
  for i in inventory_data:
    inventory_viewer.insert(parent = '', index = tk.END, values = i)

  # orders viewer code
  orders_data = database_handler.retrieve_via_sql_query("order_id,order_item_name,order_customer_name,order_final_cost,order_quantity","orders")

  orders_viewer = ttk.Treeview(orders_tab,
                              columns = ("order_id","order_item_name","order_customer_name","order_final_cost","order_quantity"),
                              show = 'headings',
                              height = 13
                              )
  orders_viewer.grid(row = 1,
                       column = 0,
                       sticky = "e"
                       )

  # creating the scrollbar
  scrollbar = ttk.Scrollbar(orders_tab, orient = "vertical", command = orders_viewer.yview)
  scrollbar.grid(row = 1,
                 column = 1,
                 sticky="nswe"
                 )
  orders_viewer.configure(yscrollcommand=scrollbar.set)

  # initialising columns
  orders_viewer.column("order_id", anchor="center", width=40)
  orders_viewer.heading('order_id', text = 'S.No')

  orders_viewer.column("order_item_name", anchor="center", width=80)
  orders_viewer.heading('order_item_name', text = 'Item')

  orders_viewer.column("order_customer_name", anchor="center", width=60)
  orders_viewer.heading('order_customer_name', text = 'Name')

  orders_viewer.column("order_final_cost", anchor="center", width=55)
  orders_viewer.heading('order_final_cost', text = 'Total')

  orders_viewer.column("order_quantity", anchor="center", width=45)
  orders_viewer.heading('order_quantity', text = 'Amt')

  orders_viewer.grid(row = 1,column = 0)

  # insert values into orders_viewer
  for i in orders_data:
    orders_viewer.insert(parent = '', index = tk.END, values = i)



  root.mainloop()

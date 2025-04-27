import tkinter as tk
from tkinter import ttk # CC make treeview table via this
import database_handler

def run_GUI():
  root = tk.Tk()
  root.title("Test view")
  root.geometry("600x385")

  # setting style
  style=ttk.Style()
  style.theme_use('clam')

  # database viewer
  database_label = tk.Label(root,text = "Database Viewer", relief = "raised")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 90,
                     pady = 10
                     )

  inventory_data = database_handler.retrieve_via_sql_query("item_id,item_name,item_cost,item_final_cost,item_stock","inventory")

  database_viewer = ttk.Treeview(root, columns = ("item_id","item_name","item_cost","item_final_cost","item_stock"), show = 'headings', height = 15)
  database_viewer.grid(row = 1,
                       column = 0,
                       padx = 5,
                       sticky = "e"
                       )

  # creates the scrollbar
  scrollbar = ttk.Scrollbar(root, orient = "vertical", command = database_viewer.yview)
  scrollbar.grid(row = 1,
                 column = 1,
                 sticky="nswe"
                 )
  database_viewer.configure(yscrollcommand=scrollbar.set)

  # CC put in notebook
  # initialise columns
  database_viewer.column("item_id", anchor="center", width=40)
  database_viewer.heading('item_id', text = 'S.No')

  database_viewer.column("item_name", anchor="center", width=85)
  database_viewer.heading('item_name', text = 'Name')

  database_viewer.column("item_cost", anchor="center", width=55)
  database_viewer.heading('item_cost', text = 'Cost')

  database_viewer.column("item_final_cost", anchor="center", width=45)
  database_viewer.heading('item_final_cost', text = 'Total')

  database_viewer.column("item_stock", anchor="center", width=50)
  database_viewer.heading('item_stock', text = 'Stock')

  database_viewer.grid(row = 1,column = 0)

  # insert values into a database_viewer
  for i in inventory_data:
    database_viewer.insert(parent = '', index = tk.END, values = i)

  root.mainloop()

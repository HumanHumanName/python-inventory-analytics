import tkinter as tk
from tkinter import ttk # CC make treeview table via this
import database_handler

def run_GUI():
  root = tk.Tk()
  root.title("Test view")
  root.geometry("690x400")

  # Setting style
  style=ttk.Style()
  style.theme_use('clam')

  # database viewer
  database_label = tk.Label(root,text = "Database Viewer", relief = "raised")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 100,
                     pady = 10,
                     )

  inventory_data = database_handler.retrieve_via_sql_query("*","inventory")

  database_viewer = ttk.Treeview(root, columns = ("item_id","item_name","item_cost","item_gst","item_discount","item_final_cost","item_margin","item_stock","item_manufacturer_name","item_manufacturer_incharge","item_manufacturer_contact_no"), show = 'headings')
  # CC TRIM COLUMS!!!! and put in notebook
  # initialise columns
  database_viewer.column("item_id", anchor="center", width=40)
  database_viewer.heading('item_id', text = 'S.No')

  database_viewer.column("item_name", anchor="center", width=85)
  database_viewer.heading('item_name', text = 'Name')

  database_viewer.column("item_cost", anchor="center", width=55)
  database_viewer.heading('item_cost', text = 'Cost')

  database_viewer.column("item_gst", anchor="center", width=45)
  database_viewer.heading('item_gst', text = 'GST')

  database_viewer.column("item_discount", anchor="center", width=40)
  database_viewer.heading('item_discount', text = '%off')

  database_viewer.column("item_final_cost", anchor="center", width=45)
  database_viewer.heading('item_final_cost', text = 'total')

  database_viewer.column("item_margin", anchor="center", width=60)
  database_viewer.heading('item_margin', text = 'margin')

  database_viewer.column("item_stock", anchor="center", width=50)
  database_viewer.heading('item_stock', text = 'stock')

  database_viewer.column("item_manufacturer_name", anchor="center", width=85)
  database_viewer.heading('item_manufacturer_name', text = 'M. Name')

  database_viewer.column("item_manufacturer_incharge", anchor="center", width=90)
  database_viewer.heading('item_manufacturer_incharge', text = 'M. Incharge')

  database_viewer.column("item_manufacturer_contact_no", anchor="center", width=90)
  database_viewer.heading('item_manufacturer_contact_no', text = 'M. Contact')

  database_viewer.grid(row = 1,column = 0)

  # insert values into a database_viewer
  for i in inventory_data:
    database_viewer.insert(parent = '', index = tk.END, values = i)

  root.mainloop()

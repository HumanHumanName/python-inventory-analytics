import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from numpy import genfromtxt
import database_handler

def run_GUI():
  root = tk.Tk()
  root.title("Home view")
  root.geometry("600x385")
  root.resizable(False, False)

  # setting style
  style=ttk.Style()
  style.theme_use('clam')

  database_label = tk.Label(root,text = "▭▭▬▣▓ ▒ ░ Database Viewer ░ ▒ ▓▣▬▭▭", relief = "ridge", font = "TkFixedFont")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 10,
                     pady = 10,
                     sticky = "nesw"
                     )

  other_functions_label = tk.Label(root, text = ' ▭▣▓ ▒ ▒ Other Functions ▒ ▒ ▓▣▭ ', relief = "ridge", font = "TkFixedFont")
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

  #CC insure the ordering of the properties in tk brackets is consitant
  first_row_frame = tk.Frame(button_frame)
  first_row_frame.grid(row = 0,
                       columnspan = 3,
                       sticky = "nsew"
                       )

  # Each column must take equal amount of space
  first_row_frame.columnconfigure(0, weight=1)
  first_row_frame.columnconfigure(1, weight=1)
  first_row_frame.columnconfigure(2, weight=1)

  modelling_view_button = tk.Button(first_row_frame,
                                    text = "▰▱▰▱▰▰▱▰\n 📊 Modelling \n Viewport \n ▰▱▰▱▰▰▱▰",
                                    font = "TkSmallCaptionFont",
                                    height = 5,
                                    width = 10
                                    )

  modelling_view_button.grid(row = 0,
                            column = 0,
                            pady = 5
                            )

  refresh_database_button = tk.Button(first_row_frame,
                                     text = "▰▱▰▱▰ \n ↻ Refresh \n  Database \n ▰▱▰▱▰",
                                     font = "TkSmallCaptionFont",
                                     height = 5,
                                     width = 6,
                                     )

  refresh_database_button.grid(row = 0,
                              column = 1,
                              pady = 5
                             )


  full_inventory_path = tk.StringVar()
  full_orders_path = tk.StringVar()
  def import_database():
    # CC Note that this works, just have to refresh the notebook
    if full_inventory_path.get() != "" and full_orders_path.get() != "":
      items = genfromtxt(full_inventory_path.get(), delimiter = ",", dtype = None, skip_header = 1, encoding = "utf8")
      database_handler.initialise_new_items(items)

      orders = genfromtxt(full_orders_path.get(), delimiter = ",", dtype = None, skip_header = 1, encoding = "utf8")
      database_handler.initialise_new_orders(orders)


  import_database_button = tk.Button(first_row_frame,
                                    text = "▰▱▰▱▰ \n 🗎 Import \n Database \n ▰▱▰▱▰",
                                    font = "TkSmallCaptionFont",
                                    command = import_database,
                                    height = 5,
                                    width = 6,
                                    )

  import_database_button.grid(row = 0,
                             column = 2,
                             pady = 5
                             )

  def set_inventory_path():
    full_inventory_path.set(tk.filedialog.askopenfilename())
    temp = full_inventory_path.get()
    inventory_path.set("Inventory path: \n" + temp[:20] + "...")

  inventory_path = tk.StringVar()
  inventory_path_button = tk.Button(button_frame,
                                    textvariable = inventory_path,
                                    font = "TkFixedFont",
                                    command = set_inventory_path,
                                    height = 3
                                    )
  inventory_path.set("Set inventory path")

  inventory_path_button.grid(row = 1,
                            columnspan = 3,
                            sticky = "nsew"
  )

  def set_orders_path():
    full_orders_path.set(tk.filedialog.askopenfilename())
    temp = full_inventory_path.get()
    orders_path.set("Orders path: \n" + temp[:20] + "...")

  orders_path = tk.StringVar()
  orders_path_button = tk.Button(button_frame,
                                textvariable = orders_path,
                                font = "TkFixedFont",
                                command = set_orders_path,
                                height = 3
                                )
  orders_path.set("Set orders path")

  orders_path_button.grid(row = 2,
                          columnspan = 3,
                          sticky = "nsew"
  )

  spacer = tk.Label(button_frame, relief = "raised")
  spacer.grid(row = 3,
              columnspan = 3,
              sticky = "nsew")

  exit_button = tk.Button(button_frame,
                          text = "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \nQuit Python-Inventory-Analytics\n ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱",
                          font = "TkFixedFont",
                          command = root.destroy,
                          height = 2
                          )
  exit_button.grid(row = 4,
                   columnspan = 3,
                   sticky = "ew"
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

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from numpy import genfromtxt
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Treeview
import database_handler

def run_GUI():
  # root window definitions
  root = tk.Tk()
  root.title("Python Inventory Analytics")
  root.geometry("660x365")
  root.resizable(False, False)

  home_view = tk.Frame(root)
  home_view.grid(row=1, column=1, sticky='news')

  modelling_view = tk.Frame(root)
  modelling_view.grid(row=1, column=1, sticky='news') # CC adjust the row and columns later


  # setting style
  style = Style("solar")
  # style=ttk.Style() # DEBUG
  # style.theme_use('clam') # DEBUG

  # functions
  def populate_data():
   # removing response message if any
   response_message.set("")

   # inventory viewer
   inventory_data = database_handler.retrieve_via_sql_query("item_id,item_name,item_cost,item_final_cost,item_stock","inventory")

   inventory_viewer = Treeview(inventory_tab,
                                   columns = ("item_id","item_name","item_cost","item_final_cost","item_stock"),
                                   show = 'headings',
                                   height = 13,
                                   bootstyle='success'
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
   inventory_viewer.column("item_id", anchor="center", width=45)
   inventory_viewer.heading('item_id', text = 'S.No')

   inventory_viewer.column("item_name", anchor="center", width=75)
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

   orders_viewer = Treeview(orders_tab,
                               columns = ("order_id","order_item_name","order_customer_name","order_final_cost","order_quantity"),
                               show = 'headings',
                               height = 13,
                               bootstyle='success'
                               )
   orders_viewer.grid(row = 1,
                        column = 0,
                        sticky = "e"
                        )

   # creating the scrollbar
   scrollbar = ttk.Scrollbar(orders_tab, orient = "vertical", command = orders_viewer.yview)
   scrollbar.grid(row = 1,
                  column = 1,
                  sticky="nsew"
                  )
   orders_viewer.configure(yscrollcommand=scrollbar.set)

   # initialising columns
   orders_viewer.column("order_id", anchor="center", width=45)
   orders_viewer.heading('order_id', text = 'S.No')

   orders_viewer.column("order_item_name", anchor="center", width=75)
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

  def import_database():
    if full_inventory_path.get() != "" and full_orders_path.get() != "":
      items = genfromtxt(full_inventory_path.get(), delimiter = ",", dtype = None, skip_header = 1, encoding = "utf8")
      database_handler.import_items(items)

      orders = genfromtxt(full_orders_path.get(), delimiter = ",", dtype = None, skip_header = 1, encoding = "utf8")
      database_handler.import_orders(orders)

      response_message.set("Import Successful; Please Refresh")
      spacer.config(fg = "green")
    else:
      response_message.set("Import Unsuccessful; Please try again")
      spacer.config(fg = "red")

  def set_inventory_path():
    full_inventory_path.set(tk.filedialog.askopenfilename())
    temp = full_inventory_path.get()
    inventory_path.set("Inventory path: \n" + temp[:20] + "...")

  def set_orders_path():
    full_orders_path.set(tk.filedialog.askopenfilename())
    temp = full_inventory_path.get()
    orders_path.set("Orders path: \n" + temp[:20] + "...")

  def switch_to_modelling_view():
    modelling_view.tkraise()

  # home view GUI
  database_label = tk.Label(home_view,text = "▭▭▪▣▓ ▒ ░ Database Viewer ░ ▒ ▓▣▪▭▭", relief = "ridge", font = "TkFixedFont")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 10,
                     pady = 10,
                     sticky = "nesw"
                     )

  other_functions_label = tk.Label(home_view, text = ' ▭▣▓ ▒ ▒ Other Functions ▒ ▒ ▓▣▭ ', relief = "ridge", font = "TkFixedFont")
  other_functions_label.grid(row = 0,
                            column = 1,
                            sticky = "ew"
                            )

  button_frame = tk.Frame(home_view)
  button_frame.grid(row = 1,
                    column = 1,
                    sticky = "nsew"
                    )

  #CC insure the ordering of the properties in tk brackets is consitant
  first_row_frame = tk.Frame(button_frame)
  first_row_frame.grid(row = 0,
                       columnspan = 3,
                       pady = 5,
                       sticky = "nsew"
                       )

  # Each column must take equal amount of space
  # CC check if this actually like.. does anything (in the one before notebook too)
  first_row_frame.columnconfigure(0, weight=1)
  first_row_frame.columnconfigure(1, weight=1)
  first_row_frame.columnconfigure(2, weight=1)

  # CC fix formating (tabs)
  modelling_view_button = Button(first_row_frame,
                                    text = "▰▱▰▱▰▰▱▰\n 📊 Modelling \n Viewport \n ▰▱▰▱▰▰▱▰",
                                    command = switch_to_modelling_view,
                                    bootstyle="primary-outline"
                                    )

  modelling_view_button.grid(row = 0,
                            column = 0,
                            pady = 5,
                            sticky = "e"
                            )

  refresh_database_button = Button(first_row_frame,
                                     text = "▰▱▰▱▰▰▱▰ \n ↻ Refresh \n  Database \n ▰▱▰▱▰▰▱▰",
                                     command = populate_data,
                                     bootstyle="warning-outline"
                                     )

  refresh_database_button.grid(row = 0,
                              column = 1,
                              pady = 5,
                              padx = 5,
                              sticky = "nsew"
                             )


  full_inventory_path = tk.StringVar()
  full_orders_path = tk.StringVar()

  import_database_button = Button(first_row_frame,
                                    text = "▰▱▰▱▰▰▱▰ \n 🗎 Import \n Database \n ▰▱▰▱▰▰▱▰",
                                    command = import_database,
                                    bootstyle="success-outline"
                                    )

  import_database_button.grid(row = 0,
                             column = 2
                             )

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

  response_message = tk.StringVar()
  spacer = tk.Label(button_frame,textvariable = response_message, relief = "raised")
  spacer.grid(row = 3,
              columnspan = 3,
              pady = 5,
              sticky = "nsew")
  response_message.set("")

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
  table_frame = tk.Frame(home_view)
  table_frame.grid(row = 1,
                  column = 0,
                  sticky = "nsew"
                  )

  # Each column must take equal amount of space
  table_frame.rowconfigure(0, weight=1)
  table_frame.rowconfigure(1, weight=1)
  table_frame.rowconfigure(2, weight=1)

  tables_notebook = ttk.Notebook(table_frame)
  tables_notebook.grid(row = 1,
                       padx = 10
                       )

  inventory_tab= ttk.Frame(tables_notebook)
  tables_notebook.add(inventory_tab, text= "    Inventory    ")

  orders_tab= ttk.Frame(tables_notebook)
  tables_notebook.add(orders_tab, text= "    Orders    ")

  populate_data()

  # Sets initial frame to be home_view
  home_view.tkraise()

  root.mainloop()

import tkinter as tk
from tkinter import ttk # CC make treeview table via this

def run_GUI():
  root = tk.Tk()
  root.title("Test view")
  root.geometry("600x400")
  root.resizable(False, False)

  database_label = tk.Label(root,text = "Database Viewer", relief = "raised")
  database_label.grid(row = 0,
                     column = 0,
                     padx = 100,
                     pady = 10,
                     )

  root.mainloop()

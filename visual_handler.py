import tkinter as tk

def run_GUI():
  root = tk.Tk()
  root.title("Test view")
  root.geometry("500x300")
  frame = tk.Frame(root)
  frame.grid(row=10,column = 10)
  tk.Label(frame, text='Hello World!').grid(row = 0, column = 0)
  tk.Label(frame, text='Hello World!').grid(row = 1, column = 1)

  root.mainloop()

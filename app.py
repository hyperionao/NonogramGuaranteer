import tkinter as tk 
from tkinter import ttk 
from main import *


def submit():
    selected_length = row_length.get()
    runs_string = runs.get()
    
    
    
    

root = tk.Tk()
root.geometry("500x300")
ttk.Label(root, text="Hello, Tkinter!").pack()

ttk.Label(root, text="Give the row/column length you are dealing with!").pack()
row_length = tk.StringVar()
row_choices = ttk.Combobox(root, width = 27, textvariable = row_length)
row_choices['values'] = (
    5, 
    10, 
    15, 
    20, 
    25
)

row_choices.pack()
row_choices.current(1) 


ttk.Label(root, text="Give the runs as shown above/aside the row/column! \nFormat should be as a continuous string: 4 5").pack()
runs = ttk.Entry()
runs.pack()

MyButton = ttk.Button(root, text='Submit!', width=10, command=submit)
MyButton.pack()

root.mainloop()

import tkinter as tk
from tkinter import ttk
from nonogram_guarantee import process_input, nonogram_logic  



def submit():
    length = row_length.get()
    runs = run_input.get()

    length, runs_list = process_input(length, runs)
    if length is None or runs_list is None:
        result_label.config(text="Invalid input. Please try again.")
        return

    result = nonogram_logic(length, runs_list)
    result_label.config(text=result)

root = tk.Tk()
root.title("Nonogram Guaranteer")
root.geometry("700x300")

style = ttk.Style()
style.configure("TLabel", font=("Comic Sans MS", 10))

ttk.Label(root, text="Row/Column Length:").pack(pady=4)
row_length = tk.StringVar()
row_choices = ttk.Combobox(root, width=27, textvariable=row_length, state="readonly")
row_choices['values'] = (5, 10, 15, 20, 25)
row_choices.pack(pady=6)
row_choices.current(1)

ttk.Label(root, text="Please input runs! (e.g., '4 5'):").pack()
run_input = tk.Entry(root, width=30)
run_input.pack(pady=6)

submit_button = ttk.Button(root, text="Submit!", command=submit)
submit_button.pack(pady=8)

result_label = ttk.Label(root, text="", justify="center")
result_label.pack()

footer = ttk.Label(root, text="this is a #aaronclassic | version 1.0", font=("Comic Sans MS", 10))
footer.pack(side="bottom", pady=10)

root.mainloop()

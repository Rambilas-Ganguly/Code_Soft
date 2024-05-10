import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def add_to_entry(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_bg = "orange"
button_active_bg = "#d0d0d0"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('00', 4, 2), ('+', 4, 3), 
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12),
                       bg=button_bg, activebackground=button_active_bg,
                       command=lambda text=text: add_to_entry(text))
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", width=5, height=2, font=('Arial', 12),
                         bg="red", activebackground=button_active_bg,
                         command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="=", width=5, height=2, font=('Arial', 12),
                             bg="green", activebackground=button_active_bg,
                             command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()

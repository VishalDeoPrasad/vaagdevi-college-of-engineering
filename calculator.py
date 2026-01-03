import tkinter as tk

def on_click(button_text):
    expression.set(expression.get() + button_text)

def clear():
    expression.set("")

def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except:
        expression.set("Error")

root = tk.Tk()
root.title("Calculator")

expression = tk.StringVar()
entry = tk.Entry(root, textvariable=expression, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for text, row, col in buttons:
    tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
command=lambda t=text: on_click(t) if t != "=" else calculate()).grid(row=row, column=col)

tk.Button(root, text="C", font=("Arial", 18), width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()

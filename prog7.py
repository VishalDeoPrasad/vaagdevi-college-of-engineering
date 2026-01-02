import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")

def login():
    username = e1.get()
    password = e2.get()
    messagebox.showinfo("Login", f"Welcome, {username}")

l1 = tk.Label(root, text="Username:")
l1.grid(row=0, column=0, padx=10, pady=10)

e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=10)

l2 = tk.Label(root, text="Password:")
l2.grid(row=1, column=0, padx=10, pady=10)

e2 = tk.Entry(root)
e2.grid(row=1, column=1, padx=10, pady=10)

b1 = tk.Button(root, text="Login", command=login)
b1.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x300")

def call():
    messagebox.showinfo("hi", "Hello World")

button = tk.Button(root, 
                   text="Click me", 
                   command=call, 
                   font=("Arial", 12), 
                   bg="blue", 
                   fg="white")
button.pack()

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
l1 = tk.Label(root, text="Username:")
l1.grid(row=0, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1 )

root.mainloop()
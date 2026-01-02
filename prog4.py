import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
l1 = tk.Label(root, text="Username:")
l1.pack(side="left")

e1 = tk.Entry(root)
e1.pack(side="right")

root.mainloop()
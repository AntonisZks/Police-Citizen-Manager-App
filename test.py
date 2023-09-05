import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Canvas X-Fill Example")

canvas = tk.Canvas(root, bg="red")
canvas.pack()

label = ttk.Label(canvas, background='blue', width=canvas.winfo_reqwidth())
canvas.create_window((0, 0), window=label, anchor=tk.NW)

button_gap = 10
button_width = (label.winfo_width() - 2*button_gap)
button = tk.Button(label, text="Press me", width=button_width)
button.place(x=button_gap, y=button_gap)

root.mainloop()

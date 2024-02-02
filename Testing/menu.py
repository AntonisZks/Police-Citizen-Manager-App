import tkinter as tk
from tkinter import Menu


def open_file():
	print("Open file")


def save_file():
	print("Save file")


def exit_app():
	root.quit()


root = tk.Tk()
root.title("Tkinter Menu Example")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

root.mainloop()

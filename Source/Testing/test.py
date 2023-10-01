import tkinter as tk


def openWindow():
	window2 = tk.Toplevel(window1)
	print("inside window 2")
	window2.mainloop()


window1 = tk.Tk()
window1.title("Window 1")

button = tk.Button(window1, text="Press me", command=openWindow)
button.pack()

print("Inside window 1")
window1.mainloop()

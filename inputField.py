import tkinter as tk
from initialization import *

class InputField:

    SEARCH_ICON_PATH = SEARCH_LOGO_IMAGE_PATH_

    def __init__(self, parent, font, fg, border_width, default_text, command=None):
        self.parent = parent
        self.font = font
        self.fg = fg
        self.border_width = border_width
        self.default_text = default_text
        self.command = command
        self.search_icon_image = tk.PhotoImage(file=self.SEARCH_ICON_PATH)
        self.search_image = resizeImage(self.search_icon_image, int((22.5/10)*self.font[1]))

    def focus_in(self, event, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            self.fg = 'black'
            entry.config(fg=self.fg)
    
    def focus_out(self, event, entry, default_text):
        if entry.get() == "":
            entry.insert(0, self.default_text)
            self.fg = 'gray'
            entry.config(fg=self.fg)

    def create(self):
        # creating the Entry Box
        self.entry_box = tk.Entry(self.parent, fg=self.fg, font=self.font, borderwidth=self.border_width)
        self.entry_box.insert(0, self.default_text)
        self.entry_box.bind("<FocusIn>", lambda event: self.focus_in(event, self.entry_box, self.default_text))
        self.entry_box.bind("<FocusOut>", lambda event: self.focus_out(event, self.entry_box, self.default_text))
        self.entry_box.bind('<Return>', lambda e: self.command())

        # Creating the Search Button
        self.search_button = tk.Button(self.parent, text="Search", image=self.search_image, command=self.command)

    def put(self):
        self.entry_box.grid(row=0, column=0)
        self.search_button.grid(row=0, column=1)
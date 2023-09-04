import tkinter as tk
from support import *

class SearchBar:
    def __init__(self, parent_widget: tk.Frame, app_data: dict[str, any], width: int, height: int, border_width: int, place_holder: str, font: tuple) -> None:
        self.parent_widget = parent_widget
        self.application_data = app_data
        self.width = width
        self.height = height
        self.border_width = border_width
        self.place_holder = place_holder
        self.font = font

        # Initialize some usefull images
        self.search_logo_image = tk.PhotoImage(file=SEARCH_PNG_PATH)

    def __focus_in(self, event, entry, place_holder):
        if entry.get() == place_holder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def __focus_out(self, event, entry, place_holder):
        if entry.get() == "":
            entry.insert(0, self.place_holder)
            entry.config(fg='gray')

    def build(self) -> None:
        # Creating the entry box
        self.entry = tk.Entry(self.parent_widget, fg="gray", font=self.font, borderwidth=self.border_width)
        self.entry.insert(0, self.place_holder)
        self.entry.bind("<FocusIn>", lambda event: self.__focus_in(event, self.entry, self.place_holder))
        self.entry.bind("<FocusOut>", lambda event: self.__focus_out(event, self.entry, self.place_holder))
        self.entry.bind('<Return>', lambda event: self.command())

        # Creating the search button
        self.search_image = resizeImage(self.search_logo_image, round(2*self.font[1]))
        self.search_button = tk.Button(self.parent_widget, text="Search", image=self.search_image)

    def put(self):
        self.entry.grid(row=0, column=0)
        self.search_button.grid(row=0, column=1)

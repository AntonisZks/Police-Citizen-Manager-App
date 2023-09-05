import tkinter as tk
from support import *

class SearchBar:
    """
    The SearchBar class represents a search bar widget that can be used to enter search queries.

    Attributes:
        parent_widget (tk.Frame): The parent widget where the search bar will be placed.
        application_data (dict): Data related to the application.
        border_width (int): The width of the search bar's border.
        place_holder (str): The placeholder text displayed in the search bar when it's empty.
        font (tuple): The font configuration for the text in the search bar.
        search_logo_image (PhotoImage): An image for the search button.

    Methods:
        __focus_in(event, entry, place_holder): Event handler for when the search bar gains focus.
        __focus_out(event, entry, place_holder): Event handler for when the search bar loses focus.
        build(): Builds the search bar and associated search button.
        put(): Places the search bar and search button within the parent widget.
    """

    def __init__(self, parent_widget: tk.Frame, app_data: dict[str, any], border_width: int, place_holder: str, font: tuple, command: callable) -> None:
        """
        Constructor for the SearchBar class.

        Args:
            parent_widget (tk.Frame): The parent widget where the search bar will be placed.
            app_data (dict): Data related to the application.
            border_width (int): The width of the search bar's border.
            place_holder (str): The placeholder text displayed in the search bar when it's empty.
            font (tuple): The font configuration for the text in the search bar.
            command (function): The function that is about to be called when the search button is pressed.
        """
        self.parent_widget = parent_widget
        self.application_data = app_data
        self.border_width = border_width
        self.place_holder = place_holder
        self.font = font
        self.command = command

        # Initialize some useful images
        self.search_logo_image = tk.PhotoImage(file=SEARCH_PNG_PATH)

    def __focusIn(self, event, entry, place_holder) -> None:
        """
        Event handler for when the search bar gains focus.

        Args:
            event: The focus-in event.
            entry (tk.Entry): The search bar entry widget.
            place_holder (str): The placeholder text displayed in the search bar.
        """
        if entry.get() == place_holder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def __focusOut(self, event, entry, place_holder) -> None:
        """
        Event handler for when the search bar loses focus.

        Args:
            event: The focus-out event.
            entry (tk.Entry): The search bar entry widget.
            place_holder (str): The placeholder text displayed in the search bar.
        """
        if entry.get() == "":
            entry.insert(0, self.place_holder)
            entry.config(fg='gray')

    def getItem(self):
        return self.entry.get()

    def build(self) -> None:
        """
        Build the search bar and associated search button.
        """
        # Creating the entry box
        self.entry = tk.Entry(self.parent_widget, fg="gray", font=self.font, borderwidth=self.border_width)
        self.entry.insert(0, self.place_holder)
        self.entry.bind("<FocusIn>", lambda event: self.__focusIn(event, self.entry, self.place_holder))
        self.entry.bind("<FocusOut>", lambda event: self.__focusOut(event, self.entry, self.place_holder))
        self.entry.bind('<Return>', lambda event: self.command())

        # Creating the search button
        self.search_image = resizeImage(self.search_logo_image, round(2*self.font[1]))
        self.search_button = tk.Button(self.parent_widget, text="Search", image=self.search_image, command=self.command)

    def put(self):
        """
        Place the search bar and search button within the parent widget.
        """
        self.entry.grid(row=0, column=0)
        self.search_button.grid(row=0, column=1)

"""
The 'searchBar.py' file contains the SearchBar class, which represents a basic search bar. It is mostly being used in the 'searchFrame.py' and in the 'updateFrame.py'
files where they allow the user to enter the input and get the appropriate output. The search bar consists of two elements. An entry box where the input is being written,
and a button which is used to execute the search process.

"""

import tkinter as tk
from Extras.support import *


class SearchBar:
    """ The SearchBar class represents a search bar widget that can be used to enter search queries.

    Attributes:
        parentWidget (tk.Frame): The parent widget where the search bar will be placed.
        applicationSettings (dict): Data related to the application.
        borderWidth (int): The width of the search bar's border.
        placeHolder (str): The placeholder text displayed in the search bar when it's empty.
        font (tuple): The font configuration for the text in the search bar.
        searchLogoImage (PhotoImage): An image for the search button.

    Methods:
        __focus_in(event, entry, place_holder): Event handler for when the search bar gains focus.
        __focus_out(event, entry, place_holder): Event handler for when the search bar loses focus.
        build(): Builds the search bar and associated search button.
        put(): Places the search bar and search button within the parent widget.

    """

    def __init__(self, parentWidget: tk.Widget, applicationSettings: dict[str, any], width: int, borderWidth: int, placeHolder: str, font: tuple, command: callable) -> None:
        """ Constructor for the SearchBar class. the search bar widget consists of two elements, an entry box and a button. Each one has its own characteristics.
            The entry box has a width, a border width, a font and a placeholder. The button has a width, an image and a command to execute when it is clicked.

        Args:
            parentWidget (tk.Frame): The parent widget where the search bar will be placed.
            applicationSettings (dict): Settings related to the application.
            borderWidth (int): The width of the search bar's border.
            placeHolder (str): The placeholder text displayed in the search bar when it's empty.
            font (tuple): The font configuration for the text in the search bar.
            command (function): The function that is about to be called when the search button is pressed.

        """

        self.searchButton = None  # Temporary initialization of the search button
        self.searchImage = None   # Temporary initialization of the search image
        self.entry = None         # Temporary initialization of the entry box

        self.parentWidget = parentWidget                # The parent widget containing the search bar
        self.applicationSettings = applicationSettings  # The settings of the application
        self.width = width                              # the width of the search bar
        self.borderWidth = borderWidth                  # The border width of the entry box
        self.placeHolder = placeHolder                  # The placeholder of the entry box
        self.font = font                                # The font of the entry box
        self.command = command                          # The command to be executed when the button is clicked

        # Initialize some useful images
        self.searchLogoImage = tk.PhotoImage(file=SEARCH_PNG_PATH)

    @staticmethod
    def __focusIn(entry: tk.Entry, placeHolder: str) -> None:
        """ Event handler for when the search bar gains focus.

        Args:
            entry (tk.Entry): The search bar entry widget.
            placeHolder (str): The placeholder text displayed in the search bar.

        """

        # Delete the placeholder of the search bar and change the text color to black
        if entry.get() == placeHolder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def __focusOut(self, entry: tk.Entry) -> None:
        """ Event handler for when the search bar loses focus.

        Args:
            entry (tk.Entry): The search bar entry widget.

        """

        # Fill the entry with its placeholder and turn the text color to grey
        if entry.get() == "":
            entry.insert(0, self.placeHolder)
            entry.config(fg='gray')

    def getItem(self) -> str:
        """ Returns the stored value inside the entry box, as a string """

        return self.entry.get()

    def build(self) -> None:
        """ Builds the search bar and associates the search button. """

        # Creating the entry box
        self.entry = tk.Entry(self.parentWidget, fg="gray", font=self.font, borderwidth=self.borderWidth, width=self.width)
        self.entry.insert(0, self.placeHolder)

        # Binding the entry with some additional options
        self.entry.bind("<FocusIn>", lambda event: self.__focusIn(self.entry, self.placeHolder))  # Binding with focusing in
        self.entry.bind("<FocusOut>", lambda event: self.__focusOut(self.entry))                  # Binding with focusing out
        self.entry.bind('<Return>', lambda event: self.command())                                 # Binding with the 'Return' key on the keyboard

        # Creating the search button
        self.searchImage = resizeImage(self.searchLogoImage, round(2 * self.font[1]))
        self.searchButton = tk.Button(self.parentWidget, text="Search", image=self.searchImage, command=self.command)

    def put(self):
        """ Places the search bar and search button within the parent widget. """

        self.entry.grid(row=0, column=0)         # Placing the entry on the left
        self.searchButton.grid(row=0, column=1)  # Placing the entry on the right

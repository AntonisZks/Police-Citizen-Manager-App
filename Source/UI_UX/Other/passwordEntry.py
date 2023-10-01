"""
The 'passwordEntry.py' file contains the PasswordEntry class, which represents a password entry widget. Specifically it is an entry with a button next to it, just like the search bar, but
this time the user is typing a password inside it, and they have the option to keep the text hidden or not. This can be done by the button next to the entry.

"""

from Source.Extras.support import *


class PasswordEntry:
    def __init__(self, parentWidget: tk.Widget, applicationSettings: dict[str, any], width: int, borderWidth: int, font: tuple, command: callable) -> None:
        """ The constructor of the Password Entry. Here all the necessary attributes are initialized.

        Args:
            parentWidget: The widget that contains the password entry
            applicationSettings: The settings of the application
            width: The width of the entry
            borderWidth: The border width of the entry
            font: The font of the entry
            command: The command to be executed when the user presses the 'Return' button on keyboad while typing

        """
        self.view = False           # A variable that keeps the current state of the hide-view button (Hide or View)
        self.hideViewButton = None  # Temporary initialization of the hide-view button
        self.hideImage = None       # Temporary initialization of the hide image
        self.viewImage = None       # Temporary initialization of the view image
        self.entry = None           # Temporary initialization of the entry box

        self.parentWidget = parentWidget                # The parent widget containing the search bar
        self.applicationSettings = applicationSettings  # The settings of the application
        self.width = width                              # the width of the search bar
        self.borderWidth = borderWidth                  # The border width of the entry box
        self.font = font                                # The font of the entry box
        self.command = command                          # The command to be executed when the button is clicked

        # Initialize some useful images
        self.hideLogoImage = tk.PhotoImage(file=HIDE_PNG_PATH)
        self.viewLogoImage = tk.PhotoImage(file=VIEW_PNG_PATH)

    def __changeState(self) -> None:
        """ Changes the state of the password entry (Hide or View). """

        # If the current state is set to 'View' then change it to 'Hide'
        if self.view:
            self.entry['show'] = '*'                       # Setting the entry text to be '*'
            self.hideViewButton['image'] = self.hideImage  # Changing the button image
            self.view = False                              # Updating the state

        # If it is set to 'Hide' change it to 'View'
        else:
            self.entry['show'] = ''                        # Setting the entry text to be normal characters
            self.hideViewButton['image'] = self.viewImage  # Changing the button image
            self.view = True                               # Updating the state

    def getItem(self) -> str:
        """ Returns the current text value of the entry. """

        return self.entry.get()

    def build(self) -> None:
        """ Builds the password entry widget. """

        # Creating the entry box
        self.entry = tk.Entry(self.parentWidget, font=self.font, borderwidth=self.borderWidth, width=self.width)
        self.entry['show'] = '*'
        self.view = False

        # Binding the entry with some additional options
        self.entry.bind('<Return>', lambda event: self.command())  # Binding with the 'Return' key on the keyboard

        # Creating the search button
        self.viewImage = resizeImage(self.viewLogoImage, round(2 * self.font[1]))
        self.hideImage = resizeImage(self.hideLogoImage, round(2 * self.font[1]))
        self.hideViewButton = tk.Button(self.parentWidget, text="", image=self.hideImage, command=self.__changeState)

        self.entry.focus()  # Focuses on the entry

        self.entry.grid(row=0, column=0)  # Placing the entry on the left
        self.hideViewButton.grid(row=0, column=1)  # Placing the entry on the right

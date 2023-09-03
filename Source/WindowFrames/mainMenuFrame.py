"""
The 'mainMenuFrame.py' file contains the main class corresponding to the MainMenuFrame and its methods.
This frame is displayed after the user selects a database in the DatabasePickerFrame and serves as the main interface
for interacting with the selected database.

"""

import tkinter as tk
from support import *


def createNavigationButton(parent: tk.Tk, text: str, font: tuple, width: int, image: tk.PhotoImage, padx: int, pady: int) -> None:
    """
    The createNavigationButton() function creates a navigation button with text and an image according to its given properties.

    Args:
        parent (Tk): The parent widget.
        text (str): The text to display on the button.
        font (tuple): The font configuration for the button text.
        width (int): The width of the button.
        image (PhotoImage): The image to display on the button.
        padx (int): The horizontal padding of the button.
        pady (int): The vertical padding of the button.

    Returns:
        Button: The created navigation button.
    """
    new_button = tk.Button(parent, text=text, font=font, width=width, image=image, compound=tk.LEFT, padx=padx, pady=pady)
    return new_button


class MainMenuFrame:
    """
    The MainMenuFrame class represents the main menu frame of the application where the user can interact with the selected database.
    It provides a basic navigation menu with the followinf options: Search, Insert, Update.

    Attributes:
        parent_data (dict): The data of the parent widget. In this case, the parent widget is the main window.
        header_options (dict): Some useful options for the Header Frame.
        body_options (dict): Some useful options for the Body Frame.
        police_logo_image (PhotoImage): An image that is displayed on the main header label.
        change_logo_image (PhotoImage): An image for the 'Change File' button.
        search_logo_image (PhotoImage): An image for the search button.
        insert_logo_image (PhotoImage): An image for the insert button.
        update_logo_image (PhotoImage): An image for the update button.
        parent_widget (Tk): The parent widget of the frame, which is always the main window.
        frame (Frame): The actual frame.
        header (Frame): The header frame.
        header_image (PhotoImage): The image used in the header section as part of the main label.
        header_label (Label): The main label displayed on the header.
        body (Frame): The body frame.
        body_title_frame (Frame): A parent frame for the label and 'Change File' button.
        body_label_message (Label): The message displaying the active database.
        change_file_button (Button): The button to change the active database.
        nav_buttons_frame (Frame): A frame for navigation buttons (Search, Insert, Update).

    Methods:
        build(): Builds the actual frame.
        __initializeImages(): Initializes images used in the frame.
        __setupStructureOptions(data): Sets up options for the frame's structure.
        __buildStructure(): Builds the general structure of the frame (Header, Body).
        __createHeaderFrame(): Creates the Header Frame.
        __createBodyFrame(): Creates the Body Frame.
    """
    def __init__(self, data: dict[str, any]) -> None:
        """
        The constructor of the MainMenuFrame class. Here, the actual frame and the main structure
        are being built, while additional data such as images and options are being initialized.

        Args:
            data (dict[str, any]): The data of the parent widget.
        """
        # Creating the actual frame
        self.parent_widget = data['window']  # The parent widget is the main window
        self.frame = tk.Frame(self.parent_widget, bg=data['theme-color'])
        self.frame.pack()

        # Setup the header, body, and footer options and initialize the images used
        self.__setupStructureOptions(data)
        self.__initializeImages()

    def __initializeImages(self) -> None:
        """
        The __initializeImages() method initializes all the images used in the frame.
        """
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.change_logo_image = tk.PhotoImage(file=self.body_options['change-file-button-image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-image-path'])
        self.insert_logo_image = tk.PhotoImage(file=self.body_options['insert-image-path'])
        self.update_logo_image = tk.PhotoImage(file=self.body_options['update-image-path'])

    def __setupStructureOptions(self, data: dict[str, any]) -> None:
        """
        The __setupStructureOptions() initializes options for all the frame's components (Header, Body).

        Args:
            data (dict[str, any]): The data of the parent widget.
        """
        self.parent_data = data

        # Setting up the Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "message-title": f"ΕΝΕΡΓΟ ΑΡΧΕΙΟ:" + " "*10 + f"{getFileName(self.parent_data['app-data']['active-database'])}",
            "message-title-font": ('Arial', round(0.018*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold'),
            "buttons-font": ('Arial', round(0.011*max(self.parent_data['window-width'], self.parent_data['window-height']))),
            "change-file-button-text": "ΑΛΛΑΓΗ",
            "change-file-button-font": ('Arial', round(0.011*max(self.parent_data['window-width'], self.parent_data['window-height']))),
            "change-file-button-padx-outer": round(0.02*self.parent_data['window-width']),
            "change-file-button-padx-inner": round(0.01*self.parent_data['window-width']),
            "change-file-button-pady-inner": round(0.005*self.parent_data['window-height']),
            "change-file-button-image-path": CHANGE_PNG_PATH,
            "search-image-path": SEARCH_PNG_PATH,
            "insert-image-path": INSERT_PNG_PATH,
            "update-image-path": UPDATE_PNG_PATH,
            "navigation-button-width": round(0.4*self.parent_data['window-width']),
            "navigation-button-font": ('Arial', round(0.025*max(self.parent_data['window-width'], self.parent_data['window-height']))),
            "navigation-button-padx-inner": round(0.03*self.parent_data['window-width']),
            "navigation-button-pady-inner": round(0.012*self.parent_data['window-height']),
            "navigation-button-pady-outer": round(0.05*self.parent_data['window-height']),
            "search-button-text": "ΑΝΑΖΗΤΗΣΗ",
            "insert-button-text": "ΚΑΤΑΧΩΡΗΣΗ",
            "update-button-text": "  ΔΙΟΡΘΩΣΗ  "
        }

    def build(self) -> None:
        """The build() method builds the actual frame."""
        # Update the body message title so as to show the correct database the user is working on and build the structure
        self.body_options['message-title'] = f"ΕΝΕΡΓΟ ΑΡΧΕΙΟ:" + " "*10 + f"{getFileName(self.parent_data['app-data']['active-database'])}"
        self.__buildStructure()

    def __buildStructure(self) -> None:
        """The __buildStructure() method builds the general structure of the main menu frame (Header, Body)."""
        self.__createHeaderFrame()  # First create the header
        self.__createBodyFrame()  # Then create the body

    def __createHeaderFrame(self) -> None:
        """The __createHeaderFrame() method creates the Header Frame, which contains the main label and logo."""
        self.header = tk.Frame(self.frame, bg=self.parent_data['theme-color'])  # Creating the header frame

        # Creating the Header Label
        self.header_image = resizeImage(self.police_logo_image, round(0.13*self.parent_data['window-width']))
        self.header_label = tk.Label(
            self.header,
            text=self.header_options['title'],
            font=self.header_options['font'],
            bg=self.parent_data['theme-color'],
            fg=self.parent_data['label-fg-color'],
            image=self.header_image, compound=tk.LEFT,
            padx=round(0.04*self.parent_data['window-width']),
            pady=round(0.04*(self.parent_data['window-height']))
        )

        # Packing the header and its widgets
        self.header_label.pack()
        self.header.pack()

    def __createBodyFrame(self) -> None:
        """The __createBodyFrame() method creates the Body Frame, which contains the message label and navigation buttons."""
        self.body = tk.Frame(self.frame, bg=self.parent_data['theme-color'])  # Creating the body frame

        # Creating a parent frame that will hold the label and 'Change File' button
        self.body_title_frame = tk.Frame(self.frame, bg=self.parent_data['theme-color'])

        # Creating the body label message
        self.body_label_message = tk.Label(
            self.body_title_frame, text=self.body_options['message-title'],
            font=self.body_options['message-title-font'],
            bg=self.parent_data['theme-color'],
            fg=self.parent_data['label-fg-color']
        )

        # Creating the 'Change File' button
        self.change_file_image = resizeImage(self.change_logo_image, round(2*self.body_options['change-file-button-font'][1]))
        self.change_file_button = tk.Button(
            self.body_title_frame,
            text=self.body_options["change-file-button-text"],
            font=self.body_options["change-file-button-font"],
            image=self.change_file_image,
            compound=tk.LEFT,
            padx=self.body_options['change-file-button-padx-inner'],
            pady=self.body_options['change-file-button-pady-inner'],

        )

        # Creating the main navigation buttons (Search, Insert, Update)
        self.nav_buttons_frame = tk.Frame(self.frame, bg=self.parent_data['theme-color'])

        # Create the images used in the buttons
        self.search_image = resizeImage(self.search_logo_image, round(2*self.body_options['navigation-button-font'][1]))
        self.insert_image = resizeImage(self.insert_logo_image, round(2*self.body_options['navigation-button-font'][1]))
        self.update_image = resizeImage(self.update_logo_image, round(2*self.body_options['navigation-button-font'][1]))

        images = [self.search_image, self.insert_image, self.update_image]
        images_texts = ["search", "insert", "update"]
        buttons = []

        # Creating each button with a 'fancy' way
        for image in zip(images, images_texts):
            new_button = createNavigationButton(
                self.nav_buttons_frame,
                self.body_options[f'{image[1]}-button-text'],
                self.body_options['navigation-button-font'],
                self.body_options['navigation-button-width'],
                image[0],
                self.body_options['navigation-button-padx-inner'],
                self.body_options['navigation-button-pady-inner'],
            )
            buttons.append(new_button)

        # Packing the body and its widgets
        self.body_label_message.grid(row=0, column=0)
        self.change_file_button.grid(row=0, column=1, padx=self.body_options['change-file-button-padx-outer'])
        self.body_title_frame.pack()
        for button in buttons:
            button.pack(pady=self.body_options['navigation-button-pady-outer'])
        self.nav_buttons_frame.pack()
        self.body.pack()

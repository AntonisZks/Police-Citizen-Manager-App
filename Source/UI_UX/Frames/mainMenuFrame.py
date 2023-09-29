"""
The 'mainMenuFrame.py' file contains the main class corresponding to the MainMenuFrame and its methods. This frame is displayed after the user
selects a database in the DatabasePickerFrame and serves as the main interface for interacting with the selected database. The frame contains
the three general options of the application, which are 'Search', 'Insert' and 'Update'. These 3 options are displayed as buttons on the user's
computer screen and provide the suitable functionality for the user. It also provides a quick message to the user about what database they are using
at Any moment and also the option to change it if the want, by navigating back to the databasePickerFrame and choose another database to work with.
"""

import json
from Source.Extras.support import *
from Source.UI_UX.Frames.frame import IFrame


def createNavigationButton(parent: tk.Widget, text: str, font: tuple, width: int, image: tk.PhotoImage, pad_x: int, pad_y: int, command: callable) -> tk.Button:
    """ Creates a navigation button with text and an image according to its given properties.

    Args:
        parent (Tk): The parent widget.
        text (str): The text to display on the button.
        font (tuple): The font configuration for the button text.
        width (int): The width of the button.
        image (PhotoImage): The image to display on the button.
        pad_x (int): The horizontal padding of the button.
        pad_y (int): The vertical padding of the button.
        command (callable): The function to be called when the button is clicked.

    Returns:
        Button: The created navigation button.
    """
    new_button = tk.Button(parent, text=text, font=font, width=width, image=image, compound=tk.LEFT, padx=pad_x, pady=pad_y, command=command)
    return new_button


class MainMenuFrame(IFrame):
    """ The MainMenuFrame class represents the main menu frame of the application where the user can interact with the selected database.
        It provides a basic navigation menu with the following options: Search, Insert, Update. The class inherits from the IFrame class.

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
        _initializeImages(): Initializes images used in the frame.
        _setupStructureOptions(data): Sets up options for the frame's structure.
        _buildStructure(): Builds the general structure of the frame (Header, Body).
        _createHeaderFrame(): Creates the Header Frame.
        _createBodyFrame(): Creates the Body Frame.
        __gotoDatabasePicker(): Leads the user to the database picker frame
        __gotoSearch(): Leads the user to the search frame

    """

    def __init__(self, applicationSettings: dict[str, Any]) -> None:
        """ The constructor of the MainMenuFrame class. Here, the actual frame and the main structure are being built, while additional data such as
            images and options are being initialized.

        Args:
            applicationSettings (dict[str, Any]): The settings of the parent widget (Application Window).
        """
        super().__init__(applicationSettings)  # Initializing the basic frame

    def _initializeImages(self) -> None:
        """ Initialize all the images used in the frame. """

        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.change_logo_image = tk.PhotoImage(file=self.body_options['change-file-button-image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-image-path'])
        self.insert_logo_image = tk.PhotoImage(file=self.body_options['insert-image-path'])
        self.update_logo_image = tk.PhotoImage(file=self.body_options['update-image-path'])

    def _setupStructureOptions(self, parentWidgetSettings: dict[str, Any]) -> None:
        """ Initialize options for all the frame's components (Header, Body).

        Args:
            parentWidgetSettings (dict[str, Any]): The settings of the parent widget.
        """
        # Setting up the Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "message-title": f"ΕΝΕΡΓΟ ΑΡΧΕΙΟ:" + " " * 10 + f"{getFileName(self.applicationSettings['app-data']['active-database'])}",
            "message-title-font": ('Arial', round(0.018 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height'])), 'bold'),
            "buttons-font": ('Arial', round(0.011 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "change-file-button-text": "ΑΛΛΑΓΗ",
            "change-file-button-font": ('Arial', round(0.011 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "change-file-button-padx-outer": round(0.02 * self.applicationSettings['window-width']),
            "change-file-button-padx-inner": round(0.01 * self.applicationSettings['window-width']),
            "change-file-button-pady-inner": round(0.005 * self.applicationSettings['window-height']),
            "change-file-button-image-path": CHANGE_PNG_PATH,
            "search-image-path": SEARCH_PNG_PATH,
            "insert-image-path": INSERT_PNG_PATH,
            "update-image-path": UPDATE_PNG_PATH,
            "navigation-button-width": round(0.4 * self.applicationSettings['window-width']),
            "navigation-button-font": ('Arial', round(0.025 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "navigation-button-padx-inner": round(0.03 * self.applicationSettings['window-width']),
            "navigation-button-pady-inner": round(0.012 * self.applicationSettings['window-height']),
            "navigation-button-pady-outer": round(0.05 * self.applicationSettings['window-height']),
            "search-button-text": "ΑΝΑΖΗΤΗΣΗ",
            "insert-button-text": "ΚΑΤΑΧΩΡΗΣΗ",
            "update-button-text": "  ΔΙΟΡΘΩΣΗ  "
        }

    def __deleteActiveDatabase(self) -> None:
        """ Deletes the active database of the application. Specifically it gains access to the .json file containing the application settings and
            empties the 'active-database' field. """

        # Updating the application data in the program and save them in a JSON file
        self.applicationSettings['app-data']['active-database'] = ""
        with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
            json.dump(self.applicationSettings['app-data'], json_file)

    def __gotoDatabasePicker(self) -> None:
        """ Changes the active frame to the Database Picker one. """

        self.app.setActiveFrame(self.app.databasePickerFrame)  # Setting the active frame to DatabasePickerFrame

    def __gotoSearch(self) -> None:
        """ Changes the active frame to the Search Frame. """

        self.app.setActiveFrame(self.app.searchFrame)  # Setting the active frame to SearchFrame

    def __gotoInsert(self) -> None:
        """ Changes the active frame to the Insert Frame. """

        self.app.setActiveFrame(self.app.insertFrame)  # Setting the active frame to InsertFrame

    def __gotoUpdate(self) -> None:
        """ Changes the active frame to the Update Frame. """

        self.app.setActiveFrame(self.app.updateFrame)  # Setting the active frame to UpdateFrame

    def _buildStructure(self) -> None:
        """ Builds the general structure of the main menu frame (Header, Body). """

        self._createHeaderFrame()  # First create the header
        self._createBodyFrame()    # Then create the body

    def _createHeaderFrame(self) -> None:
        """ The _createHeaderFrame() method is used by the __buildStructure() method, and it builds the header frame of the main structure.
            It creates a main label with a title and an image of the 'Greek Police Logo' next to it. """

        self.header = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the header frame

        # Creating the Header Label
        self.header_image = resizeImage(self.police_logo_image, round(0.13 * self.applicationSettings['window-width']))
        self.header_label = tk.Label(
            self.header,
            text=self.header_options['title'], font=self.header_options['font'],
            bg=self.applicationSettings['theme-color'], fg=self.applicationSettings['label-fg-color'],
            image=self.header_image, compound=tk.LEFT,
            padx=round(0.04 * self.applicationSettings['window-width']), pady=round(0.04 * (self.applicationSettings['window-height']))
        )

        # Packing the header and its widgets
        self.header_label.pack()
        self.header.pack()

    def _createBodyFrame(self) -> None:
        """ The _createBodyFrame() method is used by the __buildStructure() method, and it builds the body frame of the main structure.
            It creates a message telling the user which database is currently working with, and a frame containing the three basic navigation buttons,
            (Search, Insert, Update). """

        self.body = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the body frame

        # Creating a parent frame that will hold the label and 'Change File' button
        self.body_title_frame = tk.Frame(self, bg=self.applicationSettings['theme-color'])

        # Creating the body label message
        self.body_options['message-title'] = f"ΕΝΕΡΓΟ ΑΡΧΕΙΟ:" + " " * 10 + f"{getFileName(self.applicationSettings['app-data']['active-database'])}"
        self.body_label_message = tk.Label(self.body_title_frame, text=self.body_options['message-title'], font=self.body_options['message-title-font'], bg=self.applicationSettings['theme-color'], fg=self.applicationSettings['label-fg-color'])

        # Creating the 'Change File' button
        self.change_file_image = resizeImage(self.change_logo_image, int(2 * self.body_options['change-file-button-font'][1]))
        self.change_file_button = tk.Button(
            self.body_title_frame,
            text=self.body_options["change-file-button-text"], font=self.body_options["change-file-button-font"],
            image=self.change_file_image, compound=tk.LEFT,
            padx=self.body_options['change-file-button-padx-inner'], pady=self.body_options['change-file-button-pady-inner'],
            command=lambda: f"{self.__deleteActiveDatabase()}{self.__gotoDatabasePicker()}"
        )

        # Creating the main navigation buttons (Search, Insert, Update)
        self.nav_buttons_frame = tk.Frame(self, bg=self.applicationSettings['theme-color'])

        # Create the images used in the buttons
        self.search_image = resizeImage(self.search_logo_image, int(2 * self.body_options['navigation-button-font'][1]))  # Search Image
        self.insert_image = resizeImage(self.insert_logo_image, int(2 * self.body_options['navigation-button-font'][1]))  # Insert Image
        self.update_image = resizeImage(self.update_logo_image, int(2 * self.body_options['navigation-button-font'][1]))  # Update Image

        images = [self.search_image, self.insert_image, self.update_image]    # A List that contains the navigation buttons images
        images_texts = ["search", "insert", "update"]                         # A List that contains the navigation buttons titles
        commands = [self.__gotoSearch, self.__gotoInsert, self.__gotoUpdate]  # A List that contains the navigation buttons commands

        buttons = []  # An empty list that will contain all the buttons

        # Creating each button with a 'fancy' way
        for i, image in enumerate(zip(images, images_texts)):
            new_button = createNavigationButton(
                self.nav_buttons_frame,
                self.body_options[f'{image[1]}-button-text'], self.body_options['navigation-button-font'],
                self.body_options['navigation-button-width'], image[0],
                self.body_options['navigation-button-padx-inner'], self.body_options['navigation-button-pady-inner'],
                commands[i]
            )
            buttons.append(new_button)  # Adding the new button to the buttons list

        # Packing the body and its widgets
        self.body_label_message.grid(row=0, column=0)
        self.change_file_button.grid(row=0, column=1, padx=self.body_options['change-file-button-padx-outer'])
        self.body_title_frame.pack()

        for button in buttons:
            button.pack(pady=self.body_options['navigation-button-pady-outer'])

        self.nav_buttons_frame.pack()
        self.body.pack()

    def _createFooterFrame(self) -> None:
        """ The current frame does not have a footer, so the only code here calls _createFooterFrame() method of the base class. """

        return super()._createFooterFrame()

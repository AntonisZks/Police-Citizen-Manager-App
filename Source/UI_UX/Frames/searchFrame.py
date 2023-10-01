"""
The 'searchFrame.py' file contains the SearchFrame class, which represents the search frame of the application. The frame provides two options of searching,
'By Folder ID' and 'By Surname'. Providing two input fields on the upper part of the frame, the user can search for folders, according to the input they entered
inside the suitable input field. The 'Search By FolderID' field makes sure that its given data must be exactly the same with the results, while the 'Search By Surname'
field says that the results must start with the given data. The frame provides two canvas in the body part. The left canvas displays all the results records that match with
the given data to search by the user. They appear as a vertical list of check buttons, the user can click on them. A supporting side scrollbar is provided too. The right canvas
displays the data of every result showed in the left canvas. When the user clicks on a result record, a new tab is being added to the right canvas containing the data of that
result record. Therefore, the user can navigate threw different result records they selected. Finally, the frame contains a 'Return' button in order to let the user go back to the
main menu frame.

"""

from Source.UI_UX.Frames.frame import IFrame
from Source.UI_UX.Other.searchBar import SearchBar
from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.resultsRecordsListVisualizer import ResultsRecordsListVisualizer
from Source.UI_UX.RecordsStuff.resultRecordDataVisualizer import ResultRecordDataVisualizer
from Source.UI_UX.RecordsStuff.recordsManager import RecordsManager


class SearchFrame(IFrame):
    """ The SearchFrame class represents the search frame of the application where the user can search for folders by folder ID or surname.

    Attributes:
        header_options (dict): Options for the Header Frame.
        body_options (dict): Options for the Body Frame.
        police_logo_image (PhotoImage): An image that is displayed on the main header label.
        search_logo_image (PhotoImage): An image for the search bar.
        header (Frame): The header frame.
        header_image (PhotoImage): The image used in the header section as part of the main label.
        header_label (Label): The main label displayed on the header.
        body (Frame): The body frame.
        searchbars_frame (Frame): A frame that holds the search bars.
        folderID_search_bar_frame (Frame): A frame for the folderID search bar.
        folderID_search_bar (SearchBar): The search bar for folderID.
        surname_search_bar_frame (Frame): A frame for the surname search bar.
        surname_search_bar (SearchBar): The search bar for surname.

    Methods:
        _initializeImages(): Initializes images used in the frame.
        _setupStructureOptions(data): Sets up options for the frame's structure.
        _buildStructure(): Builds the general structure of the frame (Header, Body).
        _createHeaderFrame(): Creates the Header Frame.
        _createBodyFrame(): Creates the Body Frame.

    """

    def __init__(self, applicationSettings: dict[str, Any], askForPassword: bool = False) -> None:
        """ Constructor for the SearchFrame class. The constructor of the SearchFrame calls the constructor of the base class IFrame
            and initializes a scrollbar object to None.

        Args:
            applicationSettings (dict): Data related to the application.

        """

        # Initializing the basic frame
        super().__init__(applicationSettings, askForPassword)

        self.record_area_scrollbar = None  # Initialize a temporary variable for the side scrollbar

    def _initializeImages(self) -> None:
        """ Initializes all the images used in the frame. """

        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-bar-image-path'])
        self.return_logo_image = tk.PhotoImage(file=self.footer_options['return-button-image-path'])

    def _setupStructureOptions(self, parentWidgetSettings: dict[str, Any]) -> None:
        """ Sets up the options for the frame's structure.

        Args:
            parentWidgetSettings (dict[str, Any]): Data related to the application.

        """

        # Setting up the Header Options
        self.header_options = {
            "title": "ΑΝΑΖΗΤΗΣΗ ΦΑΚΕΛΩΝ ΜΕ:",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "search-bar-image-path": SEARCH_PNG_PATH,
            "search-bar-font": ('Arial', round(0.021 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "search-bar-width": round(0.022 * self.applicationSettings['window-width']),
            "search-bar-padx-outer": round(0.08 * self.applicationSettings['window-width']),
            "search-bar-pady-outer": round(0.01 * self.applicationSettings['window-height']),
            "search-bar-border-width": lambda: round(0.34 * self.body_options['search-bar-font'][1]),
            "folderID-search-bar-place-holder": "Αριθμός Φακέλου",
            "surname-search-bar-place-holder": "Επώνυμο",
            "list-visualizer-width": round(0.65 * self.applicationSettings['window-width']),
            "list-visualizer-height": round(0.55 * self.applicationSettings['window-height']),
            "data-visualizer-width": round(0.65 * self.applicationSettings['window-width']),
            "data-visualizer-height": round(0.685 * self.applicationSettings['window-height']),
            "records-area-no-records-message": "ΚΑΝΕΝΑ ΑΠΟΤΕΛΕΣΜΑ",
            "records-area-no-records-selected-message": "ΔΕΝ ΕΧΕΙ ΕΠΙΛΕΓΕΙ\nΚΑΝΕΝΑΣ ΦΑΚΕΛΟΣ",
            "records-area-font": ('Arial', round(0.03 * self.applicationSettings['window-width'])),
            "record-button-font": ('Arial', round(0.014 * self.applicationSettings['window-width']))
        }

        # Setting up the Footer Options
        self.footer_options = {
            "return-button-text": " ΕΠΙΣΤΡΟΦΗ ΣΤΟ ΜΕΝΟΥ ",
            "return-button-font": ('Arial', round(0.018 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "return-button-image-path": RETURN_PNG_PATH,
            "return-button-padx-inner": round(0.01 * self.applicationSettings['window-width']),
            "return-button-pady-inner": round(0.005 * self.applicationSettings['window-height']),
            "return-button-padx-outer": round(0.01 * self.applicationSettings['window-width']),
            "return-button-pady-outer": round(0.012 * self.applicationSettings['window-height']),
        }

    def closeAllRecordsVisualizerTabs(self) -> None:
        """ Removes all the tabs from the record manager object. """

        for index in list(self.resultsRecordsListVisualizer.selected_buttons.keys()):
            self.resultRecordDataVisualizer.removeTab(index)

    def __goToMainMenu(self):
        """ Changes the active frame to the Main Menu one. """

        self.app.tryToSetActiveFrame(self.app.mainMenuFrame)  # Setting the active frame to MainMenuFrame

    def _buildStructure(self) -> None:
        """ Builds the general structure of the search frame (Search, Insert, Update). """

        self._createHeaderFrame()  # First create the header
        self._createBodyFrame()    # Then create the body
        self._createFooterFrame()  # Finally, create the footer

    def __searchByFolderID(self) -> None:
        """ Gains access to the database the user is currently working with, and returns all of its data that their 'folder ID' field matches with the
            one the user entered inside the 'Search By Folder ID' input field. The 'folder ID' field of the results must be exactly the same with the 'folder ID' value
            the user entered. """

        # Clearing the selected tabs in the Record Visualizer Notebook
        self.closeAllRecordsVisualizerTabs()

        # Getting the current value of the folderID search bar
        item = self.folderID_search_bar.getItem()
        if item == "" or item == self.folderID_search_bar.placeHolder:
            return

        # Getting all the stored data in the current active database
        records_df = RecordsManager.getRecordsFromDatabase(self.applicationSettings['app-data']['active-database'])  # Gaining the data from the database

        # Keeping those data that their folderID is similar to the folderID search bar value
        filtered_df = records_df[records_df["Α.Φ."] == int(item)]

        # Creating the record buttons containing the returned results
        self.resultsRecordsListVisualizer.createRecordButtons(filtered_df, self.body_options['record-button-font'])

    def __searchBySurname(self) -> None:
        """ Gains access to the database the user is currently working with, and returns all of its data that their 'surname' field starts with the
            one the user entered inside the 'Search By Surname' input field. The 'surname' field of the results must start with the 'surname' value
            the user entered. """

        # Clearing the selected tabs in the Record Visualizer Notebook
        self.closeAllRecordsVisualizerTabs()

        # Getting the current value of the Surname search bar
        item = self.surname_search_bar.getItem()
        if item == "" or item == self.surname_search_bar.placeHolder:
            return

        # Getting all the stored data in the current active database
        records_df = RecordsManager.getRecordsFromDatabase(self.applicationSettings['app-data']['active-database'])  # Gaining the data from the database

        # Keeping those data that their folderID is similar to the folderID search bar value
        filtered_df = records_df[records_df["ΕΠΩΝΥΜΟ"].str.startswith(item.upper())]

        # Creating the record buttons containing the returned results
        self.resultsRecordsListVisualizer.createRecordButtons(filtered_df, self.body_options['record-button-font'])

    def _createHeaderFrame(self) -> None:
        """ The _createHeaderFrame() method is used by the __buildStructure() method, and it builds the header frame of the main structure.
            It creates a main label with a title and an image of the 'Greek Police Logo' next to it. """

        self.header = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the header frame

        # Creating the Header Label
        self.header_image = resizeImage(self.police_logo_image, round(0.12 * self.applicationSettings['window-width']))
        self.header_label = tk.Label(
            self.header,
            text=self.header_options['title'],
            font=self.header_options['font'],
            bg=self.applicationSettings['theme-color'],
            fg=self.applicationSettings['label-fg-color'],
            image=self.header_image, compound=tk.LEFT,
            padx=round(0.04 * self.applicationSettings['window-width']),
            pady=round(0.04 * (self.applicationSettings['window-height']))
        )

        # Packing the header and its widgets
        self.header_label.pack()
        self.header.pack()

    def _createBodyFrame(self) -> None:
        """ The _createBodyFrame() method is used by the __buildStructure() method, and it builds the body frame of the main structure.
            It creates the two canvas containing the results records, as a list and the data of each record the user selected. """

        self.body = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the body frame
        self.body.pack()                                                        # Packing the body frame

        self.leftFrame = tk.Frame(self.body, bg=self.applicationSettings['theme-color'])   # Creating the left frame of the body
        self.rightFrame = tk.Frame(self.body, bg=self.applicationSettings['theme-color'])  # Creating the right frame of the body

        self.leftFrame.grid(row=0, column=0)   # Griding the left frame in the scene
        self.rightFrame.grid(row=0, column=1)  # Griding the right frame in the scene

        # Creating a general frame that will hold the Search Bars
        self.searchbars_frame = tk.Frame(self.leftFrame, bg=self.applicationSettings['theme-color'])
        self.searchbars_frame.pack()

        # Creating the folderID Search Bar
        self.folderID_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.applicationSettings['theme-color'])
        self.folderID_search_bar_frame.pack(padx=self.body_options["search-bar-padx-outer"], pady=self.body_options["search-bar-pady-outer"])
        self.folderID_search_bar = SearchBar(
            self.folderID_search_bar_frame, self.applicationSettings, self.body_options["search-bar-width"],
            self.body_options["search-bar-border-width"](),  # IMPORTANT: The border width key has a function as a value, that's why we call it
            self.body_options["folderID-search-bar-place-holder"],
            self.body_options["search-bar-font"],
            self.__searchByFolderID
        )
        self.folderID_search_bar.build()  # Building the 'Search By Folder ID' search bar
        self.folderID_search_bar.put()    # Putting the 'Search By Folder ID' search bar on the screen

        # Creating the surname Search Bar
        self.surname_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.applicationSettings['theme-color'])
        self.surname_search_bar_frame.pack(padx=self.body_options["search-bar-padx-outer"], pady=self.body_options["search-bar-pady-outer"])
        self.surname_search_bar = SearchBar(
            self.surname_search_bar_frame, self.applicationSettings, self.body_options["search-bar-width"],
            self.body_options["search-bar-border-width"](),  # IMPORTANT: The border width key has a function as a value, that's why we call it
            self.body_options["surname-search-bar-place-holder"],
            self.body_options["search-bar-font"],
            self.__searchBySurname
        )
        self.surname_search_bar.build()  # Building the 'Search By Surname' search bar
        self.surname_search_bar.put()    # Putting the 'Search By Surname' search bar on the screen

        # Creating a main frame that will hold the records area left and the person data area right
        self.leftResultsFrame = tk.Frame(self.leftFrame, bg=self.applicationSettings['theme-color'])
        self.leftResultsFrame.pack()

        # Creating the results records list object that manages and displays the result records from the search
        self.resultsRecordsListVisualizer = ResultsRecordsListVisualizer(
            self.leftResultsFrame,
            self.applicationSettings,
            self.body_options['list-visualizer-width'],
            self.body_options['list-visualizer-height'],
            self.applicationSettings['theme-color-dark'],
            {
                "text": self.body_options['records-area-no-records-message'],
                "font": self.body_options['records-area-font'],
                "bg": self.applicationSettings['theme-color-dark'],
                "fg": self.applicationSettings['theme-color-very-dark']
            }
        )

        self.resultsRecordsListVisualizer.createNoRecordsMessage()
        self.resultsRecordsListVisualizer.show(
            0, 0,
            round(0.05 * self.applicationSettings['window-width']),
            round(0.018 * self.applicationSettings['window-height'])
        )

        # Creating a main frame that will hold the records area left and the person data area right
        self.rightResultsFrame = tk.Frame(self.rightFrame, bg=self.applicationSettings['theme-color'])
        self.rightResultsFrame.pack()

        # Creating the result record data visualizer object that displays the data of each record
        self.resultRecordDataVisualizer = ResultRecordDataVisualizer(
            self.rightResultsFrame,
            self.applicationSettings,
            self.body_options['data-visualizer-width'],
            self.body_options['data-visualizer-height'],
            self.applicationSettings['theme-color-dark'],
            {
                "text": self.body_options['records-area-no-records-selected-message'], "font": self.body_options['records-area-font'],
                "bg": self.applicationSettings['theme-color-dark'], "fg": self.applicationSettings['theme-color-very-dark']
            }
        )
        self.resultRecordDataVisualizer.addTemporaryTab()
        self.resultRecordDataVisualizer.show(
            0, 1,
            round(0.05 * self.applicationSettings['window-width']), round(0.018 * self.applicationSettings['window-height'])
        )

        # Connecting the records Manager and Visualiser
        self.resultsRecordsListVisualizer.dataVisualiser = self.resultRecordDataVisualizer
        self.resultRecordDataVisualizer.listVisualizer = self.resultsRecordsListVisualizer

    def _createFooterFrame(self) -> None:
        """ The _createFooterFrame() method is used by the __buildStructure() method, and it builds the footer frame of the main structure.
            It creates a 'Return' button in order to let the user go back to the Main Menu if they want. """

        # Creating an image that is going to be displayed on the 'Return' button
        self.return_image = resizeImage(self.return_logo_image, int(2 * self.footer_options["return-button-font"][1]))

        # Creating the actual button
        self.returnButton = tk.Button(
            self,
            text=self.footer_options["return-button-text"], font=self.footer_options["return-button-font"],
            image=self.return_image, compound=tk.LEFT,
            padx=self.footer_options["return-button-padx-inner"], pady=self.footer_options["return-button-pady-inner"],
            command=self.__goToMainMenu
        )

        # Packing the button
        self.returnButton.pack(padx=self.footer_options["return-button-padx-outer"], pady=self.footer_options["return-button-pady-outer"])

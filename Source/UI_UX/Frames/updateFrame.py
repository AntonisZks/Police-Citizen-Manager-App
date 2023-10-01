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
from tkinter import messagebox

from Source.UI_UX.Frames.frame import IFrame
from Source.UI_UX.Other.searchBar import SearchBar
from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.recordsManager import RecordsManager
from Source.UI_UX.RecordsStuff.resultsRecordsListVisualizer import ResultsRecordsListVisualizer
from Source.UI_UX.RecordsStuff.resultsRecordsDataEditor import ResultsRecordsDataEditor


class UpdateFrame(IFrame):
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
        self.save_logo_image = tk.PhotoImage(file=self.footer_options['save-button-image-path'])
        self.delete_logo_image = tk.PhotoImage(file=self.footer_options['delete-button-image-path'])

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
            "search-bar-pady-outer": round(0.01 * self.applicationSettings['window-width']),
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
            "save-button-text": " ΑΠΟΘΗΚΕΥΣΗ ΑΛΛΑΓΩΝ ",
            "save-button-font": ('Arial', round(0.018 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "save-button-image-path": SAVE_PNG_PATH,
            "delete-button-text": " ΔΙΑΓΡΑΦΗ ΣΤΟΙΧΕΙΩΝ ",
            "delete-button-font": ('Arial', round(0.018 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "delete-button-image-path": DELETE_PNG_PATH,
            "return-button-text": " ΕΠΙΣΤΡΟΦΗ ΣΤΟ ΜΕΝΟΥ ",
            "return-button-font": ('Arial', round(0.018 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
            "return-button-image-path": RETURN_PNG_PATH,
            "button-padx-inner": round(0.01 * self.applicationSettings['window-width']),
            "button-pady-inner": round(0.005 * self.applicationSettings['window-height']),
            "button-padx-outer": round(0.01 * self.applicationSettings['window-width']),
            "button-pady-outer": round(0.012 * self.applicationSettings['window-height']),
        }

    def closeAllRecordsVisualizerTabs(self) -> None:
        """ Removes all the tabs from the record manager object. """

        for index in list(self.resultsRecordsListVisualizer.selected_buttons.keys()):
            self.resultsRecordsDataEditor.removeTab(index)

    def __goToMainMenu(self):
        """ Changes the active frame to the Main Menu one. """

        self.app.tryToSetActiveFrame(self.app.mainMenuFrame)  # Setting the active frame to MainMenuFrame

    def __saveChanges(self):
        """ Saves the changes the user has done to specifics records, in the database. """

        if self.resultsRecordsListVisualizer.records is not None:
            recordsStates = [self.resultsRecordsListVisualizer.checkButtonsVar[-1].get()]  # Getting and fixing the states (ON/OFF) of every record in the record manager
            for i in range(len(self.resultsRecordsListVisualizer.checkButtonsVar) - 1):
                recordsStates.append(self.resultsRecordsListVisualizer.checkButtonsVar[i].get())

            # Getting the line indexes of every record
            recordsDatabaseIndexes = []
            for record in self.resultsRecordsListVisualizer.records:
                recordsDatabaseIndexes.append(record.databaseIndex)

            # Zipping the records indexes and states into a tuple in order to filter some of them later
            recordsIndexesStates = tuple(zip(recordsDatabaseIndexes, recordsStates))

            # Getting those data where their state is 1
            filteredRecordsIndexesStates = tuple(filter(lambda item: item if item[1] == 1 else None, recordsIndexesStates))
            recordIndexes = [item[0] for item in filteredRecordsIndexesStates]

            changedRecords = []  # Initializing an empty list that will hold all the records that has been changed

            # Iterate through all the tabs in the record visualizer and get the changes the user has done
            for tab in self.resultsRecordsDataEditor.notebook.tabs():
                tab = self.resultsRecordsDataEditor.notebook.nametowidget(tab)  # Getting the actual tab

                # Checking if the current tab has two children (primary data frame and secondary data frame)
                if len(tab.winfo_children()) == 2:
                    primaryDataFrame = tab.winfo_children()[0]    # Getting the primary data frame
                    secondaryDataFrame = tab.winfo_children()[1]  # Getting the secondary data frame

                    data = []  # Initializing a list which is going to contain the changed data of each tab

                    # Iterate through all the primary data and add them to the changed data list
                    for dataHolderField in primaryDataFrame.winfo_children():
                        data.append(dataHolderField.winfo_children()[1].get())

                    # Iterate through all the secondary data and add them to the changed data list
                    for dataHolderField in secondaryDataFrame.winfo_children():
                        data.append(dataHolderField.winfo_children()[1].get('1.0', tk.END))

                    changedRecords.append(data)  # Adding the new changed record to the changed records list

            if any(recordsStates) == 0:

                # Show a message box and notify the user that they haven't selected any file to change
                messagebox.showinfo("Καμία Διόρθωση", "Δεν έχετε επιλέξει κανένα φάκελο για διόρθωση")
                return

            # Checking if the data are valid
            if any(not RecordsManager.validData2(*changedRecord) for changedRecord in changedRecords):
                return

            RecordsManager.updateDataInDatabase(changedRecords, recordIndexes, self.applicationSettings['app-data']['active-database'])  # Updating the data and save them to the database

            # Show a message box and notify the user that the changes were successful, and go back to the main menu
            numberOfChangesString = f"{len(self.resultsRecordsDataEditor.notebook.tabs())} φακέλους." if len(self.resultsRecordsDataEditor.notebook.tabs()) > 1 else "1 φάκελο."
            messagebox.showinfo("Επιτυχής Διόρθωση Δεδομένων", "Έγινε επιτυχής διόρθωση δεδομένων σε " + numberOfChangesString)

            self.__goToMainMenu()  # Go to the main menu of the application

    def __deleteRecords(self):
        """ Deletes the records the user has selected from the database. """

        if self.resultsRecordsListVisualizer.records is not None:
            recordsStates = [self.resultsRecordsListVisualizer.checkButtonsVar[-1].get()]  # Getting and fixing the states (ON/OFF) of every record in the record manager
            for i in range(len(self.resultsRecordsListVisualizer.checkButtonsVar) - 1):
                recordsStates.append(self.resultsRecordsListVisualizer.checkButtonsVar[i].get())

            # Getting the line indexes of every record
            recordsDatabaseIndexes = []
            for record in self.resultsRecordsListVisualizer.records:
                recordsDatabaseIndexes.append(record.databaseIndex)

            # Zipping the records indexes and states into a tuple in order to filter some of them later
            recordsIndexesStates = tuple(zip(recordsDatabaseIndexes, recordsStates))

            # Getting those data where their state is 1
            filteredRecordsIndexesStates = tuple(filter(lambda item: item if item[1] == 1 else None, recordsIndexesStates))
            recordIndexes = [item[0] for item in filteredRecordsIndexesStates]

            if any(recordsStates) == 0:

                # Show a message box and notify the user that they haven't selected any file to change
                messagebox.showinfo("Καμία Διαγραφή", "Δεν έχετε επιλέξει κανένα φάκελο για διαγραφή")
                return

            # Show a message box and ask them if they are sure about deleting the selected files
            numberOfChangesString = f"{len(self.resultsRecordsDataEditor.notebook.tabs())} φακέλων! " if len(self.resultsRecordsDataEditor.notebook.tabs()) > 1 else "1 φακέλου! "
            if not messagebox.askyesno("Προειδοποίηση", "Πρόκειται να γίνει διαγραφή " + numberOfChangesString + "Επιθυμείτε να συνεχίσετε;", icon=messagebox.WARNING):
                return

            RecordsManager.deleteRecordsFromDatabase(recordIndexes, self.applicationSettings['app-data']['active-database'])

            # Show a message box and notify the user that the deletion were successful, and go back to the main menu
            numberOfChangesString = f"{len(self.resultsRecordsDataEditor.notebook.tabs())} φακέλων." if len(self.resultsRecordsDataEditor.notebook.tabs()) > 1 else "1 φακέλου."
            messagebox.showinfo("Επιτυχής Διαγραφή Δεδομένων", "Έγινε επιτυχής διαγραφή " + numberOfChangesString)

            self.__goToMainMenu()  # Go to the main menu of the application

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
        records_df = pd.read_excel(self.applicationSettings['app-data']['active-database'])
        records_df = records_df.fillna('')  # this command makes sure that the NaN values in the Excel are filled with ''

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
        records_df = pd.read_excel(self.applicationSettings['app-data']['active-database'])
        records_df = records_df.fillna('')  # this command makes sure that the NaN values in the Excel are filled with ''

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
        self.body.pack()  # Packing the body frame

        self.leftFrame = tk.Frame(self.body, bg=self.applicationSettings['theme-color'])  # Creating the left frame of the body
        self.rightFrame = tk.Frame(self.body, bg=self.applicationSettings['theme-color'])  # Creating the right frame of the body

        self.leftFrame.grid(row=0, column=0)  # Griding the left frame in the scene
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
        self.folderID_search_bar.put()  # Putting the 'Search By Folder ID' search bar on the screen

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
        self.surname_search_bar.put()  # Putting the 'Search By Surname' search bar on the screen

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
        self.resultsRecordsDataEditor = ResultsRecordsDataEditor(
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
        self.resultsRecordsDataEditor.addTemporaryTab()
        self.resultsRecordsDataEditor.show(
            0, 1,
            round(0.05 * self.applicationSettings['window-width']), round(0.018 * self.applicationSettings['window-height'])
        )

        # Connecting the records Manager and Visualiser
        self.resultsRecordsListVisualizer.dataVisualiser = self.resultsRecordsDataEditor
        self.resultsRecordsDataEditor.listVisualizer = self.resultsRecordsListVisualizer

    def _createFooterFrame(self) -> None:
        """ The _createFooterFrame() method is used by the __buildStructure() method, and it builds the footer frame of the main structure.
            It creates a 'Return' button in order to let the user go back to the Main Menu if they want. """

        self.footer = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the footer frame
        self.footer.pack()                                                        # Packing the footer frame

        # Creating an image that is going to be displayed on the 'Return' button
        self.return_image = resizeImage(self.return_logo_image, int(2 * self.footer_options["return-button-font"][1]))

        # Creating the 'Return' button
        self.returnButton = tk.Button(
            self.footer,
            text=self.footer_options["return-button-text"], font=self.footer_options["return-button-font"],
            image=self.return_image, compound=tk.LEFT,
            padx=self.footer_options["button-padx-inner"], pady=self.footer_options["button-pady-inner"],
            command=self.__goToMainMenu
        )

        # Creating an image that is going to be displayed on the 'Save' button
        self.save_image = resizeImage(self.save_logo_image, int(2 * self.footer_options["save-button-font"][1]))

        # Creating the 'Return' button
        self.saveButton = tk.Button(
            self.footer,
            text=self.footer_options["save-button-text"], font=self.footer_options["save-button-font"],
            image=self.save_image, compound=tk.LEFT,
            padx=self.footer_options["button-padx-inner"], pady=self.footer_options["button-pady-inner"],
            command=self.__saveChanges
        )

        # Creating an image that is going to be displayed on the 'Delete' button
        self.delete_image = resizeImage(self.delete_logo_image, int(2 * self.footer_options["delete-button-font"][1]))

        # Creating the 'Return' button
        self.deleteButton = tk.Button(
            self.footer,
            text=self.footer_options["delete-button-text"], font=self.footer_options["delete-button-font"],
            image=self.delete_image, compound=tk.LEFT,
            padx=self.footer_options["button-padx-inner"], pady=self.footer_options["button-pady-inner"],
            command=self.__deleteRecords
        )

        # Packing the buttons
        self.returnButton.grid(row=0, column=0, padx=self.footer_options["button-padx-outer"], pady=self.footer_options["button-pady-outer"])
        self.saveButton.grid(row=0, column=1, padx=self.footer_options["button-padx-outer"], pady=self.footer_options["button-pady-outer"])
        self.deleteButton.grid(row=0, column=2, padx=self.footer_options["button-padx-outer"], pady=self.footer_options["button-pady-outer"])

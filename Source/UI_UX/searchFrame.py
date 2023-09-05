"""
The 'searchFrame.py' file contains the SearchFrame class, which represents the search frame of the application. Users can search 
for folders by folder ID or surname using this frame.

"""

import tkinter as tk
import pandas as pd
from tkinter import ttk
from .frame import Frame
from .searchBar import SearchBar
from .record import Record
from support import *

def makeRecordButtontext(i, record):
    # Creating the text of the button
    button_text = f"{i+1})    " if (i+1) < 10 else f"{i+1})  "
    if record.father_name == "": button_text += f"{record.surname} {record.name}"
    else:
        ending = record.father_name[-2:]
        if ending == "ΗΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending == "ΑΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending == "ΟΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}Υ"
        else: button_text += f"{record.surname} {record.name}   του {record.father_name}"

    return button_text

class SearchFrame(Frame):
    """
    The SearchFrame class represents the search frame of the application where the user can search for folders by folder ID or surname.

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

    def __init__(self, app_data: dict[str, any]) -> None:
        """
        Constructor for the SearchFrame class.

        Args:
            app_data (dict): Data related to the application.
        """
        # Initializing the basic frame
        super().__init__(app_data)

        self.record_area_scrollbar = None

    def _initializeImages(self) -> None:
        """
        Initialize images used in the frame.
        """
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-bar-image-path'])

    def _setupStructureOptions(self, data: dict[str, any]) -> None:
        """
        Set up options for the frame's structure.

        Args:
            data (dict): Data related to the application.
        """
        # Setting up the Header Options
        self.header_options = {
            "title": "ΑΝΑΖΗΤΗΣΗ ΦΑΚΕΛΩΝ ΜΕ:",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022 * max(self.application_data['window-width'], self.application_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "search-bar-image-path": SEARCH_PNG_PATH,
            "search-bar-font": ('Arial', round(0.021 * max(self.application_data['window-width'], self.application_data['window-height']))),
            "search-bar-padx-outer": round(0.08 * self.application_data['window-width']),
            "search-bar-border-width": lambda: round(0.34 * self.body_options['search-bar-font'][1]),
            "folderID-search-bar-place-holder": "Αριθμός Φακέλου",
            "surname-search-bar-place-holder": "Επώνυμο",
            "records-area-width": round(0.65*self.application_data['window-width']),
            "records-area-height": round(0.65*self.application_data['window-height']),
            "records-area-no-records-message": "ΚΑΝΕΝΑ ΑΠΟΤΕΛΕΣΜΑ",
            "records-area-font": ('Arial', round(0.03*self.application_data['window-width'])),
            "record-button-font": ('Arial', round(0.014*self.application_data['window-width']))
        }

    def _buildStructure(self) -> None:
        """
        Build the general structure of the search frame.
        """
        self._createHeaderFrame()  # First create the header
        self._createBodyFrame()  # Then create the body

    def __createNoRecordsMessage(self):
        self.body_no_records_message = tk.Label(
            self.records_frame, 
            text=self.body_options['records-area-no-records-message'], 
            font=self.body_options['records-area-font'],
            bg=self.application_data['theme-color-dark'],
            fg=self.application_data['theme-color-very-dark']
        )
        self.body_no_records_message.pack(pady=round(0.3*self.application_data['window-height']))

    def __createRecordAreaScrollBar(self):
        self.record_area_scrollbar = tk.Scrollbar(self.records_area, orient=tk.VERTICAL, command=self.records_area.yview)
        self.record_area_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.records_area.config(yscrollcommand=self.record_area_scrollbar.set)

    def __searchByFolderID(self):
        # Getting the current value of the folderID search bar
        item = self.folderID_search_bar.getItem()

        # Getting all the stored data in the current active database
        records_df = pd.read_excel(self.application_data['app-data']['active-database'])
        
        # Keeping those data that their folderID is similar to the folderID search bar value
        filtered_df = records_df[records_df["Α.Φ."] > int(item)]

        # Cleaning any previous results amd destroying the 'No Records' message and the Scrollbar
        for child_widget in self.records_frame.winfo_children():
            child_widget.destroy()
        if self.record_area_scrollbar is not None:
            self.record_area_scrollbar.destroy()

        records = [] # Creating a list that will keep all the returned records
        for _, record in filtered_df.iterrows():
            records.append(Record(*record.to_list()))
        
        # Checking if there is any record as a result
        if len(records) == 0:
            self.__createNoRecordsMessage()
            return
        
        # Creating the side scrollbar
        self.__createRecordAreaScrollBar()

        # Creating the record buttons
        for i, record in enumerate(records):
            new_record_button = tk.Checkbutton(
                self.records_frame, 
                text=makeRecordButtontext(i, record),
                font=self.body_options['record-button-font'],
                anchor=tk.W
            )
            new_record_button.config(indicatoron=False, selectcolor=self.application_data['theme-color-light'])
            new_record_button.pack(side="top", fill='x')
            new_record_button.bind('<MouseWheel>', lambda e: onMousewheel(e, self.records_area))
            new_record_button.pack()

        # Updating the scrollregion of the record area
        self.records_area.update_idletasks()
        self.records_area.configure(scrollregion=self.records_area.bbox("all"))
        

    def __searchBySurname(self):
        print("Searching by surname...")

    def _createHeaderFrame(self) -> None:
        """
        Create the Header Frame, which contains the main label and logo.
        """
        self.header = tk.Frame(self.frame, bg=self.application_data['theme-color'])  # Creating the header frame

        # Creating the Header Label
        self.header_image = resizeImage(self.police_logo_image, round(0.13 * self.application_data['window-width']))
        self.header_label = tk.Label(
            self.header,
            text=self.header_options['title'],
            font=self.header_options['font'],
            bg=self.application_data['theme-color'],
            fg=self.application_data['label-fg-color'],
            image=self.header_image, compound=tk.LEFT,
            padx=round(0.04 * self.application_data['window-width']),
            pady=round(0.04 * (self.application_data['window-height']))
        )

        # Packing the header and its widgets
        self.header_label.pack()
        self.header.pack()

    def _createBodyFrame(self) -> None:
        """
        Create the Body Frame, which contains the search bars.
        """
        self.body = tk.Frame(self.frame, bg=self.application_data['theme-color'])  # Creating the body frame
        self.body.pack()

        # Creating a general frame that will hold the Search Bars
        self.searchbars_frame = tk.Frame(self.body, bg=self.application_data['theme-color'])
        self.searchbars_frame.pack()

        # Creating the folderID Search Bar
        self.folderID_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.application_data['theme-color'])
        self.folderID_search_bar_frame.grid(row=0, column=0, padx=self.body_options["search-bar-padx-outer"])
        self.folderID_search_bar = SearchBar(
            self.folderID_search_bar_frame, self.application_data,
            self.body_options["search-bar-border-width"](),  # IMPORTANT: The border width key has a function as a value, that's why we call it
            self.body_options["folderID-search-bar-place-holder"],
            self.body_options["search-bar-font"],
            self.__searchByFolderID
        )
        self.folderID_search_bar.build()
        self.folderID_search_bar.put()

        # Creating the surname Search Bar
        self.surname_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.application_data['theme-color'])
        self.surname_search_bar_frame.grid(row=0, column=1, padx=self.body_options["search-bar-padx-outer"])
        self.surname_search_bar = SearchBar(
            self.surname_search_bar_frame,
            self.application_data,
            self.body_options["search-bar-border-width"](),  # IMPORTANT: The border width key has a function as a value, that's why we call it
            self.body_options["surname-search-bar-place-holder"],
            self.body_options["search-bar-font"],
            self.__searchBySurname
        )
        self.surname_search_bar.build()
        self.surname_search_bar.put()

        # Creating a main frame that will hold the records area left and the person data area right
        self.results_frame = tk.Frame(self.body, bg=self.application_data['theme-color'])
        self.results_frame.pack()

        # Creating records area that corresponds to the results of the search bar
        self.records_area = tk.Canvas(
            self.results_frame, 
            width=self.body_options['records-area-width'], 
            height=self.body_options['records-area-height'],
            background=self.application_data['theme-color-dark'],
            highlightbackground=self.application_data['theme-color-dark']
        )
        self.records_area.grid(row=0, column=0, padx=round(0.05*self.application_data['window-width']), pady=round(0.018*self.application_data['window-height']))
        self.records_frame = ttk.Label(self.records_area, background=self.application_data['theme-color-dark'])
        self.records_area.create_window((0, 0), window=self.records_frame, anchor=tk.NW, width=self.body_options['records-area-width'])
        self.records_area.bind('<MouseWheel>', lambda e: onMousewheel(e, self.records_area))
        

        # Creating a 'No Records' message
        self.__createNoRecordsMessage()

    def _createFooterFrame(self) -> None:
        return super()._createFooterFrame()

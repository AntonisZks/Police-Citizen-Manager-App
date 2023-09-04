import tkinter as tk
from .frame import Frame
from .searchBar import SearchBar
from support import *

class SearchFrame(Frame):
    def __init__(self, app_data: dict[str, any]) -> None:
        # Initializing the basic frame
        super().__init__(app_data)

    def _initializeImages(self) -> None:
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-bar-image-path'])

    def _setupStructureOptions(self, data: dict[str, any]) -> None:
        # Setting up the Header Options
        self.header_options = {
            "title": "ΑΝΑΖΗΤΗΣΗ ΦΑΚΕΛΩΝ ΜΕ:",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.application_data['window-width'], self.application_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "search-bar-image-path": SEARCH_PNG_PATH,
            "search-bar-font": ('Arial', round(0.021*max(self.application_data['window-width'], self.application_data['window-height']))),
            "search-bar-padx-outer": round(0.08*self.application_data['window-width']),
            "search-bar-border-width": lambda: round(0.34*self.body_options['search-bar-font'][1]),
            "folderID-search-bar-place-holder": "Αριθμός Φακέλου",
            "surname-search-bar-place-holder": "Επώνυμο"
        }

    def _buildStructure(self) -> None:
        self._createHeaderFrame() # First create the header
        self._createBodyFrame()  # Then create the body
    
    def _createHeaderFrame(self) -> None:
        self.header = tk.Frame(self.frame, bg=self.application_data['theme-color'])  # Creating the header frame

        # Creating the Header Label
        self.header_image = resizeImage(self.police_logo_image, round(0.13*self.application_data['window-width']))
        self.header_label = tk.Label(
            self.header,
            text=self.header_options['title'],
            font=self.header_options['font'],
            bg=self.application_data['theme-color'],
            fg=self.application_data['label-fg-color'],
            image=self.header_image, compound=tk.LEFT,
            padx=round(0.04*self.application_data['window-width']),
            pady=round(0.04*(self.application_data['window-height']))
        )

        # Packing the header and its widgets
        self.header_label.pack()
        self.header.pack()
    
    def _createBodyFrame(self) -> None:
        self.body = tk.Frame(self.frame, bg=self.application_data['theme-color'])  # Creating the body frame

        # Creating a general frame that will hold the Search Bars
        self.searchbars_frame = tk.Frame(self.body, bg=self.application_data['theme-color'])

        # Creating the folderID Search Bar
        self.folderID_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.application_data['theme-color'])
        self.folderID_search_bar = SearchBar(
            self.folderID_search_bar_frame, self.application_data, 
            1, 1, self.body_options["search-bar-border-width"](), # IMPORTANT: The border width key has a function as a value, that's why we call it 
            self.body_options["folderID-search-bar-place-holder"], 
            self.body_options["search-bar-font"]
        )
        self.folderID_search_bar.build()

        # Creating the surname Search Bar
        self.surname_search_bar_frame = tk.Frame(self.searchbars_frame, bg=self.application_data['theme-color'])
        self.surname_search_bar = SearchBar(
            self.surname_search_bar_frame, 
            self.application_data, 
            1, 1, self.body_options["search-bar-border-width"](), # IMPORTANT: The border width key has a function as a value, that's why we call it 
            self.body_options["surname-search-bar-place-holder"], 
            self.body_options["search-bar-font"]
        )
        self.surname_search_bar.build()

        # Packing the body and its widgets
        self.folderID_search_bar.put()
        self.surname_search_bar.put()
        self.folderID_search_bar_frame.grid(row=0, column=0, padx=self.body_options["search-bar-padx-outer"])
        self.surname_search_bar_frame.grid(row=0, column=1, padx=self.body_options["search-bar-padx-outer"])
        self.searchbars_frame.pack()
        self.body.pack()
    
    def _createFooterFrame(self) -> None:
        return super()._createFooterFrame()

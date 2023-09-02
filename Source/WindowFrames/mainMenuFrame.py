import tkinter as tk
from support import *


def createNavigationButton(parent, text, font, width, image, padx, pady):
    new_button = tk.Button(parent, text=text, font=font, width=width, image=image, compound=tk.LEFT, padx=padx, pady=pady)
    return new_button


class MainMenuFrame:
    def __init__(self, data: dict[str, any]) -> None:
        # Creating the actual frame
        self.parent_widget = data['window'] # The parent widget is going to be the main window
        self.frame = tk.Frame(self.parent_widget, bg=data['theme-color'])
        self.frame.pack()

        # Setup the header, body, and footer options and initialize the images used
        self.__setupStructureOptions(data)
        self.__initializeImages()

    def __initializeImages(self):
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.change_logo_image = tk.PhotoImage(file=self.body_options['change-file-button-image-path'])
        self.search_logo_image = tk.PhotoImage(file=self.body_options['search-image-path'])
        self.insert_logo_image = tk.PhotoImage(file=self.body_options['insert-image-path'])
        self.update_logo_image = tk.PhotoImage(file=self.body_options['update-image-path'])

    def __setupStructureOptions(self, data: dict[str, any]) -> None:
        self.parent_data = data

        # Setting up the Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "message-title": "ΕΝΕΡΓΟ ΑΡΧΕΙΟ:          ΑΡΧΕΙΟ ΑΤ ΗΡΑΚΛΕΙΟΥ",
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

    def build(self):
        self.__buildStructure()

    def __buildStructure(self):
        self.__createHeaderFrame() # First create the header
        self.__createBodyFrame() # Then create the body
        # self.__createFooterFrame() # Finally create the footer

    def __createHeaderFrame(self) -> None:
        self.header = tk.Frame(self.frame, bg=self.parent_data['theme-color']) # Creating the header frame

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
        self.body = tk.Frame(self.frame, bg=self.parent_data['theme-color']) # Creating the body frame

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

        self.search_button = createNavigationButton(
            self.nav_buttons_frame,
            self.body_options['search-button-text'],
            self.body_options['navigation-button-font'],
            self.body_options['navigation-button-width'],
            self.search_image,
            self.body_options['navigation-button-padx-inner'],
            self.body_options['navigation-button-pady-inner'],
        )
        self.insert_button = createNavigationButton(
            self.nav_buttons_frame,
            self.body_options['insert-button-text'],
            self.body_options['navigation-button-font'],
            self.body_options['navigation-button-width'],
            self.insert_image,
            self.body_options['navigation-button-padx-inner'],
            self.body_options['navigation-button-pady-inner'],
        )
        self.update_button = createNavigationButton(
            self.nav_buttons_frame,
            self.body_options['update-button-text'],
            self.body_options['navigation-button-font'],
            self.body_options['navigation-button-width'],
            self.update_image,
            self.body_options['navigation-button-padx-inner'],
            self.body_options['navigation-button-pady-inner'],
        )

        # Packing the body and its widgets
        self.body_label_message.grid(row=0, column=0)
        self.change_file_button.grid(row=0, column=1, padx=self.body_options['change-file-button-padx-outer'])
        self.body_title_frame.pack()
        self.search_button.pack(pady=self.body_options['navigation-button-pady-outer'])
        self.insert_button.pack(pady=self.body_options['navigation-button-pady-outer'])
        self.update_button.pack(pady=self.body_options['navigation-button-pady-outer'])
        self.nav_buttons_frame.pack()
        self.body.pack()
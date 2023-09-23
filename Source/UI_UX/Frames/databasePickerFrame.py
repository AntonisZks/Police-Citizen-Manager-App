"""
The 'databasePickerFrame.py' module contains the DatabasePickerFrame class and its methods.
This frame is the first one displayed when the application starts, allowing the user to select a database (Excel file) to work with.
"""

import json
from tkinter import ttk, filedialog, messagebox
from Source.UI_UX.Frames.frame import IFrame
from Source.Extras.support import *


class DatabasePickerFrame(IFrame):
    """
    The DatabasePickerFrame class represents the starting frame of the application, allowing the user to choose a database.
    It includes a header, a body for displaying databases, and a footer with an 'Add File' button.

    Attributes:
        parent_data (dict): The data of the parent widget (main window).
        header_options (dict): Options for the Header Frame.
        body_options (dict): Options for the Body Frame.
        footer_options (dict): Options for the Footer Frame.
        police_logo_image (PhotoImage): Image displayed on the header.
        add_image (PhotoImage): Image for the 'Add File' button.
        parent_widget (Tk): The main window.
        frame (Frame): The actual frame.
        header (Frame): The header frame.
        header_image (PhotoImage): Image used in the header label.
        header_label (Label): The main label in the header.
        body (Frame): The body frame.
        body_label_message (Label): Message prompting the user to select a database.
        file_picker_area (Canvas): Area for displaying stored databases as buttons.
        file_picker_frame (Label): Supporting tool to arrange database buttons.
        file_picker_scrollbar (Scrollbar): Scrollbar for the database list.
        footer (Frame): The footer frame.
        add_file_image (PhotoImage): Image for the 'Add File' button.
        add_file_button (Button): Button to add a new database.
        button_context_menu (Menu): Context menu for database buttons.

    Methods:
        __addExcelFile(): Adds a new Excel file to the stored databases.
        __buildStructure(): Builds the frame's structure.
        __createBodyFrame(): Creates the Body Frame.
        __createExcelFileButton(parent, path): Creates a button for an Excel File.
        __createExcelFileButtonContextMenu(): Creates the context menu for database buttons.
        __createFooterFrame(): Creates the Footer Frame.
        __createHeaderFrame(): Creates the Header Frame.
        __deleteExcelFileButton(button, index): Deletes a file from the stored databases.
        __initializeImages(): Initializes images used in the frame.
        __openExcelFile(index): Opens an Excel File.
        __openExcelFileFolder(index): Opens the folder containing an Excel File.
        __rebuildStructure(): Rebuilds the frame's structure.
        __setupStructureOptions(data): Sets up structure options (Header, Body, Footer).
        __setActiveDatabase(database_path): Sets the active database for the application.
        __gotoMainMenu(): Switches to the Main Menu Frame.
        __showExcelFileButtonContextMenu(event, button, index): Displays the context menu for a database button.
    """

    def __init__(self, app_data: dict[str, any]) -> None:
        """
        Constructor for the DatabasePickerFrame class. Initializes the frame and its structure.

        Args:
            app_data (dict[str, any]): Data of the parent widget (main window).

        """
        super().__init__(app_data)

    def _initializeImages(self) -> None:
        """
        Initializes images used in the frame.

        """
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.add_image = tk.PhotoImage(file=self.footer_options['add-button-image-path'])

    def _setupStructureOptions(self, data: dict[str, any]) -> None:
        """
        Initializes options for all three frames (Header, Body, Footer).

        Args:
            data (dict[str, any]): Data of the parent widget.

        """
        self.__createExcelFileButtonContextMenu()

        # Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022 * max(self.application_data['window-width'], self.application_data['window-height'])), 'bold')
        }

        # Body Options
        self.body_options = {
            "message-title": textSpaced("ΓΙΑ  ΣΥΝΕΧΕΙΑ  ΕΠΙΛΕΞΤΕ  ΑΡΧΕΙΟ:"),
            "no-files-message": "ΔΕΝ ΕΧΕΙ ΠΡΟΕΠΙΛΕΓΕΙ\nΚΑΝΕΝΑ ΑΡΧΕΙΟ",
            "message-title-font": ('Arial', round(0.018 * max(self.application_data['window-width'], self.application_data['window-height'])), 'bold'),
            "files-font": ('Arial', round(0.011 * max(self.application_data['window-width'], self.application_data['window-height']))),
            "no-files-message-font": ('Arial', round(0.02 * max(self.application_data['window-width'], self.application_data['window-height'])))
        }

        # Footer Options
        self.footer_options = {
            "add-button-text": "ΠΡΟΣΘΗΚΗ ΑΡΧΕΙΟΥ",
            "add-button-image-path": ADD_PNG_PATH,
            "font": ('Arial', round(0.018 * max(self.application_data['window-width'], self.application_data['window-height'])))
        }

    def __setActiveDatabase(self, database_path: str) -> None:
        """
        The __setActiveDatabase() method is used to set the active database of the application

        Args:
            database_path (str): The full path to the database (Excel File)
        """
        # Updating the application data in the program and save them in a json file
        self.application_data['app-data']['active-database'] = database_path
        with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
            json.dump(self.application_data['app-data'], json_file)

    def __gotoMainMenu(self) -> None:
        """
        The __gotoMainMenu() method changes the active frame to the Main Menu one.
        
        """
        self.app.setActiveFrame(self.app.mainMenuFrame)

    @staticmethod
    def __openExcelFile(index: int) -> None:
        """
        The __openExcelFile() method is used to open an Excel File when the user right clicks on its button.

        Args:
            index (int): The index corresponding to the correct Excel file in the stored databases sequence

        """
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        os.startfile(file_path)

    @staticmethod
    def __openExcelFileFolder(index: int) -> None:
        """
        The __openExcelFileFolder() method opens the folder containing the Excel File of the stored databases on the given index.

        Args:
            index (int): The index to get the correct Excel file in the stored databases sequence and open its folder

        """
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        folder_path = os.path.dirname(file_path)
        os.startfile(folder_path)

    def __createExcelFileButton(self, parent: tk.Widget, database_path: str) -> tk.Button:
        """
        The __createExcelFileButton() creates a button corresponding to an Excel File.

        Args:
            parent (Tk): The parent widget of the frame. It is always the main window of the application
            database_path (str): The path corresponding to the Excel File in the computer

        Returns:
            Button: The final button ready to be used

        """
        button_width = round(0.022 * self.application_data['window-width'])
        newExcelFileButton = tk.Button(
            parent,
            text=getFileName(database_path),
            font=self.body_options['files-font'],
            width=button_width,
            command=lambda: f"{self.__setActiveDatabase(database_path)}{self.__gotoMainMenu()}"
        )

        return newExcelFileButton

    def __addExcelFile(self) -> None:
        """
        The __addExcelFile() method adds a new Excel File in the stored databases. First it gives the user the ability to choose
        which database he/she wants to add and then after a quick check of not be included already it adds the new file in the 
        stored databases.

        """
        filetypes = (("Excel files", "*.xls"), ("Excel files", "*.xlsx"))  # Define the available file types

        new_file_path = filedialog.askopenfilename(title="Επιλογή Αρχείου", filetypes=filetypes)
        if new_file_path in self.application_data['app-data']['stored-databases']:
            messagebox.showwarning("Ήδη Υπάρχον Αρχείο", f"Το αρχείο {new_file_path} έχει ήδη οριστεί ως προεπιλογή")
            return

        # If there is a new file path then update the stored databases list in the app data json file and in the window data dictionary
        if new_file_path:
            self.application_data['app-data']['stored-databases'].append(new_file_path)  # Add the new file path in the stored databases list
            with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
                app_data = json.load(json_file)

            app_data['stored-databases'].append(new_file_path)

            with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file)

        self.__rebuildStructure()

    def __deleteExcelFileButton(self, button: tk.Button, index: int) -> None:
        """
        The __deleteExcelFileButton() method deletes the Excel File button and the actual Excel file from the stored databases
        the user has chosen by right-clicking on it.

        Args:
            button (Button): The button to be deleted
            index (int): The index corresponding to the correct Excel file in the stored databases sequence

        """
        if messagebox.askyesno("Αφαίρεση Προεπιλεγμένου Αρχείου", "Θέλετε σίγουρα να αφαιρέσετε το αρχείο;"):
            button.destroy()
            with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
                app_data = json.load(json_file)
            self.application_data['app-data']['stored-databases'].pop(index)
            app_data['stored-databases'].pop(index)

            with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file)
            self.__rebuildStructure()

    def __createExcelFileButtonContextMenu(self) -> None:
        """
        The __createExcelFileButtonContextMenu() method creates a context menu for its individual Excel File button.
        The context menu for each button includes options such as 'Open Excel', 'Open Excel Folder' and 'Remove File'.
        
        """
        # Create a context menu for each file button when the user right clicks on it
        self.button_context_menu = tk.Menu(self, tearoff=False)
        self.button_context_menu.add_command(label="Άνοιγμα Excel")
        self.button_context_menu.add_command(label="Άνοιγμα Θέσης Αρχείου")
        self.button_context_menu.add_separator()
        self.button_context_menu.add_command(label='Αφαίρεση Αρχείου')

    def __showExcelFileButtonContextMenu(self, event, button, index) -> None:
        """
        The __showExcelFileButtonContextMenu() method is used to display the context menu of each Excel File button.

        Args:
            event (any): The event corresponds to the mouse cursor position
            button (Button): The button that is being clicked
            index (int): The index corresponding to the correct Excel file in the stored databases sequence

        """
        self.button_context_menu.post(event.x_root, event.y_root)
        self.button_context_menu.entryconfigure(0, command=lambda: self.__openExcelFile(index))
        self.button_context_menu.entryconfigure(1, command=lambda: self.__openExcelFileFolder(index))
        self.button_context_menu.entryconfigure(3, command=lambda: self.__deleteExcelFileButton(button, index))

    def _buildStructure(self) -> None:
        """
        The _buildStructure() method builds the general structure of the frame (Header, Body, Footer). It also gains
        all the stored databases to be sure if a message such as 'No Files Detected' is appropriate to be displayed.
        Finally, it displays all the Excel Files in the stored databases as buttons to the screen.

        """
        self._createHeaderFrame()  # First create the header
        self._createBodyFrame()  # Then create the body
        self._createFooterFrame()  # Finally create the footer

        # Getting the stored databases
        stored_databases = self.application_data['app-data']['stored-databases']

        # Creating a 'No Files' message if needed
        if len(stored_databases) == 0:
            self.body_no_files_message = tk.Label(
                self.file_picker_frame,
                text=self.body_options["no-files-message"],
                font=self.body_options['no-files-message-font'],
                bg=self.application_data['theme-color-dark'],
                fg=self.application_data['theme-color-very-dark']
            )
            self.body_no_files_message.pack(padx=round(0.27 * self.application_data['window-width']),
                                            pady=round(0.2 * self.application_data['window-height']))

        # Adding all the stored databases as buttons
        button_gap = round(0.015 * self.application_data['window-width'])
        for index in range(len(stored_databases)):
            row, column = index // 3, index % 3
            new_button = self.__createExcelFileButton(self.file_picker_frame, stored_databases[index])
            new_button.grid(row=row, column=column, padx=button_gap + 5, pady=button_gap + 5)
            new_button.bind('<MouseWheel>', lambda e: onMousewheel(e, self.file_picker_area))
            new_button.bind('<Button-3>', lambda event, button=new_button, i=index: self.__showExcelFileButtonContextMenu(event, button, i))

    def __rebuildStructure(self) -> None:
        """
        The __rebuildStructure() method is used to update the display of the frame. First it deletes all the widgets inside it,
        and then it builds them again calling the __buildStructure() method.
        
        """
        for child_widget in self.frame.winfo_children():
            child_widget.destroy()
        self._buildStructure()
        self._setupStructureOptions(self.application_data)

    def _createHeaderFrame(self) -> None:
        """
        The _createHeaderFrame() method is used by the __buildStructure() method, and it builds the header frame of the main structure.
        It creates a main label with a title and an image of the 'Greek Police Logo' next to it.

        """
        self.header = tk.Frame(self, bg=self.application_data['theme-color'])  # Creating the header frame

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
        The _createBodyFrame() method is used by the __buildStructure() method, and it builds the body frame of the main structure.
        It creates a message telling the user to pick a database to work with, the general canvas where all the stored databases are going
        to be displayed and a scrollbar in order to let the user have access to all the individual stored databases. Finally, it does some binding
        to provide a better way of scrolling with the mouse wheel.

        """
        self.body = tk.Frame(self, bg=self.application_data['theme-color'])  # Creating the body frame

        # Creating the Body Label Message
        self.body_label_message = tk.Label(
            self.body, text=self.body_options['message-title'],
            font=self.body_options['message-title-font'],
            bg=self.application_data['theme-color'],
            fg=self.application_data['label-fg-color']
        )

        # Creating the file picker area containing the databases' buttons
        self.file_picker_area = tk.Canvas(
            self.body,
            background=self.application_data['theme-color-dark'],
            highlightbackground=self.application_data['theme-color'],
            width=round(0.9 * self.application_data['window-width']),
            height=round(0.5 * self.application_data['window-height'])
        )

        self.file_picker_area.bind('<Configure>', lambda e: self.file_picker_area.configure(scrollregion=self.file_picker_area.bbox("all")))
        self.file_picker_area.bind('<MouseWheel>', lambda e: onMousewheel(e, self.file_picker_area))

        self.file_picker_frame = ttk.Label(self.file_picker_area, background=self.application_data['theme-color-dark'])
        self.file_picker_area.create_window((0, 0), window=self.file_picker_frame, anchor=tk.NW)
        self.file_picker_frame.bind('<MouseWheel>', lambda e: onMousewheel(e, self.file_picker_area))

        # Creating a scrollbar for the file picker area
        self.file_picker_scrollbar = tk.Scrollbar(self.file_picker_area, orient=tk.VERTICAL, command=self.file_picker_area.yview)
        self.file_picker_area.config(yscrollcommand=self.file_picker_scrollbar.set)

        # Packing the body and its widgets
        self.body_label_message.pack()
        self.file_picker_area.pack(padx=round(0.05 * self.application_data['window-width']),
                                   pady=round(0.04 * self.application_data['window-height']))
        self.file_picker_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.body.pack()

    def _createFooterFrame(self) -> None:
        """
        The _createFooterFrame() method is used by the __buildStructure() method, and it builds the footer frame of the main structure.
        It creates an 'Add File' button which lets the user add a new database into the stored databases.

        """
        self.footer = tk.Frame(self, bg=self.application_data['theme-color'])  # Creating the footer frame

        # Creating the 'Add File' button
        self.add_file_image = resizeImage(self.add_image, round(1.3 * self.footer_options['font'][1]))
        self.add_file_button = tk.Button(
            self.footer,
            text=self.footer_options['add-button-text'],
            font=self.footer_options['font'],
            image=self.add_file_image,
            compound=tk.LEFT,
            padx=round(0.7 * self.footer_options['font'][1]),
            command=self.__addExcelFile
        )

        # Packing the footer and its widgets
        self.footer.pack()
        self.add_file_button.pack(padx=round(0.028 * self.application_data['window-width']))

"""
The 'databaseFilePickerFrame.py' file contains the basic class corresponding to the DatabasePickerFrame and its methods.
When the application starts running, this is the first frame that is going to be appeared on the user's screen letting him/her
select which database he/she wants to work with. It is important that whenever we say database we basically mean simple
Excel Files (.xls, .xlsx). The first time the application will run on a machine, there will be no stored databases and the user
must add one using the 'Add File' button in the bottom of the frame. The selected database will appear on the screen and from
now on it will be saved in the system until the user decides to remove it. By clicking a database that is represented by a button
in the middle of the screen, the user works with this database and we head over to the MainMenuFrame.

"""

import json
import tkinter as tk
from support import *
from .frame import Frame
from tkinter import ttk, filedialog, messagebox
        

# The DatabasePickerFrame class stands for the starting frame of the Application
class DatabasePickerFrame(Frame):
    """
    The DatabasePickerFrame class represents the starting frame of the application. The frame allows the user to
    choose which database he/she wants to work with. It has a basic UX Structure which is made up of three child frames.
    The Header Frame, the Body Frame, and the Footer Frame. All this frames are made individually.

    Attributes:
        parent_data (dict): The data of the parent widget. In this case the parent widget is the main window
        header_options (dict): Some usefull options for the Header Frame
        body_options (dict): Some usefull options for the Body Frame
        footer_options (dict): Some usefull options for the Footer Frame
        police_logo_image (PhotoImage): An image that is going to be displayed on the main header label
        add_image (PhotoImage): An image that is going to be displayed on the footer 'Add File' Button
        parent_widget (Tk): the parent widget of the frame. It is always the main window
        frame (Frame): The actual frame
        header (Frame): The header frame
        header_image (PhotoImage): The image used in the header section as part of the main label
        header_label (Label): The main label that is goin to be displayed on the header
        body (Frame): The body frame
        body_label_message (Label): The message that tells the user to pick a database
        file_picker_area (Canvas): The area where all the stored databases are going to be displayed as buttons
        file_picker_frame (Label): A supporting tool to put all the Excel files buttons on the file_picker_area
        file_picker_scrollbar (Scrollbar): A scrollbar next to the file_picker_area that lets the user scroll through the stored databases
        footer (Frame): The footer frame
        add_file_image (PhotoImage): The styling image of the 'Add File' button in the footer section
        add_file_button (Button): The button that adds a new file in the stored databases
        button_context_menu (Menu): A context menu that appears where the user right clicks on an Excel File button

    Methods:
        __addExcelFile(): Adds a new excel file in the stored databases
        __buildStructure(): Builds the general structure of the frame (Header, Body, Footer)
        __createBodyFrame(): Creates the Body Frame
        __createExcelFileButton(parent, path): Creates a button that corresponds to an Excel File
        __createExcelFileButtonContextMenu(): Creates the context menu of each excel file button
        __createFooterFrame(): Creates the Footer Frame
        __createHeaderFrame(): Creates the Header Frame
        __deleteExcelFileButton(button, index): Removes a file from the stored databases
        __initializeImages(): Initializes some images used in the frame
        __openExcelFile(index): Opens an Excel File
        __openExcelFileFolder(index): Opens the folder containing the Excel File
        __rebuildStructure(): Rebuilds the general structure of the frame
        __setupStructureOptions(data): Sets up the options of the general structure (Header, Body, Footer)
        __showExcelFileButtonContextMenu(event, button, index): Outputs the context menu of each Excel File button
        
    """
    def __init__(self, app_data: dict[str, any]) -> None:
        """
        The constructor of the DatabasePickerFrame class. Here the actual frame and the main structure
        are being build while some additional data are being initialized such as images and some options.

        Args:
            data (dict[str, any]): The data of the parent widget

        """
        # Initializing the basic frame
        super().__init__(app_data)

    def _initializeImages(self) -> None:
        """
        The _initializeImages() method initializes all the images used in the frame.

        """
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.add_image = tk.PhotoImage(file=self.footer_options['add-button-image-path'])

    def _setupStructureOptions(self, data: dict[str, any]) -> None:
        """
        The _setupStructureOptions() method initializes some options for all the three frames that form
        the whole structure of the frame. Some of these options are images, colors, fonts, texts etc.

        Args:
            data (dict[str, any]): The data of the parent widget
        
        """
        self.__createExcelFileButtonContextMenu() # Create the context menu for each button

        # Setting up the Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.application_data['window-width'], self.application_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "message-title": textSpaced("ΓΙΑ  ΣΥΝΕΧΕΙΑ  ΕΠΙΛΕΞΤΕ  ΑΡΧΕΙΟ:"),
            "no-files-message": "ΔΕΝ ΕΧΕΙ ΠΡΟΕΠΙΛΕΓΕΙ\nΚΑΝΕΝΑ ΑΡΧΕΙΟ",
            "message-title-font": ('Arial', round(0.018*max(self.application_data['window-width'], self.application_data['window-height'])), 'bold'),
            "files-font": ('Arial', round(0.011*max(self.application_data['window-width'], self.application_data['window-height']))),
            "no-files-message-font": ('Arial', round(0.02*max(self.application_data['window-width'], self.application_data['window-height'])))
        }

        # Setting up the Footer Options
        self.footer_options = {
            "add-button-text": "ΠΡΟΣΘΗΚΗ ΑΡΧΕΙΟΥ",
            "add-button-image-path": ADD_PNG_PATH,
            "font": ('Arial', round(0.018*max(self.application_data['window-width'], self.application_data['window-height'])))
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

    def __createExcelFileButton(self, parent: tk.Tk, database_path: str) -> tk.Button:
        """
        The __createExcelFileButton() creates a button corresponding to an Excel File.

        Args:
            parent (Tk): The parent widget of the frame. It is always the main window of the application
            database_path (str): The path corresponding to the Excel File in the computer

        Returns:
            Button: The final button ready to be used

        """
        button_width = round(0.022*self.application_data['window-width'])
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
        filetypes = (("Excel files", "*.xls"), ("Excel files", "*.xlsx")) # Define the available file types

        new_file_path = filedialog.askopenfilename(title="Επιλογή Αρχείου", filetypes=filetypes)
        if new_file_path in self.application_data['app-data']['stored-databases']:
            messagebox.showwarning("Ήδη Υπάρχον Αρχείο", f"Το αρχείο {new_file_path} έχει ήδη οριστεί ως προεπιλογή")
            return

        # If there is a new file path then update the stored databases list in the app data json file and in the window data dictionary
        if new_file_path:
            self.application_data['app-data']['stored-databases'].append(new_file_path) # Add the new file path in the stored databases list
            with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
                app_data = json.load(json_file)

            app_data['stored-databases'].append(new_file_path)

            with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file)

        self.__rebuildStructure()

    def __openExcelFileFolder(self, index: int) -> None:
        """
        The __openExcelFileFolder() method opens the folder containing the Excel File of the stored databases on the given index.

        Args:
            index (int): The index to get the correct excel file in the stored databases sequence and open its folder
        
        """
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        folder_path = os.path.dirname(file_path)
        os.startfile(folder_path)

    def __deleteExcelFileButton(self, button: tk.Button, index: int) -> None:
        """
        The __deleteExcelFileButton() method deletes the Excel File button and the actual excel file from the stored databases
        the user has chosen by right clicking on it.

        Args:
            button (Button): The button to be deleted
            index (int): The index corresponding to the correct excel file in the stored databases sequence

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

    def __openExcelFile(self, index: int) -> None:
        """
        The __openExcelFile() method is used to open an Excel File when the user right clicks on its button.

        Args:
            index (int): The index corresponding to the correct excel file in the stored databases sequence
        
        """
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        os.startfile(file_path)

    def __createExcelFileButtonContextMenu(self) -> None:
        """
        The __createExcelFileButtonContextMenu() method creates a context menu for its individual Excel File button.
        The context menu for each button includes options such as 'Open Excel', 'Open Excel Folder' and 'Remove File'.
        
        """
        # Create a context menu for each file button when the user right clicks on it
        self.button_context_menu = tk.Menu(self.frame, tearoff=False)
        self.button_context_menu.add_command(label="Άνοιγμα Excel")
        self.button_context_menu.add_command(label="Άνοιγμα Θέσης Αρχείου")
        self.button_context_menu.add_separator()
        self.button_context_menu.add_command(label='Αφαίρεση Αρχείου')

    def __showExcelFileButtonContextMenu(self, event, button, index) -> None:
        """
        The __showExcelFileButtonContextMenu() method is used to display the context menu of each Excel File button.

        Args:
            event (any): The event corresponds to the mouse cursor position
            button (Button): The button that is been clicked
            index (int): The index corresponding to the correct excel file in the stored databases sequence

        """
        self.button_context_menu.post(event.x_root, event.y_root)
        self.button_context_menu.entryconfigure(0, command=lambda: self.__openExcelFile(index))
        self.button_context_menu.entryconfigure(1, command=lambda: self.__openExcelFileFolder(index))
        self.button_context_menu.entryconfigure(3, command=lambda: self.__deleteExcelFileButton(button, index))

    def _buildStructure(self) -> None:
        """
        The _buildStructure() method builds the general structure of the frame (Header, Body, Footer). It also gain
        all the stored databases so as to be sure if a message such as 'No Files Deteceted' is appropriate to be displayed.
        Finally it displayes all the Excel Files in the stored databases as buttons to the screen.

        """
        self._createHeaderFrame() # First create the header
        self._createBodyFrame() # Then create the body
        self._createFooterFrame() # Finally create the footer

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
            self.body_no_files_message.pack(padx=round(0.27*self.application_data['window-width']), pady=round(0.2*self.application_data['window-height']))

        # Adding all the stored databases as buttons
        button_gap = round(0.015*self.application_data['window-width'])
        for index in range(len(stored_databases)):
            row, column = index // 3, index % 3
            new_button = self.__createExcelFileButton(self.file_picker_frame, stored_databases[index])
            new_button.grid(row=row, column=column, padx=button_gap+5, pady=button_gap+5)
            new_button.bind('<MouseWheel>', lambda e: onMousewheel(e, self.file_picker_area))
            new_button.bind('<Button-3>', lambda event, button=new_button, i=index: self.__showExcelFileButtonContextMenu(event, button, i))

    def __rebuildStructure(self) -> None:
        """
        The __rebuildStructure() method is used to update the display of the frame. First it deletes all the widgets inside it
        and then it builds them again calling the __buildStructure() method.
        
        """
        for child_widget in self.frame.winfo_children():
            child_widget.destroy()
        self._buildStructure()
        self._setupStructureOptions(self.application_data)

    def _createHeaderFrame(self) -> None:
        """
        The _createHeaderFrame() method is used by the __buildStructure() method and it builds the header frame of the main structure.
        It creates a main label with a title and an image of the 'Greek Police Logo' next to it.

        """
        self.header = tk.Frame(self.frame, bg=self.application_data['theme-color']) # Creating the header frame

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
        """
        The _createBodyFrame() method is used by the __buildStructure() method and it builds the body frame of the main structure.
        It creates a message telling the user to pick a database to work with, the general canvas where all the stored databases are going
        to be displayed and a scrollbar in order to let the user have access to all the individual stored databases. Finally it does some binding
        so as to provide a better way of scrolling with the mouse wheel.

        """
        self.body = tk.Frame(self.frame, bg=self.application_data['theme-color']) # Creating the body frame

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
            width=round(0.9*self.application_data['window-width']),
            height=round(0.5*self.application_data['window-height'])
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
        self.file_picker_area.pack(padx=round(0.05*self.application_data['window-width']), pady=round(0.04*self.application_data['window-height']))
        self.file_picker_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.body.pack()

    def _createFooterFrame(self) -> None:
        """
        The _createFooterFrame() method is used by the __buildStructure() method and it builds the footer frame of the main structure.
        It creates an 'Add File' button whick lets the user add a new database into the stored databases.

        """
        self.footer = tk.Frame(self.frame, bg=self.application_data['theme-color']) # Creating the footer frame

        # Creating the 'Add File' button
        self.add_file_image = resizeImage(self.add_image, round(1.3*self.footer_options['font'][1]))
        self.add_file_button = tk.Button(
            self.footer, 
            text=self.footer_options['add-button-text'],
            font=self.footer_options['font'],
            image=self.add_file_image,
            compound=tk.LEFT,
            padx=round(0.7*self.footer_options['font'][1]),
            command=self.__addExcelFile
        )

        # Packing the footer and its widgets
        self.footer.pack()
        self.add_file_button.pack(padx=round(0.028*self.application_data['window-width']))

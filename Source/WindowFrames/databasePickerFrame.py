import json
import tkinter as tk
from support import *
from tkinter import ttk, filedialog, messagebox
        

# The DatabasePickerFrame class stands for the starting frame of the Application
class DatabasePickerFrame:
    def __init__(self, data: dict[str, any]) -> None:
        # Setup the header, body, and footer options and initialize the images used
        self.setupStructureOptions(data)
        self.initializeImages()

        # Creating the actual frame
        self.parent_widget = self.parent_data['window'] # The parent widget is going to be the main window
        self.frame = tk.Frame(self.parent_widget, bg=self.parent_data['theme-color']) # creating the actual frame
        self.frame.pack()

        # Creating the structure of the frame (Header, Body, Footer)
        self.buildStructure()

    def initializeImages(self) -> None:
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.add_image = tk.PhotoImage(file=self.footer_options['add-button-image-path'])

    def setupStructureOptions(self, data: dict[str, any]) -> None:
        self.parent_data = data

        # Setting up the Header Options
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold')
        }

        # Setting up the Body Options
        self.body_options = {
            "message-title": textSpaced("ΓΙΑ  ΣΥΝΕΧΕΙΑ  ΕΠΙΛΕΞΤΕ  ΑΡΧΕΙΟ:"),
            "no-files-message": "ΔΕΝ ΕΧΕΙ ΠΡΟΕΠΙΛΕΓΕΙ\nΚΑΝΕΝΑ ΑΡΧΕΙΟ",
            "message-title-font": ('Arial', round(0.018*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold'),
            "files-font": ('Arial', round(0.011*max(self.parent_data['window-width'], self.parent_data['window-height']))),
            "no-files-message-font": ('Arial', round(0.02*max(self.parent_data['window-width'], self.parent_data['window-height'])))
        }

        # Setting up the Footer Options
        self.footer_options = {
            "add-button-text": "ΠΡΟΣΘΗΚΗ ΑΡΧΕΙΟΥ",
            "add-button-image-path": ADD_PNG_PATH,
            "font": ('Arial', round(0.018*max(self.parent_data['window-width'], self.parent_data['window-height'])))
        }

    def onMousewheel(self, event: any) -> None:
        # Get the current scroll position (as a fraction) relative to the maximum scroll
        current_scroll_frac = self.file_picker_area.yview()[0]

        if event.delta > 0:  # Scrolling upwards
            if current_scroll_frac <= 0.0: return  # Don't scroll further up if already at the top
            self.file_picker_area.yview_scroll(int(-1*(event.delta/120)), "units")
        else:  # Scrolling downwards
            if current_scroll_frac >= 1.0: return  # Don't scroll further down if already at the bottom
            self.file_picker_area.yview_scroll(int(-1*(event.delta/120)), "units")

    def createFileButton(self, parent: tk.Widget, path: str) -> tk.Button:
        button_width = round(0.022*self.parent_data['window-width'])
        new_button = tk.Button(parent, text=getFileName(path), font=self.body_options['files-font'], width=button_width)
        return new_button

    def addFile(self) -> None:
        filetypes = (("Excel files", "*.xls"), ("Excel files", "*.xlsx")) # Define the available file types

        new_file_path = filedialog.askopenfilename(title="Επιλογή Αρχείου", filetypes=filetypes)
        if new_file_path in self.parent_data['app-data']['stored-databases']:
            messagebox.showwarning("Ήδη Υπάρχον Αρχείο", f"Το αρχείο {new_file_path} έχει ήδη οριστεί ως προεπιλογή")
            return

        # If there is a new file path then update the stored databases list in the app data json file and in the window data dictionary
        if new_file_path:
            self.parent_data['app-data']['stored-databases'].append(new_file_path) # Add the new file path in the stored databases list
            with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
                app_data = json.load(json_file)

            app_data['stored-databases'].append(new_file_path)

            with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file)

        self.rebuildStructure()

    def openFileFolder(self, index: int) -> None:
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        folder_path = os.path.dirname(file_path)
        os.startfile(folder_path)

    def deleteFileButton(self, button: tk.Button, index: int) -> None:
        if messagebox.askyesno("Αφαίρεση Προεπιλεγμένου Αρχείου", "Θέλετε σίγουρα να αφαιρέσετε το αρχείο;"):
            button.destroy()
            with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
                app_data = json.load(json_file)
            self.parent_data['app-data']['stored-databases'].pop(index)
            app_data['stored-databases'].pop(index)

            with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(app_data, json_file)
            self.rebuildStructure()

    def openExcelFile(self, index: int) -> None:
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            app_data = json.load(json_file)

        file_path = app_data['stored-databases'][index]
        os.startfile(file_path)

    def createContextMenu(self) -> None:
        # Create a context menu for each file button when the user right clicks on it
        self.button_context_menu = tk.Menu(self.frame, tearoff=False)
        self.button_context_menu.add_command(label="Άνοιγμα Excel")
        self.button_context_menu.add_command(label="Άνοιγμα Θέσης Αρχείου")
        self.button_context_menu.add_separator()
        self.button_context_menu.add_command(label='Αφαίρεση Αρχείου')

    def showContextMenu(self, event, button, index) -> None:
        self.button_context_menu.post(event.x_root, event.y_root)
        self.button_context_menu.entryconfigure(0, command=lambda: self.openExcelFile(index))
        self.button_context_menu.entryconfigure(1, command=lambda: self.openFileFolder(index))
        self.button_context_menu.entryconfigure(3, command=lambda: self.deleteFileButton(button, index))

    def buildStructure(self) -> None:
        self.createHeaderFrame() # First create the header
        self.createBodyFrame() # Then create the body
        self.createFooterFrame() # Finally create the footer
        self.createContextMenu() # Create the context menu for each button

        # Getting the stored databases
        stored_databases = self.parent_data['app-data']['stored-databases']

        # Creating a 'No Files' message if needed
        if len(stored_databases) == 0:
            self.body_no_files_message = tk.Label(
                self.file_picker_frame,
                text=self.body_options["no-files-message"],
                font=self.body_options['no-files-message-font'],
                bg=self.parent_data['theme-color-dark'],
                fg=self.parent_data['theme-color-very-dark']
            )
            self.body_no_files_message.pack(padx=round(0.27*self.parent_data['window-width']), pady=round(0.2*self.parent_data['window-height']))

        # Adding all the stored databases as buttons
        button_gap = round(0.015*self.parent_data['window-width'])
        for index in range(len(stored_databases)):
            row, column = index // 3, index % 3
            new_button = self.createFileButton(self.file_picker_frame, stored_databases[index])
            new_button.grid(row=row, column=column, padx=button_gap+5, pady=button_gap+5)
            new_button.bind('<MouseWheel>', self.onMousewheel)
            new_button.bind('<Button-3>', lambda event, button=new_button, i=index: self.showContextMenu(event, button, i))

    def rebuildStructure(self) -> None:
        for child_widget in self.frame.winfo_children():
            child_widget.destroy()

        self.buildStructure()

    def createHeaderFrame(self) -> None:
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

    def createBodyFrame(self) -> None:
        self.body = tk.Frame(self.frame, bg=self.parent_data['theme-color']) # Creating the body frame

        # Creating the Body Label Message
        self.body_label_message = tk.Label(
            self.body, text=self.body_options['message-title'],
            font=self.body_options['message-title-font'],
            bg=self.parent_data['theme-color'],
            fg=self.parent_data['label-fg-color']
        )

        # Creating the file picker area containing the databases' buttons
        self.file_picker_area = tk.Canvas(
            self.body,
            background=self.parent_data['theme-color-dark'],
            highlightbackground=self.parent_data['theme-color'],
            width=round(0.9*self.parent_data['window-width']),
            height=round(0.5*self.parent_data['window-height'])
        )

        self.file_picker_area.bind('<Configure>', lambda e: self.file_picker_area.configure(scrollregion=self.file_picker_area.bbox("all")))
        self.file_picker_area.bind('<MouseWheel>', self.onMousewheel)

        self.file_picker_frame = ttk.Label(self.file_picker_area, background=self.parent_data['theme-color-dark'])
        self.file_picker_area.create_window((0, 0), window=self.file_picker_frame, anchor=tk.NW)
        self.file_picker_frame.bind('<MouseWheel>', self.onMousewheel)

        # Creating a scrollbar for the file picker area
        self.file_picker_scrollbar = tk.Scrollbar(self.file_picker_area, orient=tk.VERTICAL, command=self.file_picker_area.yview)
        self.file_picker_area.config(yscrollcommand=self.file_picker_scrollbar.set)

        # Packing the body and its widgets
        self.body_label_message.pack()
        self.file_picker_area.pack(padx=round(0.05*self.parent_data['window-width']), pady=round(0.04*self.parent_data['window-height']))
        self.file_picker_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.body.pack()

    def createFooterFrame(self) -> None:
        self.footer = tk.Frame(self.frame, bg=self.parent_data['theme-color']) # Creating the footer frame

        # Creating the 'Add File' button
        self.add_file_image = resizeImage(self.add_image, round(1.3*self.footer_options['font'][1]))
        self.add_file_button = tk.Button(
            self.footer, 
            text=self.footer_options['add-button-text'],
            font=self.footer_options['font'],
            image=self.add_file_image,
            compound=tk.LEFT,
            padx=round(0.7*self.footer_options['font'][1]),
            command=self.addFile
        )

        # Packing the footer and its widgets
        self.footer.pack()
        self.add_file_button.pack(padx=round(0.028*self.parent_data['window-width']))

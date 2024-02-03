import tkinter as tk
import pandas as pd
from initialization import *
from person import Person
from inputField import InputField
from tkinter import ttk


class SearchWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Toplevel()

        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = self.geometry_data['width']
        self.height = self.geometry_data['height']
        self.spawn_x = self.geometry_data['spawn_x']
        self.spawn_y = self.geometry_data['spawn_y']
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Initialize all the font options
        self.font_size = self.geometry_data['font_size']
        self.button_font = ('Arial', int(self.font_size*1.2))

        # Initialize the title, the icon, and the background color of the window
        self.window.title("Αναζήτηση")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

    def on_mousewheel(self, event):
        self.result_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_main_label(self):
        self.main_label_image = resizeImage(self.police_icon_image, int((2/20)*self.height))
        self.main_label = tk.Label(self.window, text="ΑΝΑΖΗΤΗΣΗ ΦΑΚΕΛΩΝ ΜΕ:", font=('Arial', int(self.font_size*(1.2)), 'bold'), fg="white", bg="#2A508C", 
                                   image=self.main_label_image, compound="left", padx=int((1/50)*self.width))
        self.main_label.pack(pady=(1/30)*self.height)

    def create_entry_boxes(self):
        # Defining a general frame that will contain the other two frames
        self.entries_frame = tk.Frame(self.window, bg="#2A508C")
        self.entries_frame.pack()

        # Defining the FolderID frame that will contain the entry box for searching a folder ID with its search button
        self.folderID_frame = tk.Frame(self.entries_frame, bg="#2A508C")
        self.folderID_frame.grid(row=0, column=0, padx=((1/20)*self.width))

        # Defining the Surname frame that will contain the entry box for searching a surname with its search button
        self.surname_frame = tk.Frame(self.entries_frame, bg="#2A508C")
        self.surname_frame.grid(row=0, column=1, padx=((1/20)*self.width))

        # Creating the input field for Folder ID
        self.folderID_entry = InputField(self.folderID_frame, ('Arial', int(self.font_size*(8/10))), 'gray', int((1/100)*self.width), 'Αριθμός Φακέλου', self.searchByFolderID)
        self.folderID_entry.create()
        self.folderID_entry.put()

        # Creating the input field for Surname
        self.surname_entry = InputField(self.surname_frame, ('Arial', int(self.font_size*(8/10))), 'gray', int((1/100)*self.width), 'Επώνυμο', self.searchBySurname)
        self.surname_entry.create()
        self.surname_entry.put()

    def create_no_result_label(self):
        self.no_result_label = tk.Label(self.buttonList_label, text="ΚΑΝΕΝΑ ΑΠΟΤΕΛΕΣΜΑ", font=('Arial', self.font_size), fg="#0D2750", bg="#1C3E73")
        self.no_result_label.pack(pady=int((3/10)*self.height))

    def create_result_canvas(self):
        # Creating the result Canvas containg the main Result Button List frame
        self.result_canvas = tk.Canvas(self.window, width=int((9/10)*self.width), height=int((7/10)*self.height))
        self.result_canvas.pack(padx=int((1/20)*self.width), pady=int((1/25)*self.height))

        # Creating the Result Button List frame
        self.buttonList_label = ttk.Label(self.result_canvas, background="#1C3E73")
        self.result_canvas.create_window((0, 0), window=self.buttonList_label, anchor="nw", width=int((9/10)*self.width))

        # Binding the canvas with additional properties
        self.result_canvas.bind('<MouseWheel>', self.on_mousewheel)

        # Changing the background color of the canvas
        self.result_canvas.config(background="#1C3E73", highlightbackground="#1C3E73")

        # Create the no result label
        self.create_no_result_label()

    def getDataByFolderID(self, value):
        df = pd.read_excel(get_active_database(), header=0)
        filtered_df = df[df['Α.Φ.'] == value]

        return filtered_df

    def getDataBySurname(self, value):
        df = pd.read_excel(get_active_database(), header=0)
        df = df.fillna('')
        filtered_df = df[df['ΕΠΩΝΥΜΟ'].str.startswith(value)]

        return filtered_df

    def searchByFolderID(self):
        def fix_date(date):
            year = date[0:4]; month = date[5:7]; day = date[8:10]
            return f"{day}/{month}/{year}"
        
        # Getting the data from the Database according to the given value of the FolderID Field
        value = self.folderID_entry.entry_box.get()
        data = self.getDataByFolderID(int(value))

        # Cleaning any previous results
        for button in self.buttonList_label.winfo_children(): button.destroy()

        # Checking of the new data are empty
        if data.empty:
            self.create_no_result_label()
            return

        # Creating and Adding the reaults buttons to the canvas
        for i in range(len(data)):
            # Creating a person object with the appropriate data
            info = data.iloc[i]
            
            # Fixing the date field if it is appropriate
            if "-" in str(info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"]): info['ΗΜΕΡ.ΓΕΝΝΗΣΗΣ'] = fix_date(str(info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"]))
            
            # Creating the person object
            person = Person(info["Α.Φ."], info["ΕΠΩΝΥΜΟ"], info["ΟΝΟΜΑ"], info["ΠΑΤΡΩΝΥΜΟ"], info["ΜΗΤΡΩΝΥΜΟ"], info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"], info["ΤΟΠΟΣ ΓΕΝΝΗΣΗΣ"], info["Δ/ΝΣΗ ΚΑΤΟΙΚΙΑΣ"], info["ΠΕΡΙΟΧΗ"], info['ΤΗΛΕΦΩΝΟ'], info['ΕΙΔΟΣ ΕΠΙΧΕΙΡΗΣΗΣ'], info["ΠΑΡΑΤΗΡΗΣΕΙΣ"], info['ΣΧΟΛΙΑ'])
            
            # Creating the text of the button
            if person.father_name == "": string = f"{person.surname} {person.name}"
            else: 
                ending = person.father_name[-2:]
                if ending == "ΗΣ": string = f"{person.surname} {person.name}   του {person.father_name[:-1]}"
                elif ending == "ΑΣ": string = f"{person.surname} {person.name}   του {person.father_name[:-1]}"
                elif ending == "ΟΣ": string = f"{person.surname} {person.name}   του {person.father_name[:-1]}Υ"
                else: string = f"{person.surname} {person.name}   του {person.father_name}"
            
            # Creating the result button and adding it to the Result Button List
            newResultButton = tk.Button(self.buttonList_label, text=string, font=('Arial', int(self.font_size//1.6)), command=person.introduce)
            newResultButton.pack(side="top", fill='x')
            newResultButton.bind('<MouseWheel>', self.on_mousewheel)
        
        self.result_canvas.update_idletasks()
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))


    def searchBySurname(self):
        def fix_date(date):
            year = date[0:4]; month = date[5:7]; day = date[8:10]
            return f"{day}/{month}/{year}"
        
        def upper_case(string):
            upper = []
            for character in string:
                if character.islower(): upper.append(character.upper())
                else: upper.append(character)
            return ''.join(upper)

        # Getting the data from the Database accoriding to the given value of the Surname Input Field
        value = self.surname_entry.entry_box.get()
        data = self.getDataBySurname(upper_case(value))

        # Cleaning any previous results
        for button in self.buttonList_label.winfo_children(): button.destroy()

        # Checking of the new data are empty
        if data.empty:
            self.create_no_result_label()
            return

        # Creating and Adding the reaults buttons to the canvas
        for i in range(len(data)):
            # Creating a person object with the appropriate data
            info = data.iloc[i]
            
            # Fixing the date field if it is appropriate
            if "-" in str(info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"]): info['ΗΜΕΡ.ΓΕΝΝΗΣΗΣ'] = fix_date(str(info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"]))
            
            # Creating the person object
            person = Person(info["Α.Φ."], info["ΕΠΩΝΥΜΟ"], info["ΟΝΟΜΑ"], info["ΠΑΤΡΩΝΥΜΟ"], info["ΜΗΤΡΩΝΥΜΟ"], info["ΗΜΕΡ.ΓΕΝΝΗΣΗΣ"], info["ΤΟΠΟΣ ΓΕΝΝΗΣΗΣ"], info["Δ/ΝΣΗ ΚΑΤΟΙΚΙΑΣ"], info["ΠΕΡΙΟΧΗ"], info['ΤΗΛΕΦΩΝΟ'], info['ΕΙΔΟΣ ΕΠΙΧΕΙΡΗΣΗΣ'], info["ΠΑΡΑΤΗΡΗΣΕΙΣ"], info['ΣΧΟΛΙΑ'])
            
            # Creating the text of the button
            string = f"{i+1})       " if i < 9 else f"{i+1})     "
            if person.father_name == "": string += f"{person.surname} {person.name}"
            else: 
                ending = person.father_name[-2:]
                if ending == "ΗΣ": string += f"{person.surname} {person.name}   του {person.father_name[:-1]}"
                elif ending == "ΑΣ": string += f"{person.surname} {person.name}   του {person.father_name[:-1]}"
                elif ending == "ΟΣ": string += f"{person.surname} {person.name}   του {person.father_name[:-1]}Υ"
                else: string += f"{person.surname} {person.name}   του {person.father_name}"
            
            
            # Creating the result button and adding it to the Result Button List
            newResultButton = tk.Button(self.buttonList_label, anchor="w", text=string, font=('Arial', int(self.font_size//1.6)), command=person.introduce)
            newResultButton.pack(side="top", fill='x')
            newResultButton.bind('<MouseWheel>', self.on_mousewheel)
        
        self.result_canvas.update_idletasks()
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))

    def run(self):
        self.initialize_window() # Initialize a main window
        self.create_main_label() # Create the main label
        self.create_entry_boxes() # Create the entry boxes
        self.create_result_canvas() # Create the result canvas

        self.window.mainloop()
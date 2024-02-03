import tkinter as tk
import math
import xlrd
import xlwt
from initialization import *
from inputField import InputField
from tkinter import messagebox

class Info:
    def __init__(self, label_text, label_font, entry_text, entry_font, parent, width, edit_text=False):
        self.label = tk.Label(parent, text=label_text, font=label_font, fg="white", bg="#2A508C")
        self.entry = tk.Entry(parent, font=entry_font, fg="black", borderwidth=int((1/100)*width))
        self.entry.insert(0, entry_text)
        self.entry.config(state="readonly") if not edit_text else self.entry.config(state="normal")

    def put(self):
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=1, column=0)

class Person:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_
    BACK_LOGO_IMAGE_PATH = BACK_LOGO_IMAGE_PATH_
    SAVE_LOGO_IMAGE_PATH = SAVE_LOGO_IMAGE_PATH_
    DELETE_LOGO_IMAGE_PATH =  DELETE_LOGO_IMAGE_PATH_

    def __init__(self, folderID, surname, name, father_name, mother_name, birthdate, birthplace, address, area, phone, business_type, notes, comments):
        self.folderID = "" if isinstance(folderID, float) and math.isnan(folderID) else folderID
        self.surname = "" if isinstance(surname, float) and math.isnan(surname) else surname
        self.name = "" if isinstance(name, float) and math.isnan(name) else name
        self.father_name = "" if isinstance(father_name, float) and math.isnan(father_name) else father_name
        self.mother_name = "" if isinstance(mother_name, float) and math.isnan(mother_name) else mother_name
        self.birthdate = "" if isinstance(birthdate, float) and math.isnan(birthdate) else birthdate
        self.birthplace = "" if isinstance(birthplace, float) and math.isnan(birthplace) else birthplace
        self.address = "" if isinstance(address, float) and math.isnan(address) else address
        self.area = "" if isinstance(area, float) and math.isnan(area) else area
        self.phone = "" if isinstance(phone, float) and math.isnan(phone) else phone
        self.business_type = "" if isinstance(business_type, float) and math.isnan(business_type) else business_type
        self.notes = "" if isinstance(notes, float) and math.isnan(notes) else notes
        self.comments = "" if isinstance(comments, float) and math.isnan(comments) else comments

    def get_excel_line_number(self):
        wb = xlrd.open_workbook(get_active_database())
        ws = wb.sheet_by_index(0)

        target_value = self.folderID
        row_number = None
        for row in range(ws.nrows):
            for col in range(ws.ncols):
                cell_value = ws.cell_value(row, col)
                if cell_value == target_value:
                    row_number = row + 1
                    break
            if row_number is not None:
                break

        if row_number is not None:
            return row_number

    def initialize_window(self, title):
        # Initialize the window
        self.window = tk.Toplevel()

        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)
        self.back_icon_image = tk.PhotoImage(file=self.BACK_LOGO_IMAGE_PATH)
        self.save_icon_image = tk.PhotoImage(file=self.SAVE_LOGO_IMAGE_PATH)
        self.delete_icon_image = tk.PhotoImage(file=self.DELETE_LOGO_IMAGE_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = self.geometry_data['width']
        self.height = self.geometry_data['height']
        self.spawn_x = self.geometry_data['spawn_x']
        self.spawn_y = self.geometry_data['spawn_y']
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")
        
        # Initialize all the font options
        self.font_size = self.geometry_data['font_size']
        self.main_lebel_font = ('Arial', int(self.font_size*(1.2)), 'Bold')
        self.label_font = ('Arial', int(self.font_size*(0.4)))
        self.entry_font = ('Arial', int(self.font_size*(0.7)))
        self.back_button_font = ("Arial", int(self.font_size*(0.55)))
        self.save_button_font = ("Arial", int(self.font_size*(0.55)))
        self.delete_button_font = ("Arial", int(self.font_size*(0.55)))
        self.notes_font = ('Arial', int(self.font_size*(0.5)))
        self.comments_font = ('Arial', int(self.font_size*(0.7)))

        # Initialize some other usefull options
        self.notes_width_factor = 60
        self.notes_height_factor = 5
        self.comments_width_factor = 45
        self.comments_height_factor = 5
        self.pad_y = int((1/150)*self.width)

        # Initialize the title, the icon, and the background color of the window
        self.window.title(title)
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")
    
    def on_entry(self, event):
        current_index = self.entry_boxes.index(event.widget)
        next_index = (current_index + 1) % len(self.entry_boxes)
        self.entry_boxes[next_index].focus()

    def create_main_label(self, label_text):
        self.main_label_image = resizeImage(self.police_icon_image, int((2/25)*self.width))
        self.main_label = tk.Label(self.window, text=label_text, font=('Arial', int(self.font_size*(1.2)), 'bold'), fg="white", bg="#2A508C",
                                   image=self.main_label_image, compound="left", padx=int((1/50)*self.width))
        self.main_label.pack(pady=(1/50)*self.width)

    def initialize_information(self, edit_text=False, pad_y=0):
        self.entry_boxes = []
        self.general_frame = tk.Frame(self.window, bg="#2A508C")
        self.general_frame.pack(padx=int((1/30)*self.width), pady=pad_y)
        
        # Creating the folderID info
        self.folderID_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.folderID_frame.pack(anchor="w", padx=int((1/50)*self.width), pady=self.pad_y)
        self.folderID_info = Info("ΑΡΙΘΜΟΣ ΦΑΚΕΛΟΥ /1020:", self.label_font, self.folderID, self.entry_font, self.folderID_frame, self.width, edit_text); self.folderID_info.put()
        self.entry_boxes.append(self.folderID_info.entry); self.folderID_info.entry.bind('<Return>', self.on_entry); self.folderID_info.entry.bind('<Tab>', self.on_entry)

        # Creating the Surname and name info
        self.fullname_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.fullname_frame.pack(pady=self.pad_y)
        self.surname_frame = tk.Frame(self.fullname_frame, bg="#2A508C"); self.surname_frame.grid(row=0, column=0, padx=int((1/50)*self.width))
        self.surname_info = Info("ΕΠΩΝΥΜΟ:", self.label_font, self.surname, self.entry_font, self.surname_frame, self.width, edit_text); self.surname_info.put()
        self.name_frame = tk.Frame(self.fullname_frame, bg="#2A508C"); self.name_frame.grid(row=0, column=1, padx=int((1/50)*self.width))
        self.name_info = Info("ΟΝΟΜΑ:", self.label_font, self.name, self.entry_font, self.name_frame, self.width, edit_text); self.name_info.put()
        self.entry_boxes.append(self.surname_info.entry); self.surname_info.entry.bind('<Return>', self.on_entry); self.surname_info.entry.bind('<Tab>', self.on_entry)
        self.entry_boxes.append(self.name_info.entry); self.name_info.entry.bind('<Return>', self.on_entry); self.name_info.entry.bind('<Tab>', self.on_entry)

        # Creating the father and mother names
        self.father_mother_name_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.father_mother_name_frame.pack(pady=self.pad_y)
        self.father_name_frame = tk.Frame(self.father_mother_name_frame, bg="#2A508C"); self.father_name_frame.grid(row=0, column=0, padx=int((1/50)*self.width))
        self.father_name_info = Info("ΠΑΤΡΩΝΥΜΟ:", self.label_font, self.father_name, self.entry_font, self.father_name_frame, self.width, edit_text); self.father_name_info.put()
        self.mother_name_frame = tk.Frame(self.father_mother_name_frame, bg="#2A508C"); self.mother_name_frame.grid(row=0, column=1, padx=int((1/50)*self.width))
        self.mother_name_info = Info("ΜΗΤΡΩΝΥΜΟ:", self.label_font, self.mother_name, self.entry_font, self.mother_name_frame, self.width, edit_text); self.mother_name_info.put()
        self.entry_boxes.append(self.father_name_info.entry); self.father_name_info.entry.bind('<Return>', self.on_entry); self.father_name_info.entry.bind('<Tab>', self.on_entry)
        self.entry_boxes.append(self.mother_name_info.entry); self.mother_name_info.entry.bind('<Return>', self.on_entry); self.mother_name_info.entry.bind('<Tab>', self.on_entry)

        # Creating the birth info
        self.birth_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.birth_frame.pack(pady=self.pad_y)
        self.birthdate_frame = tk.Frame(self.birth_frame, bg="#2A508C"); self.birthdate_frame.grid(row=0, column=0, padx=int((1/50)*self.width))
        self.birthdate_info = Info("ΗΜΕΡΟΜΗΝΙΑ ΓΕΝΝΗΣΗΣ:", self.label_font, self.birthdate, self.entry_font, self.birthdate_frame, self.width, edit_text); self.birthdate_info.put()
        self.birthplace_frame = tk.Frame(self.birth_frame, bg="#2A508C"); self.birthplace_frame.grid(row=0, column=1, padx=int((1/50)*self.width))
        self.birthplace_info = Info("ΤΟΠΟΣ ΓΕΝΝΗΣΗΣ:", self.label_font, self.birthplace, self.entry_font, self.birthplace_frame, self.width, edit_text); self.birthplace_info.put()
        self.entry_boxes.append(self.birthdate_info.entry); self.birthdate_info.entry.bind('<Return>', self.on_entry); self.birthdate_info.entry.bind('<Tab>', self.on_entry)
        self.entry_boxes.append(self.birthplace_info.entry); self.birthplace_info.entry.bind('<Return>', self.on_entry); self.birthplace_info.entry.bind('<Tab>', self.on_entry)

        # Creating the address info
        self.address_area_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.address_area_frame.pack(pady=self.pad_y)
        self.address_frame = tk.Frame(self.address_area_frame, bg="#2A508C"); self.address_frame.grid(row=0, column=0, padx=int((1/50)*self.width))
        self.address_info = Info("ΔΙΕΥΘΥΝΣΗ ΚΑΤΟΙΚΙΑΣ:", self.label_font, self.address, self.entry_font, self.address_frame, self.width, edit_text); self.address_info.put()
        self.area_frame = tk.Frame(self.address_area_frame, bg="#2A508C"); self.area_frame.grid(row=0, column=1, padx=int((1/50)*self.width))
        self.area_info = Info("ΠΕΡΙΟΧΗ:", self.label_font, self.area, self.entry_font, self.area_frame, self.width, edit_text); self.area_info.put()
        self.entry_boxes.append(self.address_info.entry); self.address_info.entry.bind('<Return>', self.on_entry); self.address_info.entry.bind('<Tab>', self.on_entry)
        self.entry_boxes.append(self.area_info.entry); self.area_info.entry.bind('<Return>', self.on_entry); self.area_info.entry.bind('<Tab>', self.on_entry)

        # Creating the phone and the business type info
        self.phone_business_frame = tk.Frame(self.general_frame, bg="#2A508C"); self.phone_business_frame.pack(pady=self.pad_y)
        self.phone_frame = tk.Frame(self.phone_business_frame, bg="#2A508C"); self.phone_frame.grid(row=0, column=0, padx=int((1/50)*self.width))
        self.phone_info = Info("ΤΗΛΕΦΩΝΟ:", self.label_font, str(self.phone)[:-2], self.entry_font, self.phone_frame, self.width, edit_text); self.phone_info.put()
        self.business_type_frame = tk.Frame(self.phone_business_frame, bg="#2A508C"); self.business_type_frame.grid(row=0, column=1, padx=int((1/50)*self.width))
        self.business_type_info = Info("ΕΙΔΟΣ ΕΠΙΧΕΙΡΗΣΗΣ:", self.label_font, self.business_type, self.entry_font, self.business_type_frame, self.width, edit_text); self.business_type_info.put()
        self.entry_boxes.append(self.phone_info.entry); self.phone_info.entry.bind('<Return>', self.on_entry); self.phone_info.entry.bind('<Tab>', self.on_entry)
        self.entry_boxes.append(self.business_type_info.entry); self.business_type_info.entry.bind('<Return>', self.on_entry); self.business_type_info.entry.bind('<Tab>', self.on_entry)

        # Creating the notes info
        self.notes_frame = tk.Frame(self.window, bg="#2A508C"); self.notes_frame.pack(padx=int((1/30)*self.width), pady=self.pad_y)
        self.notes_label = tk.Label(self.notes_frame, text="ΠΑΡΑΤΗΡΗΣΕΙΣ:", font=self.label_font, fg="white", bg="#2A508C")
        self.notes_text_area = tk.Text(self.notes_frame, font=self.notes_font, fg="black", borderwidth=int((1/100)*self.width), width=int(self.general_frame.winfo_width()*self.notes_width_factor), height=int(self.general_frame.winfo_height()*self.notes_height_factor))
        self.notes_text_area.insert('1.0', self.notes)
        self.notes_text_area.config(state="disabled") if not edit_text else self.notes_text_area.config(state="normal")
        self.notes_label.pack(anchor="w")
        self.entry_boxes.append(self.notes_text_area); self.notes_text_area.bind('<Return>', self.on_entry); self.notes_text_area.bind('<Tab>', self.on_entry)
        self.notes_text_area.pack()

        # Creating the comments info
        self.comments_frame = tk.Frame(self.window, bg="#2A508C"); self.comments_frame.pack(padx=int((1/30)*self.width), pady=self.pad_y)
        self.comments_label = tk.Label(self.comments_frame, text="ΣΧΟΛΙΑ:", font=self.label_font, fg="white", bg="#2A508C")
        self.comments_text_area = tk.Text(self.comments_frame, font=self.comments_font, fg="black", borderwidth=int((1/100)*self.width), width=int(self.general_frame.winfo_width()*self.comments_width_factor), height=int(self.general_frame.winfo_height()*self.comments_height_factor))
        self.comments_text_area.insert('1.0', self.comments)
        self.comments_text_area.config(state="disabled") if not edit_text else self.comments_text_area.config(state="normal")
        self.comments_label.pack(anchor="w")
        self.entry_boxes.append(self.comments_text_area); self.comments_text_area.bind('<Return>', self.on_entry); self.comments_text_area.bind('<Tab>', self.on_entry)
        self.comments_text_area.pack()

    def fixDate(self, date):
        new_date = date.replace("-", "/")
        return new_date

    def save_information(self):
        # Checking if the folderID and the surname entries are empty
        if self.folderID_info.entry.get().strip() == "" or self.surname_info.entry.get().strip() == "":
            self.window.attributes('-topmost', False)
            messagebox.showerror("Μη Καθορισμένα Δεδομένα", "Τα πεδία 'ΑΡΙΘΜΟΣ ΦΑΚΕΛΟΥ' και 'ΕΠΩΝΥΜΟ' πρέπει να είναι συμπληρωμένα.")
            self.window.attributes('-topmost', True)
            return

        # Creating a new person object
        correct_date = self.fixDate(self.birthdate_info.entry.get())
        new_person = Person(self.folderID_info.entry.get(), self.surname_info.entry.get(), self.name_info.entry.get(), self.father_name_info.entry.get(), self.mother_name_info.entry.get(), correct_date, self.birthplace_info.entry.get(), self.address_info.entry.get(), self.area_info.entry.get(), self.phone_info.entry.get(), self.business_type_info.entry.get(), self.notes_text_area.get('1.0', tk.END), self.comments_text_area.get('1.0', tk.END))
        
        # Open the existing Excel file for reading
        workbook = xlrd.open_workbook(get_active_database())
        sheet = workbook.sheet_by_index(0)

        # Read the data and convert date values
        existing_data = []
        for row in range(sheet.nrows):
            row_data = []
            if row + 1 == self.nline_in_excel: continue
            for col in range(sheet.ncols):
                cell_value = sheet.cell(row, col).value
                
                # Check if the cell contains a date value
                if sheet.cell_type(row, col) == xlrd.XL_CELL_DATE:
                    
                    # Convert the date value to a tuple (year, month, day, hour, minute, second)
                    date_tuple = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
                    
                    # Convert the tuple to a formatted date string
                    formatted_date = "{:04d}/{:02d}/{:02d}".format(*date_tuple[:3])
                    year = formatted_date[0:4]; month = formatted_date[5:7]; day = formatted_date[8:10]
                    formatted_date = f"{day}/{month}/{year}"
                    row_data.append(formatted_date)
                else:
                    row_data.append(cell_value)
            existing_data.append(row_data)
        
        # Add new data to the list
        new_data = [int(new_person.folderID), new_person.surname, new_person.name, new_person.father_name, new_person.mother_name, new_person.birthdate, new_person.birthplace, new_person.address, new_person.area, new_person.phone, new_person.business_type, new_person.notes[:-1], new_person.comments[:-1]]
        existing_data.append(new_data)

        # Create a new Workbook for writing the updated data
        new_workbook = xlwt.Workbook()
        new_sheet = new_workbook.add_sheet('Sheet1')
        for row_idx, row_data in enumerate(existing_data):
            for col_idx, cell_value in enumerate(row_data):
                new_sheet.write(row_idx, col_idx, cell_value)
        new_workbook.save(get_active_database())

        self.window.destroy()
        self.update_window.destroy()
    
    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.window, bg="#2A508C"); self.buttons_frame.pack()

        self.save_icon = resizeImage(self.save_icon_image, int((20/10)*self.save_button_font[1]))
        self.save_button = tk.Button(self.buttons_frame, text=" ΑΠΟΘΗΚΕΥΣΗ ΔΙΟΡΘΩΣΗΣ ", font=self.save_button_font, padx=int((1/100)*self.width), pady=int((1/100)*self.height),
                                       image=self.save_icon, compound="left", command=self.save_information)
        self.save_button.grid(row=0, column=0, pady=self.pad_y*5, padx=int((1/50)*self.width))

        self.delete_icon = resizeImage(self.delete_icon_image, int((20/10)*self.delete_button_font[1]))
        self.delete_button = tk.Button(self.buttons_frame, text=" ΔΙΑΓΡΑΦΗ ΤΩΝ ΣΤΟΙΧΕΙΩΝ ", font=self.delete_button_font, padx=int((1/100)*self.width), pady=int((1/107)*self.height),
                                       image=self.delete_icon, compound="left", command=self.delete_folder)
        self.delete_button.grid(row=0, column=1, pady=self.pad_y*5, padx=int((1/50)*self.width))

        self.back_icon = resizeImage(self.back_icon_image, int((25/10)*self.back_button_font[1]))
        self.back_button = tk.Button(self.buttons_frame, text="ΠΙΣΩ  ", font=self.back_button_font, padx=int((1/50)*self.width), pady=int((1/150)*self.height),
                                     image=self.back_icon, compound="left", command=self.close_window)
        self.back_button.grid(row=1, column=0, pady=int((3/5)*self.pad_y), padx=int((1/30)*self.width), columnspan=2)

    def delete_folder(self):
        # Asking the user if he/she wants to delete the folder for sure
        if not messagebox.askyesno("Διαγραφή Φακέλου;", "Ο φάκελος πρόκειται να διαγραφτεί οριστικά. Θέλετε σίγουρα να συνεχίσετε;"): return

        # Open the existing Excel file for reading
        workbook = xlrd.open_workbook(get_active_database())
        sheet = workbook.sheet_by_index(0)

        # Read the data and convert date values
        existing_data = []
        for row in range(sheet.nrows):
            row_data = []
            if row + 1 == self.nline_in_excel: continue
            for col in range(sheet.ncols):
                cell_value = sheet.cell(row, col).value
                
                # Check if the cell contains a date value
                if sheet.cell_type(row, col) == xlrd.XL_CELL_DATE:
                    
                    # Convert the date value to a tuple (year, month, day, hour, minute, second)
                    date_tuple = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
                    
                    # Convert the tuple to a formatted date string
                    formatted_date = "{:04d}/{:02d}/{:02d}".format(*date_tuple[:3])
                    year = formatted_date[0:4]; month = formatted_date[5:7]; day = formatted_date[8:10]
                    formatted_date = f"{day}/{month}/{year}"
                    row_data.append(formatted_date)
                else:
                    row_data.append(cell_value)
            existing_data.append(row_data)

        # Create a new Workbook for writing the updated data
        new_workbook = xlwt.Workbook()
        new_sheet = new_workbook.add_sheet('Sheet1')
        for row_idx, row_data in enumerate(existing_data):
            for col_idx, cell_value in enumerate(row_data):
                new_sheet.write(row_idx, col_idx, cell_value)
        new_workbook.save(get_active_database())

        self.window.destroy()
        self.update_window.destroy()

    def close_window(self):
        self.window.destroy()

    def introduce(self):
        self.initialize_window("Εμφάνιση Στοιχείων Ατομικού Φακέλου") # Initialize a main window
        self.create_main_label("ΕΜΦΑΝΙΣΗ ΣΤΟΙΧΕΙΩΝ ΦΑΚΕΛΟΥ") # Create the main label
        self.initialize_information() # Initialize the information for the person

        self.window.mainloop()
    
    def update(self, update_window):
        self.initialize_window("Διόρθωση ή Διαγραφή Στοιχείων Ατομικού Φακέλου") # Initialize a main window
        self.create_main_label("ΔΙΟΡΘΩΣΗ ή ΔΙΑΓΡΑΦΗ\nΣΤΟΙΧΕΙΩΝ ΦΑΚΕΛΟΥ") # Create the main label
        self.initialize_information(edit_text=True, pad_y=0) # Initialize the information for the person

        self.create_buttons() # Create the buttons

        self.update_window = update_window
        self.nline_in_excel = self.get_excel_line_number()
        self.window.mainloop()

    def __str__(self):
        text = f"FolderID: {self.folderID}\nSurname: {self.surname}\nName: {self.name}\nFatherName: {self.father_name}\nMotherName: {self.mother_name}\nBirthDate: {self.birthdate}\nBirthPlace: {self.birthplace}\nAddress: {self.address}\nArea: {self.area}\nPhone: {self.phone}\nNotes: {self.notes}\nComments: {self.comments}"
        return text
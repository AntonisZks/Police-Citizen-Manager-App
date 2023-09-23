import tkinter as tk
import math

correctInsertion = lambda item: "" if (item is None) or (isinstance(item, float) and math.isnan(item)) else item


def createSmallInfo(parent_widget, options, label_text, entry_text, entry_state, row, column):
    frame = tk.Frame(parent_widget, background=options['bg'])
    frame.grid(row=row, column=column, padx=options['info-padx'], pady=options['info-pady'])
    label = tk.Label(frame, text=label_text, font=options['label-font'], fg=options['fg'], bg=options['bg'])
    entry = tk.Entry(frame, font=options['entry-font'], borderwidth=options['entry-border-width'])
    entry.insert(0, entry_text)
    entry.config(state=entry_state)
    label.grid(row=0, column=0, sticky=tk.W)
    entry.grid(row=1, column=0, sticky=tk.W)


def createBigInfo(parent_widget, options, label_text, text_area_text, text_area_state):
    frame = tk.Frame(parent_widget, background=options['bg'])
    frame.pack(anchor=tk.W, padx=options['info-padx'], pady=options['info-pady'])
    label = tk.Label(frame, text=label_text, font=options['label-font'], fg=options['fg'], bg=options['bg'])
    text_area = tk.Text(frame, font=options['text-area-font'], borderwidth=options['text-area-border-width'], width=options['big-info-width'],
                        height=options['big-info-height'])
    text_area.insert('1.0', text_area_text)
    text_area.config(state=text_area_state)
    label.grid(row=0, column=0, sticky=tk.W)
    text_area.grid(row=1, column=0, sticky=tk.W)


class Record:
    def __init__(self, folderID: str, surname: str, name: str, father_name: str, mother_name: str,
                 birthdate: str, birthplace: str, address: str, area: str, phone: str, business_type: str, notes: str, comments: str) -> None:
        self.folderID = correctInsertion(folderID)
        self.surname = correctInsertion(surname)
        self.name = correctInsertion(name)
        self.father_name = correctInsertion(father_name)
        self.mother_name = correctInsertion(mother_name)
        self.birthdate = correctInsertion(birthdate)
        self.birthplace = correctInsertion(birthplace)
        self.address = correctInsertion(address)
        self.area = correctInsertion(area)
        self.phone = correctInsertion(phone)
        self.business_type = correctInsertion(business_type)
        self.notes = correctInsertion(notes)
        self.comments = correctInsertion(comments)

    def createDataFrame(self, parent_widget, app_data):
        frame = tk.Frame(parent_widget, background=app_data['theme-color-dark'])
        frame.pack()

        options = {
            "info-padx": round(0.01 * app_data['window-width']),
            "info-pady": round(0.005 * app_data['window-height']),
            "label-font": ('Arial', round(0.010 * app_data['window-width'])),
            "fg": "white",
            "bg": app_data['theme-color-dark'],
            "entry-font": ('Arial', round(0.015 * app_data['window-width'])),
            "text-area-font": ('Arial', round(0.015 * app_data['window-width'])),
            "entry-border-width": round(0.005 * app_data['window-width']),
            "text-area-border-width": round(0.005 * app_data['window-width']),
            'big-info-width': round(0.041 * app_data['window-width']),
            'big-info-height': round(0.005 * app_data['window-width'])
        }

        primary_data_frame = tk.Frame(frame, background=options['bg'], pady=round(0.01 * app_data['window-height']))
        primary_data_frame.pack()

        createSmallInfo(primary_data_frame, options, "ΑΡΙΘΜΟΣ ΦΑΚΕΛΟΥ: 1020/", self.folderID, "readonly", 0, 0)
        createSmallInfo(primary_data_frame, options, "ΕΠΩΝΥΜΟ:", self.surname, "readonly", 1, 0)
        createSmallInfo(primary_data_frame, options, "ΟΝΟΜΑ:", self.name, "readonly", 1, 1)
        createSmallInfo(primary_data_frame, options, "ΠΑΤΡΩΝΥΜΟ:", self.father_name, "readonly", 2, 0)
        createSmallInfo(primary_data_frame, options, "ΜΗΤΡΩΝΥΜΟ:", self.mother_name, "readonly", 2, 1)
        createSmallInfo(primary_data_frame, options, "ΗΜΕΡΟΜΗΝΙΑ ΓΕΝΝΗΣΗΣ:", self.birthdate, "readonly", 3, 0)
        createSmallInfo(primary_data_frame, options, "ΤΟΠΟΣ ΓΕΝΝΗΣΗΣ:", self.birthplace, "readonly", 3, 1)
        createSmallInfo(primary_data_frame, options, "ΔΙΕΥΘΥΝΣΗ ΚΑΤΟΙΚΙΑΣ:", self.address, "readonly", 4, 0)
        createSmallInfo(primary_data_frame, options, "ΠΕΡΙΟΧΗ:", self.area, "readonly", 4, 1)
        createSmallInfo(primary_data_frame, options, "ΤΗΛΕΦΩΝΟ:", self.phone, "readonly", 5, 0)
        createSmallInfo(primary_data_frame, options, "ΕΙΔΟΣ ΕΠΙΧΕΙΡΗΣΗΣ:", self.business_type, "readonly", 5, 1)

        secondary_data_frame = tk.Frame(frame, background=options['bg'])
        secondary_data_frame.pack()

        createBigInfo(secondary_data_frame, options, "ΠΑΡΑΤΗΡΗΣΕΙΣ", self.notes, "disabled")
        createBigInfo(secondary_data_frame, options, "ΣΧΟΛΙΑ", self.comments, "disabled")

        return frame

    def __str__(self):
        text = f"""FolderID: {self.folderID}\n
                   Surname: {self.surname}\n
                   Name: {self.name}\n
                   FatherName: {self.father_name}\n
                   MotherName: {self.mother_name}\n
                   BirthDate: {self.birthdate}\n
                   BirthPlace: {self.birthplace}\n
                   Address: {self.address}\n
                   Area: {self.area}\n
                   Phone: {self.phone}\n
                   Notes: {self.notes}\n
                   Comments: {self.comments} """

        return text

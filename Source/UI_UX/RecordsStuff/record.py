import math
from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.dataHolderField import SmallDataHolderField, BigDataHolderField


correctInsertion = lambda item: "" if (item is None) or (isinstance(item, float) and math.isnan(item)) else item


class Record:
    def __init__(self, folderID: str, surname: str, name: str, father_name: str, mother_name: str,
                 birthdate: str, birthplace: str, address: str, area: str, phone: str, business_type: str, notes: str, comments: str) -> None:
        self.folderID = correctInsertion(folderID)
        self.surname, self.name = correctInsertion(surname), correctInsertion(name)
        self.father_name, self.mother_name = correctInsertion(father_name), correctInsertion(mother_name)
        self.birthdate, self.birthplace = correctInsertion(birthdate), correctInsertion(birthplace)
        self.address, self.area = correctInsertion(address), correctInsertion(area)
        self.phone, self.business_type = correctInsertion(phone), correctInsertion(business_type)
        self.notes, self.comments = correctInsertion(notes), correctInsertion(comments)

    def createDataFrame(self, parent_widget: tk.Widget, app_data: dict[str, Any]):
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

        # Creating the two general frames that will hold the Data Holders (primary_data_frame, secondary_data_frame)
        primary_data_frame = tk.Frame(frame, background=options['bg'], pady=round(0.01 * app_data['window-height']))
        primary_data_frame.pack()

        secondary_data_frame = tk.Frame(frame, background=options['bg'])
        secondary_data_frame.pack()

        # Creating the Data Holders
        index = 0
        for row in range(6):
            for column in range(2):
                if not (row == 0 and column == 1):
                    SmallDataHolderField(primary_data_frame, options, COLUMNS_NAMES[index], list(vars(self).values())[index], "readonly", "", row, column).put()
                    index += 1

        for index in range(11, 13):
            BigDataHolderField(secondary_data_frame, options, COLUMNS_NAMES[11], list(vars(self).values())[index], "disabled", "").put()

        return frame

    @staticmethod
    def createEmptyDataFrame(parent_widget: tk.Widget, app_data: dict[str, Any]):
        frame = tk.Frame(parent_widget, background=app_data['theme-color-dark'])
        frame.pack()

        options = {
            "info-padx": round(0.02 * app_data['window-width']), "info-pady": round(0.005 * app_data['window-height']),
            "label-font": ('Arial', round(0.015 * app_data['window-width'])),
            "fg": "white", "bg": app_data['theme-color-dark'],
            "entry-font": ('Arial', round(0.018 * app_data['window-width'])), "text-area-font": ('Arial', round(0.013 * app_data['window-width'])),
            "entry-border-width": round(0.005 * app_data['window-width']), "text-area-border-width": round(0.005 * app_data['window-width']),
            'big-info-width': round(0.066 * app_data['window-width']), 'big-info-height': round(0.005 * app_data['window-width'])
        }

        # Creating the two general frames that will hold the Data Holders (primary_data_frame, secondary_data_frame)
        primary_data_frame = tk.Frame(frame, background=options['bg'], pady=round(0.01 * app_data['window-height']))
        primary_data_frame.pack()

        secondary_data_frame = tk.Frame(frame, background=options['bg'])
        secondary_data_frame.pack()

        # Creating the Data Holders
        index = 0
        dataHolders = []
        placeHolders = ['', '', '', '', '', 'DD/MM/YY', 'π.χ. Αθήνα', 'π.χ. Ακροπόλεως 51', 'π.χ. Χαλάνδρι', '10-ψήφιος αριθμός', '', '', '']
        for row in range(6):
            for column in range(2):
                if not (row == 0 and column == 1):
                    dataHolder = SmallDataHolderField(primary_data_frame, options, COLUMNS_NAMES[index], "", "normal", placeHolders[index], row, column)
                    dataHolders.append(dataHolder.dataHolder)  # TODO: change the item inside the append() method to the actual dataHolder object and not its attribute
                    dataHolder.put()
                    index += 1

        for index in range(11, 13):
            dataHolder = BigDataHolderField(secondary_data_frame, options, COLUMNS_NAMES[11], "", "normal", placeHolders[index])
            dataHolders.append(dataHolder.dataHolder)  # TODO: change the item inside the append() method to the actual dataHolder object and not its attribute
            dataHolder.put()

        return frame, dataHolders

    def __repr__(self):
        text = f"""FolderID: {self.folderID}\n
                   Surname: {self.surname}\nName: {self.name}\n
                   FatherName: {self.father_name}\nMotherName: {self.mother_name}\n
                   BirthDate: {self.birthdate}\nBirthPlace: {self.birthplace}\n
                   Address: {self.address}\nArea: {self.area}\n
                   Phone: {self.phone}\nBusiness Type: {self.business_type}\n
                   Notes: {self.notes}\nComments: {self.comments}
                """
        return text

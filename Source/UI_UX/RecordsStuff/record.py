"""
The 'record.py' file contains the Record class, which implements a record of a person. It stores the data of every person that are required for the application.
These data are 'folder id', 'surname', 'name', 'father name', 'mother name', 'birthdate', 'birthplace', 'address', 'area', 'phone', 'business type', 'notes' and 'comments'.
The class also contains two special method that create a form of that data. Specifically the createDataFrame() method takes the person's data and creates a basic frame that
contains a bunch of dataHolderFields where they contain those data, making sure of course the user cannot change them. On the other hand, the createEmptyDataFrame() returns
the same frame, but this time it doesn't contain any data. Instead, the frame allows the user to enter their new data in it, and that's why it is a static method.

"""

from tkinter import Frame

from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.dataHolderFields import SmallDataHolderField, BigDataHolderField


correctInsertion = lambda item: "" if (item is None) or (isinstance(item, float) and math.isnan(item)) else item


class Record:
    def __init__(self, folderID: str, surname: str, name: str, father_name: str, mother_name: str, birthdate: str, birthplace: str, address: str, area: str, phone: str, business_type: str, notes: str, comments: str) -> None:
        """ The constructor of the Record class. Here all the person's data are being initialized and stored.

        Args:
            folderID: The person's folder id
            surname: The person's surname
            name: The person's name
            father_name: The person's father name
            mother_name: The person's mother name
            birthdate: The person's birthdate
            birthplace: The person's birthplace
            address: The person's address
            area: The person's area living
            phone: The person's phone number
            business_type: The person's type of business
            notes: Some notes about the person
            comments: Some comments about the person

        """

        self.folderID = correctInsertion(folderID)
        self.surname, self.name = correctInsertion(surname), correctInsertion(name)
        self.father_name, self.mother_name = correctInsertion(father_name), correctInsertion(mother_name)
        self.birthdate, self.birthplace = correctInsertion(birthdate), correctInsertion(birthplace)
        self.address, self.area = correctInsertion(address), correctInsertion(area)
        self.phone, self.business_type = correctInsertion(phone), correctInsertion(business_type)
        self.notes, self.comments = correctInsertion(notes), correctInsertion(comments)

        self.databaseIndex = None

    def createDataFrame(self, parent_widget: tk.Widget, applicationSettings: dict[str, Any], edit: bool = False) -> tk.Frame:
        """ Creates a frame containing a form representing the record's data inside dataHolderFields.

        Args:
            parent_widget (tkinter.Widget): The widget containing the frame.
            applicationSettings (dict[str, Any]): The settings of the application.
            edit (bool): Declares if editing the record's data is allowed.

        """

        # Creating the main frame
        frame = tk.Frame(parent_widget, background=applicationSettings['theme-color-dark'])
        frame.pack()

        # Initialize some settings of the form inside the frame
        formSettings = {
            "info-padx": round(0.01 * applicationSettings['window-width']),
            "info-pady": round(0.005 * applicationSettings['window-height']),
            "label-font": ('Arial', round(0.010 * applicationSettings['window-width'])),
            "fg": "white",
            "bg": applicationSettings['theme-color-dark'],
            "entry-font": ('Arial', round(0.015 * applicationSettings['window-width'])),
            "text-area-font": ('Arial', round(0.015 * applicationSettings['window-width'])),
            "entry-border-width": round(0.005 * applicationSettings['window-width']),
            "text-area-border-width": round(0.005 * applicationSettings['window-width']),
            'big-info-width': round(0.041 * applicationSettings['window-width']),
            'big-info-height': round(0.006 * applicationSettings['window-width'])
        }

        # Creating the two general frames that will hold the Data Holders (primary_data_frame, secondary_data_frame)
        primary_data_frame = tk.Frame(frame, background=formSettings['bg'], pady=round(0.01 * applicationSettings['window-height']))
        primary_data_frame.pack()

        secondary_data_frame = tk.Frame(frame, background=formSettings['bg'])
        secondary_data_frame.pack()

        # Creating the Data Holders
        index = 0
        fieldState = "readonly" if not edit else "normal"
        for row in range(6):
            for column in range(2):
                if not (row == 0 and column == 1):
                    SmallDataHolderField(primary_data_frame, formSettings, COLUMNS_NAMES[index], list(vars(self).values())[index], fieldState, "", row, column).put()  # Create a small data holder field and put it onto the scene
                    index += 1

        fieldState = "disabled" if not edit else "normal"
        for index in range(11, 13):
            BigDataHolderField(secondary_data_frame, formSettings, COLUMNS_NAMES[index], list(vars(self).values())[index], fieldState, "").put()  # Create a small data holder field and put it onto the scene

        return frame

    @staticmethod
    def createEmptyDataFrame(parent_widget: tk.Widget, applicationSettings: dict[str, Any]) -> tuple[Frame, list[SmallDataHolderField | BigDataHolderField]]:
        """ Creates an empty form ready to be filled by the user.

        Args:
            parent_widget (tkinter.Widget): The widget containing the frame
            applicationSettings (dict[str, Any]): The settings of the application

        Returns:
            tkinter.Frame, list[SmallDataHolderField | BigDataHolderField]

        """

        # Creating the main frame
        frame = tk.Frame(parent_widget, background=applicationSettings['theme-color-dark'])
        frame.pack()

        # Initialize some settings of the form inside the frame
        options = {
            "info-padx": round(0.02 * applicationSettings['window-width']), "info-pady": round(0.005 * applicationSettings['window-height']),
            "label-font": ('Arial', round(0.015 * applicationSettings['window-width'])),
            "fg": "white", "bg": applicationSettings['theme-color-dark'],
            "entry-font": ('Arial', round(0.018 * applicationSettings['window-width'])), "text-area-font": ('Arial', round(0.013 * applicationSettings['window-width'])),
            "entry-border-width": round(0.005 * applicationSettings['window-width']), "text-area-border-width": round(0.005 * applicationSettings['window-width']),
            'big-info-width': round(0.066 * applicationSettings['window-width']), 'big-info-height': round(0.005 * applicationSettings['window-width'])
        }

        # Creating the two general frames that will hold the Data Holders (primary_data_frame, secondary_data_frame)
        primary_data_frame = tk.Frame(frame, background=options['bg'], pady=round(0.01 * applicationSettings['window-height']))
        primary_data_frame.pack()

        secondary_data_frame = tk.Frame(frame, background=options['bg'])
        secondary_data_frame.pack()

        # Creating the Data Holders
        index = 0
        dataHolderFields = []
        placeHolders = ['', '', '', '', '', 'DD/MM/YYYY', 'π.χ. Αθήνα', 'π.χ. Ακροπόλεως 51', 'π.χ. Χαλάνδρι', '10-ψήφιος αριθμός', '', '', '']
        for row in range(6):
            for column in range(2):
                if not (row == 0 and column == 1):
                    dataHolderField = SmallDataHolderField(primary_data_frame, options, COLUMNS_NAMES[index], "", "normal", placeHolders[index], row, column)
                    dataHolderFields.append(dataHolderField)
                    dataHolderField.put()
                    index += 1

        for index in range(11, 13):
            dataHolderField = BigDataHolderField(secondary_data_frame, options, COLUMNS_NAMES[index], "", "normal", placeHolders[index])
            dataHolderFields.append(dataHolderField)
            dataHolderField.put()

        return frame, dataHolderFields

    def __repr__(self) -> str:
        """ A supporting method for testing only.

        Returns:
            str
        """

        text = f"""FolderID: {self.folderID}\n
                   Surname: {self.surname}\nName: {self.name}\n
                   FatherName: {self.father_name}\nMotherName: {self.mother_name}\n
                   BirthDate: {self.birthdate}\nBirthPlace: {self.birthplace}\n
                   Address: {self.address}\nArea: {self.area}\n
                   Phone: {self.phone}\nBusiness Type: {self.business_type}\n
                   Notes: {self.notes}\nComments: {self.comments}
                """
        return text

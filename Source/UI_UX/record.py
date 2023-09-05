import math


class Record:
    def __init__(self, folderID: str, surname: str, name: str, father_name: str, mother_name: str,
                birthdate: str, birthplace: str, address: str, area: str, phone: str, business_type: str, notes: str, comments: str) -> None:
        self.folderID = "" if (folderID is None) or (isinstance(folderID, float) and math.isnan(folderID)) else folderID
        self.surname = "" if (surname is None) or (isinstance(surname, float) and math.isnan(surname)) else surname
        self.name = "" if (name is None) or (isinstance(name, float) and math.isnan(name)) else name
        self.father_name = "" if (father_name is None) or (isinstance(father_name, float) and math.isnan(father_name)) else father_name
        self.mother_name = "" if (mother_name is None) or (isinstance(mother_name, float) and math.isnan(mother_name)) else mother_name
        self.birthdate = "" if (birthdate is None) or (isinstance(birthdate, float) and math.isnan(birthdate)) else birthdate
        self.birthplace = "" if (birthplace is None) or (isinstance(birthplace, float) and math.isnan(birthplace)) else birthplace
        self.address = "" if (address is None) or (isinstance(address, float) and math.isnan(address)) else address
        self.area = "" if (area is None) or (isinstance(area, float) and math.isnan(area)) else area
        self.phone = "" if (phone is None) or (isinstance(phone, float) and math.isnan(phone)) else phone
        self.business_type = "" if (business_type is None) or (isinstance(business_type, float) and math.isnan(business_type)) else business_type
        self.notes = "" if (notes is None) or (isinstance(notes, float) and math.isnan(notes)) else notes
        self.comments = "" if (comments is None) or (isinstance(comments, float) and math.isnan(comments)) else comments

    def __str__(self):
        text = f"FolderID: {self.folderID}\nSurname: {self.surname}\nName: {self.name}\nFatherName: {self.father_name}\nMotherName: {self.mother_name}\nBirthDate: {self.birthdate}\nBirthPlace: {self.birthplace}\nAddress: {self.address}\nArea: {self.area}\nPhone: {self.phone}\nNotes: {self.notes}\nComments: {self.comments}"
        return text
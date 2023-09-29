import re
from Source.UI_UX.RecordsStuff.dataHolderFields import SmallDataHolderField, BigDataHolderField
from tkinter import messagebox


class RecordsManager:
	def __init__(self):
		pass

	@staticmethod
	def validData(data: list[SmallDataHolderField | BigDataHolderField]) -> bool:

		# Checking if the folderID and surname fields are filled
		data[0].removePlaceHolder()
		if data[0].dataHolder.get() == "":
			messagebox.showerror("Ελλιπή Στοιχεία", "Το πεδίο 'Αριθμός Φακέλου' πρέπει να είναι συμπληρωμένο")
			data[0].dataHolder.focus()
			return False

		data[1].removePlaceHolder()
		if data[1].dataHolder.get() == "":
			messagebox.showerror("Ελλιπή Στοιχεία", "Το πεδίο 'Επώνυμο' πρέπει να είναι συμπληρωμένο")
			data[1].dataHolder.focus()
			return False

		# Checking if the given date agrees with the Data Prototype
		datePattern = r'\b\d{2}/\d{2}/\d{4}\b'

		data[5].removePlaceHolder()
		if data[5].dataHolder.get() != "" and not re.match(datePattern, data[5].dataHolder.get()):
			messagebox.showerror("Μη Έγκυρη Ημερομηνία", f"Το πεδίο 'Ημερομηνία Γέννησης' ωφείλει να ικανοποιεί το πρότυπο DD/MM/YY. Η τιμή '{data[5].dataHolder.get()}' δεν το ικανοποιεί. Το πεδίο μπορεί να είναι κενό")
			data[5].dataHolder.focus()
			return False

		# Checking if the given phone number is valid
		data[9].removePlaceHolder()
		if data[9].dataHolder.get() != "" and len(data[9].dataHolder.get()) != 10:
			messagebox.showerror(f"Μη Έγκυρος Αριθμός Τηλεφώνου", f"Ο αριθμός τηλεφώνου '{data[9].dataHolder.get()}' δεν είναι έγκυρος. Ο αριθμός πρέπει να είναι 10-ψήφιος. Το πεδίο μπορεί να είναι κενό")
			data[9].dataHolder.focus()
			return False

		# Adding all the placeholders again
		for dataHolderField in data:
			dataHolderField.addPlaceHolder()

		return True

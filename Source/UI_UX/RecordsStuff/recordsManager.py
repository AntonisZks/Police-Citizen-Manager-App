"""
The 'recordManager.py' file includes the basic RecordManager class, which contains several useful methods to manage the application records. Specifically we can access to all the records, insert new records to databases,
check for records' validation or even delete records from databases. All these ideas are implemented in suitable static methods.

"""

import re
import pandas as pd
from Source.UI_UX.RecordsStuff.dataHolderFields import SmallDataHolderField, BigDataHolderField
from tkinter import messagebox
from typing import Any
from functools import singledispatchmethod


class RecordsManager:

	@staticmethod
	def getRecordsFromDatabase(database: str) -> pd.DataFrame:
		"""	Gains access to the records of the given database and returns a pandas Data Frame with these records. """

		data_df = pd.read_excel(database)  # Getting the data from the given database
		data_df = data_df.fillna('')       # This command makes sure that the NaN values in the Excel are filled with ''

		return data_df

	@staticmethod
	def saveRecordToDatabase(record: list[str | Any], database: str) -> None:
		"""	Saves one record into the given database. """

		data_df = pd.read_excel(database)   # Getting the data from the given database
		data_df.loc[len(data_df)] = record  # Adding the record to the end of the dataframe

		# Save the dataframe to the database
		data_df.to_excel(database, index=False)

	@staticmethod
	def saveRecordsToDatabase(records: list[list[str | Any]], database: str) -> None:
		""" Saves several records into the given database. """

		data_df = pd.read_excel(database)  # Getting the data from the given database

		# Adding each record to the end of the dataframe
		for record in records:
			data_df.loc[len(data_df)] = record

		# Save the dataframe to the database
		data_df.to_excel(database, index=False)

	@staticmethod
	def updateDataInDatabase(records: list[list[str | Any]], recordsIndexes: list[int], database: str) -> None:
		""" Updates the given data into the given database. """

		database_df = pd.read_excel(database)  # Getting the data from the given database
		for record in records:
			database_df.loc[len(database_df)] = record

		# Delete the lines corresponding to the selected records form the dataframe
		for index in recordsIndexes:
			database_df = database_df.drop(index)

		# Store the dataframe to the database
		database_df.to_excel(database, index=False)

	@staticmethod
	def deleteRecordsFromDatabase(recordsIndexes: list[int], database: str):
		""" Deletes the given records' line indexes from the given database. """

		database_df = RecordsManager.getRecordsFromDatabase(database)  # Creating a dataframe containing all the records in the database

		# Delete the lines corresponding to the selected records form the dataframe
		for index in recordsIndexes:
			database_df = database_df.drop(index)

		database_df.to_excel(database, index=False)  # Store the data frame to the database

	@singledispatchmethod
	def __validData(self, data: Any) -> None:
		""" Polymorphism method to implement other editions of validData(). """

		raise NotImplementedError(f"{type(data)} is not supported as a type of argument in validData().")

	@staticmethod
	@__validData.register
	def validData(data: list[SmallDataHolderField | BigDataHolderField]) -> bool:
		""" Checks if the given data are valid according to the application record's data prototypes. """

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

	@staticmethod
	@__validData.register
	def validData(data: list[str | Any]) -> bool:
		""" Checks if the given data are valid according to the application record's data prototypes. """

		# Checking if the folderID and surname fields are filled
		if data[0] == "":
			messagebox.showerror("Ελλιπή Στοιχεία", "Το πεδίο 'Αριθμός Φακέλου' πρέπει να είναι συμπληρωμένο")
			return False

		if data[1] == "":
			messagebox.showerror("Ελλιπή Στοιχεία", "Το πεδίο 'Επώνυμο' πρέπει να είναι συμπληρωμένο")
			return False

		# Checking if the given date agrees with the Data Prototype
		datePattern = r'\b\d{2}/\d{2}/\d{4}\b'

		if data[5] != "" and not re.match(datePattern, data[5]):
			messagebox.showerror("Μη Έγκυρη Ημερομηνία", f"Το πεδίο 'Ημερομηνία Γέννησης' ωφείλει να ικανοποιεί το πρότυπο DD/MM/YY. Η τιμή '{data[5]}' δεν το ικανοποιεί. Το πεδίο μπορεί να είναι κενό")
			return False

		# Checking if the given phone number is valid
		if data[9] != "" and len(data[9]) != 10:
			messagebox.showerror(f"Μη Έγκυρος Αριθμός Τηλεφώνου", f"Ο αριθμός τηλεφώνου '{data[9]}' δεν είναι έγκυρος. Ο αριθμός πρέπει να είναι 10-ψήφιος. Το πεδίο μπορεί να είναι κενό")
			return False

		return True

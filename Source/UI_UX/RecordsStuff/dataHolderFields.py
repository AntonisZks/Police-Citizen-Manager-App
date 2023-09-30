"""
The 'dataHolderFields.py' file contains the classes referred to dataHolderFields that are mostly used in record forms. The file contains the basic abstract class 'IDataHolderFrame',
which provides the standard characteristics of a data holder field. These are its parent widget, label text, its data holder text, its state, its placeholder and its row and column
to be put. It also provides some additional methods that are all abstract they have to do with the functionality of the data holder field. These are addPlaceHolder(), removePlaceHolder(),
_build(), _focusIn(), _focusOut(), put() and getData().

"""

import tkinter as tk
from abc import ABC, abstractmethod
from typing import Any, Literal


class DataHolderField(ABC):
	def __init__(self, parentWidget: tk.Widget, dataSettings: dict[str, Any], labelText: str, dataHolderText: str, dataHolderState: str | Literal["normal", "disabled", "readonly"], placeHolder: str, row: int = 0, column: int = 0) -> None:
		""" The constructor of the DataHolderField. It initializes the basic characteristics of the data holder field.

		Args:
			parentWidget (tkinter.Widget): The widget containing the data holder field
			dataSettings (dict[str, Any]): The settings of the field
			labelText (str): The text of the label
			dataHolderText (str): The text of the data holder
			dataHolderState (str): The state of the data holder
			placeHolder (str): the text of the placeholder
			row (int): The row to be placed
			column (int): The column to be placed
		"""

		self.dataHolder = None  # Temporary initialization of the data holder

		self.parentWidget, self.dataSettings = parentWidget, dataSettings
		self.labelText, self.dataHolderText = labelText, dataHolderText
		self.dataHolderState, self.placeHolder = dataHolderState, placeHolder
		self.row, self.column = row, column

	@abstractmethod
	def addPlaceHolder(self) -> None:
		""" Abstract method to add a placeholder to the field. Each data holder field has a different way of implementing this method. """

	@abstractmethod
	def removePlaceHolder(self) -> None:
		""" Abstract method to remove the placeholder from the field. Each data holder field has a different way of removing the placeholder. """

	@abstractmethod
	def _focusIn(self, event) -> None:
		""" Abstract method to focus in, on the field. Each data holder frame has a different approach to that. """

	@abstractmethod
	def _focusOut(self, event) -> None:
		""" Abstract method to focus out,  of the field. Each data holder frame has a different approach to that. """

	@abstractmethod
	def _build(self) -> None:
		""" Abstract method to build the field. Each data holder field has a different architecture. So each one implements itw own _build() method. """

	@abstractmethod
	def put(self) -> None:
		""" Abstract method to pack the field to the scene. Each data holder frame has a different approach to that. """

	@abstractmethod
	def getData(self) -> str:
		""" Abstract method to get the data of the field. Each data holder frame has a different approach to that. """


class SmallDataHolderField(DataHolderField):
	def __init__(self, parentWidget: tk.Widget, dataSettings: dict[str, Any], labelText: str = "", dataHolderText: str = "", dataHolderState: str | Literal["normal", "disabled", "readonly"] = "normal", placeHolder: str = "", row: int = 0, column: int = 0) -> None:
		""" The constructor of the SmallDataHolderField. Calls the constructor of the parent class and also builds the data holder field. """

		super().__init__(parentWidget, dataSettings, labelText, dataHolderText, dataHolderState, placeHolder, row, column)
		self._build()  # Build the data holder field

	def _build(self) -> None:
		""" Builds the data holder field. The field consists of two parts. A label and an entry called 'data holder'. The field is actually a frame that contains these
			two parts of the whole data holder field. """

		# Create a basic Frame
		self.frame = tk.Frame(self.parentWidget, background=self.dataSettings['bg'])

		# Creating the label and the entry (data holder)
		self.label = tk.Label(self.frame, text=self.labelText, font=self.dataSettings['label-font'], fg=self.dataSettings['fg'], bg=self.dataSettings['bg'])
		self.dataHolder = tk.Entry(self.frame, font=self.dataSettings['entry-font'], borderwidth=self.dataSettings['entry-border-width'])
		self.dataHolder.insert(0, self.dataHolderText)
		self.dataHolder.config(state=self.dataHolderState)

		# Packing the label and the data holder
		self.label.grid(row=0, column=0, sticky=tk.W)
		self.dataHolder.grid(row=1, column=0, sticky=tk.W)

		# Placing a placeholder if needed
		if self.placeHolder != "":
			self.addPlaceHolder()

	def addPlaceHolder(self) -> None:
		""" Adds a placeholder to the field. """

		# Adding the placeholder
		if self.dataHolder.get() == "":
			self.dataHolder.insert(0, self.placeHolder)
			self.dataHolder.config(fg='gray')
			self.dataHolder.bind("<FocusIn>", self._focusIn)
			self.dataHolder.bind("<FocusOut>", self._focusOut)

	def removePlaceHolder(self) -> None:
		""" Removes the placeholder from the field. """

		if self.dataHolder.get() == self.placeHolder:
			self.dataHolder.delete(0, tk.END)

	def _focusIn(self, event) -> None:
		""" Executes a 'focus in' command to the field. """

		# Removes the placeholder if needed
		if self.dataHolder.get() == self.placeHolder:
			self.dataHolder.delete(0, tk.END)
			self.dataHolder.config(fg='black')

	def _focusOut(self, event) -> None:
		""" Executes a 'focus out' command to the field. """

		# Adds the placeholder if needed
		if self.dataHolder.get() == "":
			self.dataHolder.insert(0, self.placeHolder)
			self.dataHolder.config(fg='gray')

	def getData(self) -> str:
		""" Returns the data contained by the field. """

		return self.dataHolder.get()

	def put(self):
		""" Packs the field to the scene on the appropriate row and column. """

		self.frame.grid(row=self.row, column=self.column, padx=self.dataSettings['info-padx'], pady=self.dataSettings['info-pady'])


class BigDataHolderField(DataHolderField):
	def __init__(self, parentWidget: tk.Widget, dataSettings: dict[str, Any], labelText: str = "", dataHolderText: str = "", dataHolderState: str | Literal["normal", "disabled", "readonly"] = "normal", placeHolder: str = "", row: int = 0, column: int = 0):
		""" The constructor of the BigDataHolderField. Calls the constructor of the parent class and also builds the data holder field. """

		super().__init__(parentWidget, dataSettings, labelText, dataHolderText, dataHolderState, placeHolder, row, column)
		self._build()

	def _build(self):
		""" Builds the data holder field. The field consists of two parts. A label and an entry called 'data holder'. The field is actually a frame that contains these
			two parts of the whole data holder field. """

		self.frame = tk.Frame(self.parentWidget, background=self.dataSettings['bg'])

		self.label = tk.Label(self.frame, text=self.labelText, font=self.dataSettings['label-font'], fg=self.dataSettings['fg'], bg=self.dataSettings['bg'])
		self.dataHolder = tk.Text(self.frame, font=self.dataSettings['text-area-font'], borderwidth=self.dataSettings['text-area-border-width'], width=self.dataSettings['big-info-width'], height=self.dataSettings['big-info-height'])
		self.dataHolder.insert('1.0', self.dataHolderText)
		self.dataHolder.config(state=self.dataHolderState)

		self.label.grid(row=0, column=0, sticky=tk.W)
		self.dataHolder.grid(row=1, column=0, sticky=tk.W)

		if self.placeHolder != "":
			self.addPlaceHolder()

	def addPlaceHolder(self):
		""" Adds a placeholder to the field. """

		if self.dataHolder.get('1.0', tk.END) == "":
			self.dataHolder.insert('1.0', self.placeHolder)
			self.dataHolder.config(fg='gray')
			self.dataHolder.bind("<FocusIn>", self._focusIn)
			self.dataHolder.bind("<FocusOut>", self._focusOut)

	def removePlaceHolder(self):
		""" Removes the placeholder from the field. """

		if self.dataHolder.get('1.0', tk.END) == self.placeHolder:
			self.dataHolder.delete('1.0', tk.END)

	def _focusIn(self, event) -> None:
		""" Executes a 'focus in' command to the field. """

		if self.dataHolder.get('1.0', tk.END) == self.placeHolder:
			self.dataHolder.delete(0, tk.END)
			self.dataHolder.config(fg='black')

	def _focusOut(self, event) -> None:
		""" Executes a 'focus out' command to the field. """

		if self.dataHolder.get('1.0', tk.END) == "":
			self.dataHolder.insert(0, self.placeHolder)
			self.dataHolder.config(fg='gray')

	def getData(self):
		""" Returns the data contained by the field. """

		return self.dataHolder.get('1.0', tk.END)

	def put(self):
		""" Packs the field to the scene on the appropriate row and column. """

		self.frame.pack(anchor=tk.W, padx=self.dataSettings['info-padx'], pady=self.dataSettings['info-pady'])

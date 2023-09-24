import tkinter as tk
from abc import ABC, abstractmethod


class DataHolderField(ABC):
	def __init__(self, parentWidget, dataOptions, labelText, dataHolderText, dataHolderState, placeHolder, row=0, column=0):
		self.dataHolder = None

		self.parentWidget = parentWidget
		self.dataOptions = dataOptions
		self.labelText = labelText
		self.dataHolderText = dataHolderText
		self.dataHolderState = dataHolderState
		self.placeHolder = placeHolder
		self.row = row
		self.column = column

	@abstractmethod
	def _addPlaceHolder(self):
		pass

	@abstractmethod
	def _focusIn(self, event):
		pass

	@abstractmethod
	def _focusOut(self, event):
		pass

	@abstractmethod
	def _build(self):
		pass

	@abstractmethod
	def put(self):
		pass


class SmallDataHolderField(DataHolderField):
	def __init__(self, parentWidget, dataOptions, labelText, dataHolderText, dataHolderState, placeHolder, row=0, column=0):
		super().__init__(parentWidget, dataOptions, labelText, dataHolderText, dataHolderState, placeHolder, row, column)
		self._build()

	def _build(self):
		self.frame = tk.Frame(self.parentWidget, background=self.dataOptions['bg'])

		self.label = tk.Label(self.frame, text=self.labelText, font=self.dataOptions['label-font'], fg=self.dataOptions['fg'], bg=self.dataOptions['bg'])
		self.dataHolder = tk.Entry(self.frame, font=self.dataOptions['entry-font'], borderwidth=self.dataOptions['entry-border-width'])
		self.dataHolder.insert(0, self.dataHolderText)
		self.dataHolder.config(state=self.dataHolderState)

		self.label.grid(row=0, column=0, sticky=tk.W)
		self.dataHolder.grid(row=1, column=0, sticky=tk.W)

		if self.placeHolder != "":
			self._addPlaceHolder()

	def _addPlaceHolder(self):
		self.dataHolder.insert(0, self.placeHolder)
		self.dataHolder.config(fg='gray')
		self.dataHolder.bind("<FocusIn>", self._focusIn)
		self.dataHolder.bind("<FocusOut>", self._focusOut)

	def _focusIn(self, event) -> None:
		if self.dataHolder.get() == self.placeHolder:
			self.dataHolder.delete(0, tk.END)
			self.dataHolder.config(fg='black')

	def _focusOut(self, event) -> None:
		if self.dataHolder.get() == "":
			self.dataHolder.insert(0, self.placeHolder)
			self.dataHolder.config(fg='gray')

	def put(self):
		self.frame.grid(row=self.row, column=self.column, padx=self.dataOptions['info-padx'], pady=self.dataOptions['info-pady'])


class BigDataHolderField(DataHolderField):
	def __init__(self, parentWidget, dataOptions, labelText, dataHolderText, dataHolderState, placeHolder, row=0, column=0):
		super().__init__(parentWidget, dataOptions, labelText, dataHolderText, dataHolderState, placeHolder, row, column)
		self._build()

	def _build(self):
		self.frame = tk.Frame(self.parentWidget, background=self.dataOptions['bg'])

		self.label = tk.Label(self.frame, text=self.labelText, font=self.dataOptions['label-font'], fg=self.dataOptions['fg'], bg=self.dataOptions['bg'])
		self.dataHolder = tk.Text(self.frame, font=self.dataOptions['text-area-font'], borderwidth=self.dataOptions['text-area-border-width'], width=self.dataOptions['big-info-width'], height=self.dataOptions['big-info-height'])
		self.dataHolder.insert('1.0', self.dataHolderText)
		self.dataHolder.config(state=self.dataHolderState)

		self.label.grid(row=0, column=0, sticky=tk.W)
		self.dataHolder.grid(row=1, column=0, sticky=tk.W)

		if self.placeHolder != "":
			self._addPlaceHolder()

	def _addPlaceHolder(self):
		self.dataHolder.insert('1.0', self.placeHolder)
		self.dataHolder.config(fg='gray')
		self.dataHolder.bind("<FocusIn>", self._focusIn)
		self.dataHolder.bind("<FocusOut>", self._focusOut)

	def _focusIn(self, event) -> None:
		if self.dataHolder.get('1.0', tk.END) == self.placeHolder:
			self.dataHolder.delete(0, tk.END)
			self.dataHolder.config(fg='black')

	def _focusOut(self, event) -> None:
		if self.dataHolder.get('1.0', tk.END) == "":
			self.dataHolder.insert(0, self.placeHolder)
			self.dataHolder.config(fg='gray')

	def put(self):
		self.frame.pack(anchor=tk.W, padx=self.dataOptions['info-padx'], pady=self.dataOptions['info-pady'])

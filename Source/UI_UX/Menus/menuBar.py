import tkinter as tk


class MainApplicationWindowMenuBar(tk.Menu):
	def __init__(self, parentWidget: tk.Tk):
		super().__init__(parentWidget)

		self.parentWidget = parentWidget
		self.parentWidget.config(menu=self)
		self.__build()

	def __build(self):
		self.__createFileSubMenu()  # Creating the 'File' submenu
		self.__createEditSubMenu()  # Creating the 'Edit' submenu
		self.__createHelpSubMenu()  # Creating the 'Help' submenu

	def __createFileSubMenu(self):
		self.fileMenu = tk.Menu(self, tearoff=0)
		self.fileMenu.add_cascade(label="Έξοδος", command=self.parentWidget.onClosing)
		self.add_cascade(label="Αρχείο", menu=self.fileMenu)

	def __createEditSubMenu(self):
		self.editMenu = tk.Menu(self, tearoff=0)
		self.add_cascade(label="Επεξεργασία", menu=self.editMenu)

	def __createHelpSubMenu(self):
		self.helpMenu = tk.Menu(self, tearoff=0)
		self.add_cascade(label="Βοήθεια", menu=self.helpMenu)

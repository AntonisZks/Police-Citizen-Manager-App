"""
The 'insertFrame.py' file contains the InsertFrame class, which represents the insert frame of the application. This frame allows the user to create a new form,
which contains the data of a Person ('Folder ID', 'Surname', 'Name', 'Father name', 'Mother name', etc.) and add it into the current database they work with at
that time. The frame makes sure that the fields 'Folder ID' and 'Surname' must be filled and the that the field 'Birthdate' and 'Phone number' agree with prototypes
of them. I f the user enters something wrong, the insertion stops, and a related message appears on the screen and describes what exactly went wrong during the insertion
of the data. The form the user has to fill is consists of several entries called dataHolderFields, where they have a main label describing what to insert, and an entry box
so as the user enters the data inside it. All the previous are implemented with specific methods.

"""

from tkinter import messagebox
from Source.UI_UX.Frames.frame import IFrame
from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.record import Record
from Source.UI_UX.RecordsStuff.recordsManager import RecordsManager


class InsertFrame(IFrame):
	""" The InsertFrame class represents the insert frame of the application where the user can create a new form of
    	a new person's data and add it to the database.

    Attributes:
        applicationSettings (dict[str, Any]): Settings related to the application.

    Methods:
        __init__() -> None: Constructor for the InsertFrame class. Initializes the frame and scrollbar object.
        _initializeImages() -> None: Initializes the images used in the frame.
        _setupStructureOptions() -> None: Sets up the options for the frame's structure.
        __goToMainMenu() -> None: Changes the active frame to the Main Menu one.
        __validInputData() -> bool: Checks if the data entered by the user are valid for insertion.
        __saveRecord() -> None: Saves the new person's data entered by the user if they are valid.
        __resetStructure(): Resets the structure of the frame by destroying all children widgets and rebuilding it.
        _buildStructure() -> None: Builds the general structure of the insert frame.
        _createHeaderFrame() -> None: Creates the Header Frame, which contains the main label and logo.
        _createBodyFrame() -> None: Creates the Body Frame, which contains the form for the user to fill.
        _createFooterFrame() -> None: Creates the Footer of the frame with 'Return' and 'Save' buttons.

    """

	def __init__(self, applicationSettings: dict[str, Any]) -> None:
		""" Constructor for the InsertFrame class. The constructor of the InsertFrame calls the constructor of the base class IFrame
			and initializes a scrollbar object to None.

		Args:
			applicationSettings (dict[str, Any]): Settings related to the application.

		"""
		# Initializing the basic frame
		super().__init__(applicationSettings)

		self.record_area_scrollbar = None  # Initialize a temporary variable for the side scrollbar

	def _initializeImages(self) -> None:
		""" Initializes some all the images used in the frame. """

		self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
		self.return_logo_image = tk.PhotoImage(file=self.footer_options['return-button-image-path'])
		self.save_logo_image = tk.PhotoImage(file=self.footer_options['save-button-image-path'])

	def _setupStructureOptions(self, parentWidgetSettings: dict[str, Any]) -> None:
		""" Sets up the options for the frame's structure.

		Args:
			parentWidgetSettings (dict[str, Any]): Data related to the application.

		"""

		# Setting up the Header Options
		self.header_options = {
			"title": "ΚΑΤΑΧΩΡΗΣΗ ΣΤΟΙΧΕΙΩΝ ΦΑΚΕΛΟΥ",
			"image-path": POLICE_LOGO_PNG_PATH,
			"font": ('Arial', round(0.022 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height'])), 'bold')
		}

		# Setting up the Body Options
		self.body_options = {
			"empty-form-padx": round(0.04 * self.applicationSettings['window-width']),
			"empty-form-pady": round(0.04 * self.applicationSettings['window-height']),
			"title": "Σ Υ Μ Π Λ Η Ρ Ω Σ Η   Φ Ο Ρ Μ Α Σ",
			"title-font": ('Arial', round(0.022 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height'])), 'bold', 'italic', 'underline'),
			"title-pady": round(0.02 * self.applicationSettings['window-height'])
		}

		# Setting up the Footer Options
		self.footer_options = {
			"return-button-text": " ΕΠΙΣΤΡΟΦΗ ΣΤΟ ΜΕΝΟΥ ",
			"return-button-font": ('Arial', round(0.013 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
			"return-button-image-path": RETURN_PNG_PATH,
			"return-button-padx-inner": round(0.01 * self.applicationSettings['window-width']),
			"return-button-pady-inner": round(0.005 * self.applicationSettings['window-height']),
			"return-button-padx-outer": round(0.01 * self.applicationSettings['window-width']),
			"return-button-pady-outer": round(0.012 * self.applicationSettings['window-height']),
			"save-button-text": " ΑΠΟΘΗΚΕΥΣΗ ΣΤΟΙΧΕΙΩΝ ",
			"save-button-font": ('Arial', round(0.012 * max(self.applicationSettings['window-width'], self.applicationSettings['window-height']))),
			"save-button-image-path": SAVE_PNG_PATH,
			"save-button-padx-inner": round(0.01 * self.applicationSettings['window-width']),
			"save-button-pady-inner": round(0.005 * self.applicationSettings['window-height']),
			"save-button-padx-outer": round(0.01 * self.applicationSettings['window-width']),
			"save-button-pady-outer": round(0.013 * self.applicationSettings['window-height']),

			"buttons-frame-pady": round(0.020 * self.applicationSettings['window-height'])
		}

	def __goToMainMenu(self) -> None:
		""" Changes the active frame to the Main Menu one. """

		self.app.setActiveFrame(self.app.mainMenuFrame)

	def __saveRecord(self) -> None:
		""" Saves the new person's data the user entered if they are valid of course. The method first gains access to the data of the current database
			the user is working with, and after that it checks whether the data are valid in order to continue. If so, the method adds the new data to a temporary
			'Pandas' dataframe and then saves this dataframe into an Excel file which is the same file from where the data were gained at first. After the insertion
			is completed the method a message appears on the screen saying that the insertion was successful. """

		# Checking if the user entered valid inputs in the form
		if not RecordsManager.validData(self.dataHolderFields):
			# Adding all the placeholders again
			for dataHolderField in self.dataHolderFields:
				dataHolderField.addPlaceHolder()

			return

		# Removing all the placeholders
		for dataHolderField in self.dataHolderFields:
			dataHolderField.removePlaceHolder()

		# Getting the new data
		new_data = []
		for dataHolderField in self.dataHolderFields:
			value = dataHolderField.getData().replace("\n", "")
			new_data.append(value)

		# Adding the new data to the dataframe
		RecordsManager.saveRecordToDatabase(new_data, self.applicationSettings['app-data']['active-database'])

		# Adding all the placeholders again
		for dataHolderField in self.dataHolderFields:
			dataHolderField.addPlaceHolder()

		# Successful Data Insertion and resetting the frame
		messagebox.showinfo("Επιτυχής Καταχώρηση", "Τα στοιχεία καταχωρήθηκαν με επιτυχία!")
		self.__resetStructure()

	def __resetStructure(self):
		""" Resets the structure of the frame. Specifically it destroys all the children widgets of the frame, and then it calls the
			method _buildStructure() again. """

		for childWidget in self.winfo_children():
			childWidget.destroy()

		self._buildStructure()

	def _buildStructure(self) -> None:
		""" Builds the general structure of the search frame (Header, Body, Footer). """

		self._createHeaderFrame()  # First create the header
		self._createBodyFrame()  # Then create the body
		self._createFooterFrame()  # Finally, create the footer

	def _createHeaderFrame(self) -> None:
		""" Creates the Header Frame, which contains the main label and logo. """

		self.header = tk.Frame(self, bg=self.applicationSettings['theme-color'])  # Creating the header frame

		# Creating the Header Label
		self.header_image = resizeImage(self.police_logo_image, round(0.10 * self.applicationSettings['window-width']))
		self.header_label = tk.Label(
			self.header,
			text=self.header_options['title'],
			font=self.header_options['font'],
			bg=self.applicationSettings['theme-color'],
			fg=self.applicationSettings['label-fg-color'],
			image=self.header_image, compound=tk.LEFT,
			padx=round(0.04 * self.applicationSettings['window-width']),
			pady=round(0.04 * (self.applicationSettings['window-height']))
		)

		# Packing the header and its widgets
		self.header_label.pack()
		self.header.pack()

	def _createBodyFrame(self) -> None:
		""" Creates the Body Frame, which contains the basic form the user has to fill. The form consists of some special objects called dataHolderFields
			which consists of two parts. A label describing the input type and an entry box where the value is being entered inside it. The user has to fill
			those dataHolderFields (not all of them) and then they can insert the data they entered inside the database. """

		self.body = tk.Frame(self, bg=self.applicationSettings["theme-color-dark"])
		self.body.pack()

		# Creating a title
		self.titleLabel = tk.Label(self.body, text=self.body_options["title"], font=self.body_options["title-font"], bg=self.applicationSettings["theme-color-dark"], fg=self.applicationSettings['label-fg-color'])
		self.titleLabel.pack(pady=(self.body_options["title-pady"], 0))

		# Creating an empty form the user has to fill
		frame, self.dataHolderFields = Record.createEmptyDataFrame(self.body, self.applicationSettings)
		frame.pack(padx=self.body_options["empty-form-padx"], pady=(0, self.body_options["empty-form-pady"]))

		# Binding the entries in order to have access to each one using the keyboard 'Return' and 'Tab' buttons
		for dataHolder in self.dataHolderFields:
			dataHolder.dataHolder.bind('<Return>', lambda e: onEntry(e, self.dataHolderFields))
			dataHolder.dataHolder.bind('<Tab>', lambda e: onEntry(e, self.dataHolderFields))

		# Binding the last entry (Comments One) in order to save the new form if the user presses 'Tab' or 'Return'
		self.dataHolderFields[12].dataHolder.bind('<Return>', lambda e: self.__saveRecord())
		self.dataHolderFields[12].dataHolder.bind('<Tab>', lambda e: self.__saveRecord())

		# Filling the first entry (folderID one) with the new available folder id
		lastFolderID = getLastFolderID(self.applicationSettings)
		self.dataHolderFields[0].dataHolder.insert(0, lastFolderID + 1)

		# Focus in the first entry (surname one)
		self.dataHolderFields[1].dataHolder.focus()

	def _createFooterFrame(self) -> None:
		""" Creates the Footer of the frame. The footer part contains two buttons. The one called 'Return' and the one called 'Save'. The 'Return' button
			allows the user to navigate back to the Main Menu Frame, while the 'Save' button allows them to save the data they entered in the form, inside
			the database. """

		self.footer = tk.Frame(self, bg=self.applicationSettings["theme-color"])
		self.footer.pack(pady=self.footer_options["buttons-frame-pady"])

		# Creating the 'Return' button
		self.return_image = resizeImage(self.return_logo_image, int(2 * self.footer_options["return-button-font"][1]))
		self.returnButton = tk.Button(
			self.footer,
			text=self.footer_options["return-button-text"],
			font=self.footer_options["return-button-font"],
			image=self.return_image,
			compound=tk.LEFT,
			padx=self.footer_options["return-button-padx-inner"],
			pady=self.footer_options["return-button-pady-inner"],
			command=self.__goToMainMenu
		)
		self.returnButton.grid(row=0, column=0, padx=self.footer_options["return-button-padx-outer"], pady=self.footer_options["return-button-pady-outer"])

		# Creating the 'Save' buttons
		self.save_image = resizeImage(self.save_logo_image, int(2 * self.footer_options["save-button-font"][1]))
		self.saveButton = tk.Button(
			self.footer,
			text=self.footer_options["save-button-text"],
			font=self.footer_options["save-button-font"],
			image=self.save_image,
			compound=tk.LEFT,
			padx=self.footer_options["save-button-padx-inner"],
			pady=self.footer_options["save-button-pady-inner"],
			command=self.__saveRecord
		)
		self.saveButton.grid(row=0, column=1, padx=self.footer_options["return-button-padx-outer"], pady=self.footer_options["return-button-pady-outer"])

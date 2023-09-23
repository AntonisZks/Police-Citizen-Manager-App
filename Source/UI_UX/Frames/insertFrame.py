"""
The 'insertFrame.py' file contains the InsertFrame class, which represents the insert frame of the application. Users can create a new form
and insert them to the database.

"""

from Source.UI_UX.Frames.frame import IFrame
from Source.Extras.support import *
from Source.UI_UX.RecordsStuff.record import Record


class InsertFrame(IFrame):
	def __init__(self, app_data: dict[str, any]) -> None:
		"""
		Constructor for the SearchFrame class.

		Args:
			app_data (dict): Data related to the application.
		"""
		# Initializing the basic frame
		super().__init__(app_data)

		self.record_area_scrollbar = None

	def _initializeImages(self) -> None:
		"""
		Initialize images used in the frame.
		"""
		self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
		self.return_logo_image = tk.PhotoImage(file=self.footer_options['return-button-image-path'])
		self.save_logo_image = tk.PhotoImage(file=self.footer_options['save-button-image-path'])

	def _setupStructureOptions(self, data: dict[str, any]) -> None:
		"""
		Set up options for the frame's structure.

		Args:
			data (dict): Data related to the application.
		"""
		# Setting up the Header Options
		self.header_options = {
			"title": "ΚΑΤΑΧΩΡΗΣΗ ΣΤΟΙΧΕΙΩΝ ΦΑΚΕΛΟΥ",
			"image-path": POLICE_LOGO_PNG_PATH,
			"font": ('Arial', round(0.022 * max(self.application_data['window-width'], self.application_data['window-height'])), 'bold')
		}

		# Setting up the Body Options
		self.body_options = {
			"empty-form-padx": round(0.04 * self.application_data['window-width']),
			"empty-form-pady": round(0.04 * self.application_data['window-height']),
			"title": "Σ Υ Μ Π Λ Η Ρ Ω Σ Η   Φ Ο Ρ Μ Α Σ",
			"title-font": ('Arial', round(0.022 * max(self.application_data['window-width'], self.application_data['window-height'])), 'bold', 'italic', 'underline'),
			"title-pady": round(0.02 * self.application_data['window-height'])
		}

		# Setting up the Footer Options
		self.footer_options = {
			"return-button-text": " ΕΠΙΣΤΡΟΦΗ ΣΤΟ ΜΕΝΟΥ ",
			"return-button-font": ('Arial', round(0.013 * max(self.application_data['window-width'], self.application_data['window-height']))),
			"return-button-image-path": RETURN_PNG_PATH,
			"return-button-padx-inner": round(0.01 * self.application_data['window-width']),
			"return-button-pady-inner": round(0.005 * self.application_data['window-height']),
			"return-button-padx-outer": round(0.01 * self.application_data['window-width']),
			"return-button-pady-outer": round(0.012 * self.application_data['window-height']),
			"save-button-text": " ΑΠΟΘΗΚΕΥΣΗ ΣΤΟΙΧΕΙΩΝ ",
			"save-button-font": ('Arial', round(0.012 * max(self.application_data['window-width'], self.application_data['window-height']))),
			"save-button-image-path": SAVE_PNG_PATH,
			"save-button-padx-inner": round(0.01 * self.application_data['window-width']),
			"save-button-pady-inner": round(0.005 * self.application_data['window-height']),
			"save-button-padx-outer": round(0.01 * self.application_data['window-width']),
			"save-button-pady-outer": round(0.013 * self.application_data['window-height']),

			"buttons-frame-pady": round(0.020 * self.application_data['window-height'])
		}

	def __goToMainMenu(self):
		"""
		Change the active frame to the Main Menu one.
		"""
		self.app.setActiveFrame(self.app.mainMenuFrame)

	def __saveRecord(self):
		# Getting the stored data in the database
		df = pd.read_excel(self.application_data['app-data']['active-database'])

		# Getting the new data
		new_data = []
		for entry in self.entries:
			value = entry.get() if isinstance(entry, tk.Entry) else entry.get("1.0", tk.END)
			value = value.replace("\n", "")
			new_data.append(value)

		# Adding the new data to the dataframe
		new_row = dict(zip(df.columns, new_data))
		df.loc[len(df)] = new_row

		# Storing the data of the dataframe into the database
		df.to_excel(self.application_data['app-data']['active-database'], index=False)

	def _buildStructure(self) -> None:
		"""
		Build the general structure of the search frame.
		"""
		self._createHeaderFrame()  # First create the header
		self._createBodyFrame()  # Then create the body
		self._createFooterFrame()  # Finally, create the footer

	def _createHeaderFrame(self) -> None:
		"""
		Create the Header Frame, which contains the main label and logo.
		"""
		self.header = tk.Frame(self, bg=self.application_data['theme-color'])  # Creating the header frame

		# Creating the Header Label
		self.header_image = resizeImage(self.police_logo_image, round(0.10 * self.application_data['window-width']))
		self.header_label = tk.Label(
			self.header,
			text=self.header_options['title'],
			font=self.header_options['font'],
			bg=self.application_data['theme-color'],
			fg=self.application_data['label-fg-color'],
			image=self.header_image, compound=tk.LEFT,
			padx=round(0.04 * self.application_data['window-width']),
			pady=round(0.04 * (self.application_data['window-height']))
		)

		# Packing the header and its widgets
		self.header_label.pack()
		self.header.pack()

	def _createBodyFrame(self) -> None:
		"""
		Create the Body Frame, which contains the search bars.
		"""
		self.body = tk.Frame(self, bg=self.application_data["theme-color-dark"])
		self.body.pack()

		# Creating a title
		self.titleLabel = tk.Label(
			self.body,
			text=self.body_options["title"],
			font=self.body_options["title-font"],
			bg=self.application_data["theme-color-dark"],
			fg=self.application_data['label-fg-color']
		)
		self.titleLabel.pack(pady=(self.body_options["title-pady"], 0))

		# Creating an empty form the user has to fill
		frame, self.entries = Record.createEmptyDataFrame(self.body, self.application_data)
		frame.pack(padx=self.body_options["empty-form-padx"], pady=(0, self.body_options["empty-form-pady"]))

		# Binding the entries in order to have access to each one using the keyboard 'Return' and 'Tab' buttons
		for entry in self.entries:
			entry.bind('<Return>', lambda e: onEntry(e, self.entries))
			entry.bind('<Tab>', lambda e: onEntry(e, self.entries))

		# Filling the first entry (folderID one) with the new available folder id
		lastFolderID = getLastFolderID(self.application_data)
		self.entries[0].insert(0, lastFolderID + 1)

		# Focus in the first entry (surname one)
		self.entries[1].focus()

	def _createFooterFrame(self) -> None:
		"""
		Create the Footer Frame which contains the 'Return' button
		"""
		self.footer = tk.Frame(self, bg=self.application_data["theme-color"])
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

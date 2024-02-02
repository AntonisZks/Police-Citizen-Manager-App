"""
The 'passwordWindow.py' file contains the PasswordWindow class, which represents a window that asks for the application password. It is mostly used for accessing the update frame of the app,
making sure that not everybody has access to that frame. The window pops up in front of the main window of the application and closes whether the user decides to close it or by typing the correct
password. If an incorrect password is being typed then the window closes again, but this time an error message box pops up too, notifying the user about the wrong password.

"""

import tkinter
from tkinter import messagebox
from Source.Extras.support import *
from Source.UI_UX.Other.passwordEntry import PasswordEntry
from UI_UX.changePasswordWindow import ChangePasswordWindow


class PasswordWindow(tk.Toplevel):
	def __init__(self, applicationSettings: dict[str, Any], widgetToOpen: tk.Widget | ChangePasswordWindow = None) -> None:
		""" The constructor of the Password window. The class inherits from the tkinter.Toplevel class to make sure that it is a tkinter window type.

		Args:
			applicationSettings: The settings of the application.
			widgetToOpen: The widget that is about to be accessed if the password is correct.

		"""
		super().__init__()  # Calling the constructor of the base class

		self.__setWindowGeometry()						    # Setting the geometry of the window
		self.title("Εισαγωγή Κωδικού Πρόσβασης")			# Setting the title of the window
		self.config(bg=applicationSettings['theme-color'])  # Setting the background color of the window

		# initializing the attributes of the class
		self.applicationSettings = applicationSettings
		self.widgetToOpen = widgetToOpen

		# Creating a main frame that will hold all the appropriate widgets
		self.frame = tk.Frame(self, bg=applicationSettings['theme-color'])
		self.frame.pack()

		self.__initializeImages()  # Initializing all the necessary images
		self.__buildStructure()    # Building the structure of the window

	def __initializeImages(self) -> None:
		""" Initializes all the images used in the window. """

		self.police_logo_image = tk.PhotoImage(file=POLICE_LOGO_PNG_PATH)

	def __setWindowGeometry(self) -> None:
		""" Sets the geometry of the window. """

		# Getting the screen width and height
		self.screen_width = self.winfo_screenwidth()
		self.screen_height = self.winfo_screenheight()

		# Calculating the width and height of the main window
		if self.screen_width > self.screen_height:
			self.window_height = round(0.4 * self.screen_height)
			self.window_width = round(1.8 * self.window_height)
		else:
			self.window_width = round(0.9 * self.screen_width)
			self.window_height = round(1.2 * self.window_width)

		# Calculating the x and y coordinates to spawn the window at the center of the screen
		spawn_x = (self.screen_width - self.window_width) // 2
		spawn_y = (self.screen_height - self.window_height) // 2 - 40

		self.geometry(f"{self.window_width}x{self.window_height}+{spawn_x}+{spawn_y}")

	def __buildStructure(self) -> None:
		""" Builds the main structure of the window (Header, Body, Footer). """

		self.__createHeaderFrame()  # Making the header frame
		self.__createBodyFrame()    # Making the body frame
		self.__createFooterFrame()  # Making the footer frame

	def __createHeaderFrame(self) -> None:
		""" Creates the header of the window. """

		self.header = tk.Frame(self.frame, bg=self.applicationSettings['theme-color'])  # Creating the header main frame
		self.header.pack()																# Packing the main frame

		# Creating the Header Label
		self.header_image = resizeImage(self.police_logo_image, round(0.10 * self.applicationSettings['window-width']))
		self.header_label = tk.Label(
			self.header,
			text="ΕΙΣΑΓΕΤΕ ΤΟΝ ΚΩΔΙΚΟ ΠΡΟΣΒΑΣΗΣ:", font=('Arial', round(0.03*self.applicationSettings['window-width']), 'bold'),
			bg=self.applicationSettings['theme-color'], fg=self.applicationSettings['label-fg-color'],
			image=self.header_image, compound=tk.LEFT,
			padx=round(0.04 * self.applicationSettings['window-width']), pady=round(0.04 * (self.applicationSettings['window-height']))
		)
		self.header_label.pack()  # Packing the label

	def __createBodyFrame(self) -> None:
		""" Creates the body of the window. """

		self.body = tk.Frame(self.frame, bg=self.applicationSettings['theme-color'])  # Creating the body main frame
		self.body.pack()															  # Packing the main frame

		# Creating a password entry object
		self.passwordEntry = PasswordEntry(self.body, self.applicationSettings, round(0.02 * self.applicationSettings['window-width']), round(0.01 * self.applicationSettings['window-width']), ('Arial', round(0.03 * self.applicationSettings['window-width'])), self.check)
		self.passwordEntry.build()  # Building the password entry object
		self.passwordEntry.focus()  # Focus in the password entry

	def __createFooterFrame(self) -> None:
		""" Creates the footer of the window. """

		self.footer = tk.Frame(self.frame, bg=self.applicationSettings['theme-color'])  # Creating the footer main frame
		self.footer.pack()																# Packing the main frame

		self.submitButton = tk.Button(self.footer, text="ΕΠΙΒΕΒΑΙΩΣΗ", font=('Arial', round(0.03 * self.applicationSettings['window-width'])), command=self.check)  # Creating the submit button
		self.submitButton.pack(pady=round(0.06 * self.applicationSettings['window-height']))																		# Packing the submit button

	def check(self) -> None:
		""" Checks whether the entered password is correct or not. """

		inputPassword = self.passwordEntry.getItem()					  # Getting the entered password
		savedPassword = self.applicationSettings['app-data']['password']  # Getting the stored password

		# Checking if the entered password is correct
		if inputPassword == savedPassword:
			self.destroy()  # Destroying the password window

			# Check whether the widget to open is either a frame or a change password window
			if isinstance(self.widgetToOpen, tkinter.Frame):
				self.applicationSettings['object'].setActiveFrame(self.widgetToOpen)  # Setting the active frame to be the given widget
			else:
				self.widgetToOpen.deiconify()				# Make the window visible
				self.widgetToOpen.newPasswordEntry.focus()  # Focus on the window first entry

		else:
			messagebox.showerror("Λάθος Κωδικός Πρόσβασης", "Ο κωδικός πρόσβασης που δώσατε είναι λανθασμένος.")  # Pop up a message box saying that the password is incorrect
			self.destroy()																						  # Destroying the password window

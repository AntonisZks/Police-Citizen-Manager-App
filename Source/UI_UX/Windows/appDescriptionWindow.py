from Extras.support import *


class AppDescriptionWindow(tk.Toplevel):
	def __init__(self, applicationSettings: dict[str, Any]) -> None:
		super().__init__()

		self.__setWindowGeometry()
		self.title("Περιγραφή Εφαρμογής")
		self.config(bg=applicationSettings['theme-color'])

		self.applicationSettings = applicationSettings

		self.frame = tk.Frame(self, bg=applicationSettings['theme-color'])
		self.frame.pack()

		self.__initializeImages()
		self.__buildStructure()

	def __setWindowGeometry(self) -> None:
		""" Sets the geometry of the window. """

		# Getting the screen width and height
		self.screen_width = self.winfo_screenwidth()
		self.screen_height = self.winfo_screenheight()

		# Calculating the width and height of the main window
		if self.screen_width > self.screen_height:
			self.window_height = round(0.8 * self.screen_height)
			self.window_width = round(0.8 * self.window_height)
		else:
			self.window_width = round(0.9 * self.screen_width)
			self.window_height = round(1.2 * self.window_width)

		# Calculating the x and y coordinates to spawn the window at the center of the screen
		spawn_x = (self.screen_width - self.window_width) // 2
		spawn_y = (self.screen_height - self.window_height) // 2 - 40

		self.geometry(f"{self.window_width}x{self.window_height}+{spawn_x}+{spawn_y}")

	def __initializeImages(self) -> None:
		self.police_logo_image = tk.PhotoImage(file=POLICE_LOGO_PNG_PATH)

	def __buildStructure(self) -> None:
		self.__createHeaderFrame()  # Making the header frame
		self.__createBodyFrame()  # Making the body frame

	def __createHeaderFrame(self):
		self.header = tk.Frame(self.frame, bg=self.applicationSettings['theme-color'])
		self.header.pack()

		self.header_image = resizeImage(self.police_logo_image, round(0.10 * self.applicationSettings['window-width']))
		self.header_label = tk.Label(
			self.header,
			text="ΣΧΕΤΙΚΑ ΜΕ ΤΗΝ ΕΦΑΡΜΟΓΗ", font=('Arial', round(0.03 * self.applicationSettings['window-width']), 'bold'),
			bg=self.applicationSettings['theme-color'], fg=self.applicationSettings['label-fg-color'],
			image=self.header_image, compound=tk.LEFT,
			padx=round(0.04 * self.applicationSettings['window-width']), pady=round(0.04 * (self.applicationSettings['window-height']))
		)
		self.header_label.pack()

	def __createBodyFrame(self):
		self.body = tk.Frame(self.frame, bg=self.applicationSettings['theme-color'])
		self.body.pack()

		self.description_area = tk.Text(
			self.body,
			wrap="word", font=('Arial', round(0.015 * self.applicationSettings['window-width'])),
			padx=round(0.04 * self.applicationSettings['window-width']), pady=round(0.04 * (self.applicationSettings['window-height'])),
			fg="white", bg=self.applicationSettings['theme-color-dark'], borderwidth=0
		)

		with open(APPLICATION_DESCRIPTION_INFO_PATH_, "r", encoding='utf-8') as file:
			app_description = file.read()

		self.description_area.insert('1.0', app_description)
		self.description_area.pack(padx=round(0.04 * self.applicationSettings['window-width']), pady=round(0.04 * (self.applicationSettings['window-height'])))

		self.description_area.config(state=tk.DISABLED)

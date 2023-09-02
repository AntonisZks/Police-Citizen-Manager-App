import tkinter as tk
import json
from support import *
from WindowFrames.databasePickerFrame import DatabasePickerFrame

# The class App stands for the main application
class App:
    def __init__(self):
        self.window = tk.Tk() # Initialize the main window

        # Setting the options of the main window
        self.setWindowIcon() # Window Icon
        self.setWindowGeometry() # Window Geometry
        self.window.state("zoomed") # Window State
        self.window.config(bg=BACKGROUND_COLOR_1) # Background Color
        self.window.title("Ελληνική Αστυνομία, Ατομικοί Φάκελοι") # Window Title

        # Getting the App Data
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            self.app_data = json.load(json_file)

        # Creating some useful options about the Application
        self.createOptions()

        # Creating the frames used by the main window
        self.createFrames() # Create the frames

    def createFrames(self):
        self.databasePickerFrame = DatabasePickerFrame(self.options)
    
    def createOptions(self):
        self.options = {
            "app-data": self.app_data,
            "window": self.window,
            "window-width": self.window_width,
            "window-height": self.window_height,
            "theme-color": BACKGROUND_COLOR_1,
            "theme-color-dark": BACKGROUND_COLOR_2,
            "theme-color-very-dark": BACKGROUND_COLOR_3,
            "label-fg-color": "white"
        }

    def setWindowIcon(self):
        self.window_icon = tk.PhotoImage(file=POLICE_LOGO_PNG_PATH)
        self.window.iconphoto(True, self.window_icon)

    def setWindowGeometry(self):
        # Getting the screen width and height
        screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        
        # Calculating the width and height of the main window
        if screen_width > screen_height:
            self.window_height = round(0.9*screen_height)
            self.window_width = round(0.8*self.window_height)
        else:
            self.window_width = round(0.9*screen_width)
            self.window_height = round(1.2*self.window_width)

        # Calculating the x and y coordinates so as to spawn the window at the center of the screen
        spawn_x = (screen_width - self.window_width) // 2
        spawn_y = (screen_height - self.window_height) // 2 - 40

        self.window.geometry(f"{self.window_width}x{self.window_height}+{spawn_x}+{spawn_y}")

    def run(self):
        self.window.mainloop()

"""
The main.py file contains the basic class that corresponds to the Application with its methods. It also contain the main code
the program starts from. In order to start the application we create an App object and then we run it calling the run() method.

"""

import tkinter as tk
import json
from support import *
from WindowFrames.databasePickerFrame import DatabasePickerFrame
from WindowFrames.mainMenuFrame import MainMenuFrame

# The class App stands for the main application
class App:
    """
    The App class represents the main application, where it has a main window and some usefull options.

    Attributes:
        window (Tk): The main window of the application
        window_icon (PhotImage): The icon of the main window
        window_width (int): The width of the main window
        window_height (int): The height of the main window
        app_data (dict): The data of the application
        options (dict): Some usefull options of the application
        databasePickerFrame (DatabasePickerFrame): the frame where the user selects the excel file

    Methods:
        __createFrames(): Creates the frames of the application
        __createOptions(): Creates the options of the application
        __setWindowGeometry(): Sets the window geometry of the application main window
        __setWindowIcon(): Sets the icon of the application main window
        run(): Runs the application

    """
    def __init__(self) -> None:
        """
        The constructor of the application. Here all the basic stuff of the application are being initialized,
        such as the main window, the icon of the window, the geometry of the window, the title etc.
        It also gain the application data stored in a .json file called appData.json

        """
        self.window = tk.Tk() # Initialize the main window

        # Setting the options of the main window
        self.__setWindowIcon() # Window Icon
        self.__setWindowGeometry() # Window Geometry
        self.window.state("zoomed") # Window State
        self.window.config(bg=BACKGROUND_COLOR_1) # Background Color
        self.window.title("Ελληνική Αστυνομία, Ατομικοί Φάκελοι") # Window Title

        # Getting the App Data
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            self.app_data = json.load(json_file)

        # Creating some useful options about the Application
        self.__createOptions()

        # Creating the frames used by the main window
        self.createFrames() # Create the frames

        # Set the active frame
        self.active_frame = None
        self.setActiveFrame(self.databasePickerFrame)

    def createFrames(self) -> None:
        """
        The __createFrames() method creates all the frames used by the application.
        By default the first frame ever used is the DatabasePickerFrame which gives the user
        the ability to choose which database he/she wants to administrate.

        """
        self.databasePickerFrame = DatabasePickerFrame(self.options)
        self.mainMenuFrame = MainMenuFrame(self.options)

    def setActiveFrame(self, frame: tk.Frame) -> None:
        """
        The setActiveFrame() method sets the given frame as an active one to the application.

        Args:
            frame (Frame): The frame passed in order to be set as active
        
        """
        if self.active_frame is not None:
            self.active_frame.destroy()
        
        self.active_frame = frame
        self.active_frame.build()
    
    def __createOptions(self) -> None:
        """
        The __createOptions() method creates all the usefull options for the application.
        Some of them are the app_data, the main window, the window width and height, the theme colors etc.

        """
        self.options = {
            "app-data": self.app_data,
            "object": self,
            "window": self.window,
            "window-width": self.window_width,
            "window-height": self.window_height,
            "theme-color": BACKGROUND_COLOR_1,
            "theme-color-dark": BACKGROUND_COLOR_2,
            "theme-color-very-dark": BACKGROUND_COLOR_3,
            "label-fg-color": "white"
        }

    def __setWindowIcon(self) -> None:
        """
        The __setWindowIcon() method sets the icon of the window. It obtains the image by the file support.py

        """
        self.window_icon = tk.PhotoImage(file=POLICE_LOGO_PNG_PATH)
        self.window.iconphoto(True, self.window_icon)

    def __setWindowGeometry(self) -> None:
        """
        The __setWindowGeometry() method sets the geometry of the window. It obtains the current screen dimensions
        and then it calculates the width and the height of the window. It also calculates the spawn position of the window
        which by default is the center of the screen. Finally it sets all the above to the main window.
        
        """
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

    def run(self) -> None:
        """
        The run() method is called when the application needs to run. It calls the mainloop() method
        of the window object.

        """
        self.window.mainloop()


if __name__ == '__main__':
    myApp = App()
    myApp.run()
    
    # attributes = vars(myApp.databasePickerFrame)
    # attribute_types = {attr: type(value).__name__ for attr, value in attributes.items()}
    # for attr, attr_type in attribute_types.items():
    #     print(f"Attribute: {attr}, type: {attr_type}")

    # methods = [method for method in dir(myApp.databasePickerFrame) if callable(getattr(myApp.databasePickerFrame, method))]
    # for method in methods:
    #     print("Method:", method)
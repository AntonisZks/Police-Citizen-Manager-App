"""
The 'app.py' file contains the basic class that corresponds to the Application with its methods. It also contains the main code
the program starts from. In order to start the application we create an App object, and then we run it calling the run() method.

"""

import json
from Source.Extras.support import *
from Source.UI_UX.Frames.frame import IFrame
from Source.UI_UX.Frames.databasePickerFrame import DatabasePickerFrame
from Source.UI_UX.Frames.mainMenuFrame import MainMenuFrame
from Source.UI_UX.Frames.searchFrame import SearchFrame
from Source.UI_UX.Frames.insertFrame import InsertFrame
from Source.UI_UX.Frames.updateFrame import UpdateFrame


# The class App stands for the main application
class App(tk.Tk):
    """ The App class represents the main application, where it has a main window and some useful options.

    Attributes:
        window_icon (PhotImage): The icon of the main window
        window_width (int): The width of the main window
        window_height (int): The height of the main window
        app_data (dict): The data of the application
        options (dict): Some useful options of the application
        databasePickerFrame (DatabasePickerFrame): the frame where the user selects the Excel file

    Methods:
        __createFrames(): Creates the frames of the application
        __createOptions(): Creates the options of the application
        __setWindowGeometry(): Sets the window geometry of the application main window
        __setWindowIcon(): Sets the icon of the application main window
        run(): Runs the application

    """

    def __init__(self) -> None:
        """ The constructor of the application. Here all the basic stuff of the application are being initialized,
            such as the main window, the icon of the window, the geometry of the window, the title etc.
            It also gains the application data stored in a .json file called appData.json. """

        super().__init__()
        self.insertFrame = None
        self.searchFrame = None
        self.updateFrame = None
        self.mainMenuFrame = None
        self.databasePickerFrame = None

        self.protocol("WM_DELETE_WINDOW", self.__onClosing)

        # Setting the options of the main window
        self.__setWindowIcon()  # Window Icon
        self.__setWindowGeometry()  # Window Geometry
        self.state("zoomed")  # Window State
        self.config(bg=BACKGROUND_COLOR_1)  # Background Color
        self.title("Ελληνική Αστυνομία, Ατομικοί Φάκελοι")  # Window Title

        # Getting the App Data
        with open(APP_DATA_PATH, 'r', encoding='utf-8') as json_file:
            self.app_data = json.load(json_file)

        # Creating some useful options about the Application
        self.__createOptions()

        # Creating the frames used by the main window
        self.createFrames()  # Create the frames

        # Set the active frame
        self.active_frame = None
        self.setActiveFrame(self.databasePickerFrame)

    def __onClosing(self) -> None:
        """ The __onClosing() method is called when the user decides to close the application. When this happens the program is making
            sure that the active database of the application is being removed, to not leaving useless data behind. This function
            is responsible for this work. """

        self.app_data['active-database'] = ""  # Modify the active database and make it empty

        # Add the modified application data in the json file
        with open(APP_DATA_PATH, 'w', encoding='utf-8') as json_file:
            json.dump(self.app_data, json_file)

        self.destroy()  # And of course destroy the main window and terminate the application

    def createFrames(self) -> None:
        """ The __createFrames() method creates all the frames used by the application.
            By default, the first frame ever used is the DatabasePickerFrame which gives the user
            the ability to choose which database he/she wants to administrate. """

        self.databasePickerFrame = DatabasePickerFrame(self.options)
        self.mainMenuFrame = MainMenuFrame(self.options)
        self.searchFrame = SearchFrame(self.options)
        self.insertFrame = InsertFrame(self.options)
        self.updateFrame = UpdateFrame(self.options)

    def setActiveFrame(self, frame: IFrame | None) -> None:
        """ The setActiveFrame() method sets the given frame as an active one to the application.

        Args:
            frame (Frame): The frame passed in order to be set as active
        
        """
        if self.active_frame is not None:
            self.active_frame.destroy()

        self.active_frame = frame
        self.active_frame.build()
        self.active_frame.pack()

    def __createOptions(self) -> None:
        """ The __createOptions() method creates all the useful options for the application.
            Some of them are the app_data, the main window, the window width and height, the theme colors etc. """

        self.options = {
            "app-data": self.app_data,
            "object": self,
            "window": self,
            "window-width": self.window_width,
            "window-height": self.window_height,
            "theme-color": BACKGROUND_COLOR_1,
            "theme-color-dark": BACKGROUND_COLOR_2,
            "theme-color-very-dark": BACKGROUND_COLOR_3,
            "theme-color-light": BACKGROUND_COLOR_4,
            "label-fg-color": "white",
            "screen-width": self.screen_width,
            "screen-height": self.screen_height
        }

    def __setWindowIcon(self) -> None:
        """ The __setWindowIcon() method sets the icon of the window. It obtains the image by the file support.py """

        self.window_icon = tk.PhotoImage(file=POLICE_LOGO_PNG_PATH)
        self.iconphoto(True, self.window_icon)

    def __setWindowGeometry(self) -> None:
        """ The __setWindowGeometry() method sets the geometry of the window. It obtains the current screen dimensions,
            and then it calculates the width and the height of the window. It also calculates the spawn position of the window
            which by default is the center of the screen. Finally, it sets all the above to the main window. """

        # Getting the screen width and height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Calculating the width and height of the main window
        if self.screen_width > self.screen_height:
            self.window_height = round(0.9 * self.screen_height)
            self.window_width = round(0.8 * self.window_height)
        else:
            self.window_width = round(0.9 * self.screen_width)
            self.window_height = round(1.2 * self.window_width)

        # Calculating the x and y coordinates to spawn the window at the center of the screen
        spawn_x = (self.screen_width - self.window_width) // 2
        spawn_y = (self.screen_height - self.window_height) // 2 - 40

        self.geometry(f"{self.window_width}x{self.window_height}+{spawn_x}+{spawn_y}")

    def run(self) -> None:
        """ The run() method is called when the application needs to run. It calls the mainloop() method
            of the window object. """

        self.mainloop()


if __name__ == '__main__':
    myApp = App()  # Create an App object
    myApp.run()    # Call the run() method of the App object to start the application

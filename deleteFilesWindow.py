import tkinter as tk
from initialization import *

class DeleteFilesWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Toplevel()
        
        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = self.geometry_data['width']//2
        self.height = self.geometry_data['height']//2
        self.spawn_x = self.geometry_data['spawn_x'] + (self.geometry_data['width'] - self.width)//2
        self.spawn_y = self.geometry_data['spawn_y'] + (self.geometry_data['height'] - self.height)//2
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Ιnitialize all the font options
        self.font_size = self.geometry_data['font_size']//2

        # Initialize the title, the icon, and the background color of the window
        self.window.title("Διαγραφή Προεπιλεγμένων Αρχείων")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

    def create_main_label(self):
        self.main_label = tk.Label(self.window, text="ΕΠΙΛΕΞΤΕ ΑΡΧΕΙΑ ΓΙΑ ΔΙΑΓΡΑΦΗ:", font=('Arial', int((15/10)*self.font_size), 'bold'), 
                                   fg="white", bg="#2A508C", pady=int((1/20)*self.height))
        self.main_label.pack()

    def run(self):
        self.initialize_window()
        self.create_main_label()
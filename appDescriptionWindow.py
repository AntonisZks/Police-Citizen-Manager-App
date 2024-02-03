import tkinter as tk
from initialization import *

class AppDescriptionWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Toplevel()
        
        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = int((8/10)*self.geometry_data['width'])
        self.height = int((8/10)*self.geometry_data['height'])
        self.spawn_x = self.geometry_data['spawn_x'] + (self.geometry_data['width'] - self.width)//2
        self.spawn_y = self.geometry_data['spawn_y'] + (self.geometry_data['height'] - self.height)//2
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Ιnitialize all the font options
        self.font_size = self.geometry_data['font_size']

        # Initialize the title, the icon, and the background color of the window
        self.window.title("Σχετικά με το Police Citizen Manager")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

    def create_main_label(self):
        self.main_label_image = resizeImage(self.police_icon_image, int((2/20)*self.height))
        self.main_label = tk.Label(self.window, text="ΣΧΕΤΙΚΑ ΜΕ ΤΗΝ ΕΦΑΡΜΟΓΗ", font=('Arial', int(self.font_size*(1.1)), 'bold'), fg="white", bg="#2A508C", 
                                   image=self.main_label_image, compound="left", padx=int((1/50)*self.width))
        self.main_label.pack(pady=(1/30)*self.height)

    def create_text_area(self):
        self.text_area = tk.Text(self.window, wrap="word", font=('Arial', int((5/10)*self.font_size)), 
                                 padx=int((1/30)*self.width), pady=int((1/30)*self.height), height=int((6/10)*self.height),
                                 fg="white", bg="#2A508C", borderwidth=0)
        with open(APPLICATION_DESCRIPTION_INFO_PATH_, "r", encoding="utf-8") as file:
            app_information_text = file.read()

        self.text_area.insert('1.0', app_information_text)
        self.text_area.pack(padx=int((1/20)*self.width), pady=int((1/30)*self.height))

    def run(self):
        self.initialize_window()
        self.create_main_label()
        self.create_text_area()

        self.window.mainloop()
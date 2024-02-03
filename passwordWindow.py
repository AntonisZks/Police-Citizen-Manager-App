import tkinter as tk
from initialization import *
from update import UpdateWindow
from tkinter import messagebox

class PasswordWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_
    HIDE_PASSWORD_IMAGE_PATH = HIDE_LOGO_IMAGE_PATH_
    VIEW_PASSWORD_IMAGE_PATH = VIEW_LOGO_IMAGE_PATH_

    def __init__(self, window_to_open):
        self.window_to_open = window_to_open

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Toplevel()

        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)
        self.hide_password_icon_image = tk.PhotoImage(file=self.HIDE_PASSWORD_IMAGE_PATH)
        self.view_password_icon_image = tk.PhotoImage(file=self.VIEW_PASSWORD_IMAGE_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = int((8/10)*self.geometry_data['width'])
        self.height = int((4/10)*self.geometry_data['height'])
        self.spawn_x = self.geometry_data['spawn_x'] + (self.geometry_data['width'] - self.width)//2
        self.spawn_y = self.geometry_data['spawn_y'] + (self.geometry_data['height'] - self.height)//2
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Initialize all the font options
        self.font_size = self.geometry_data['font_size']
        self.label_font = ('Arial', int(self.font_size*(0.9)), 'bold')
        self.password_font = ('Arial', int(self.font_size*(1)))
        self.button_font = ('Arial', int(self.font_size*(0.9)))
        
        # Initialize the title, the icon, and the background color of the window
        self.window.title("Εισαγωγή Κωδικού Πρόσβασης")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

    def create_main_label(self):
        self.main_label_image = resizeImage(self.police_icon_image, int((2/15)*self.height))
        self.main_label = tk.Label(self.window, text="ΕΙΣΑΓΕΤΕ ΤΟΝ ΚΩΔΙΚΟ ΠΡΟΣΒΑΣΗΣ:", font=self.label_font, fg="white", bg="#2A508C",
                                   image=self.main_label_image, compound="left", padx=int((1/50)*self.width))
        self.main_label.pack(pady=(1/20)*self.width)

    def create_password_entry(self):
        self.password_entry_frame = tk.Frame(self.window, bg="#2A508C")
        self.password_entry_frame.pack()
        self.password_entry = tk.Entry(self.password_entry_frame, font=self.password_font, borderwidth=int((1/100)*self.width), show="*")
        self.password_entry.pack(side="left")
        self.password_entry.bind('<Return>', self.check)

        self.view = False
        desired_size = int((3/48)*self.width)
        self.hide_icon = resizeImage(self.hide_password_icon_image, desired_size)
        self.view_icon = resizeImage(self.view_password_icon_image, desired_size)
        self.hide_unhide_button = tk.Button(self.password_entry_frame, image=self.hide_icon, command=self.change_state)
        self.hide_unhide_button.pack(side="left")
        self.password_entry.focus()

    def change_state(self):
        if self.view:
            self.password_entry['show'] = '*'
            self.hide_unhide_button['image'] = self.hide_icon
            self.view = False
        else:
            self.password_entry['show'] = ''
            self.hide_unhide_button['image'] = self.view_icon
            self.view = True

    def create_submit_button(self):
        self.submit_button = tk.Button(self.window, text="ΕΠΙΒΕΒΑΙΩΣΗ", font=self.button_font, command=self.check)
        self.submit_button.pack(pady=(1/20)*self.width)

    def check(self, temp=None):
        self.valid_password = False
        with open(PASSWORD_PATH_, "r") as file:
            password = file.readline()
            if self.password_entry.get() == password:
                self.valid_password = True
        if self.valid_password:
            self.window.destroy()
            self.window_to_open.run()
        else:
            self.window.attributes('-topmost', False)
            messagebox.showwarning("Λάθος Κωδικός Πρόσβασης", "Ο κωδικός πρόσβασης που καταχωρήσατε δεν είναι σωστός.")
            self.window.attributes('-topmost', True)
            self.password_entry.focus()

    def run(self):
        self.initialize_window()
        self.create_main_label()
        self.create_password_entry()
        self.create_submit_button()

        self.window.mainloop()
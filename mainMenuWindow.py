import tkinter as tk
from initialization import *
from search import SearchWindow
from insert import InsertWindow
from update import UpdateWindow
from passwordWindow import PasswordWindow
from changePasswordWindow import ChangePasswordWindow
from appDescriptionWindow import AppDescriptionWindow
from appLicenceInfoWindow import AppLicenceInfoWindow

class MainMenuWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_
    SEARCH_ICON_PATH = SEARCH_LOGO_IMAGE_PATH_
    INSERT_ICON_PATH = INSERT_LOGO_IMAGE_PATH_
    UPDATE_ICON_PATH = UPDATED_LOGO_IMAGE_PATH_
    CHANGE_ICON_PATH = CHANGE_LOGO_IMAGE_PATH_

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Tk()
        
        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)
        self.search_icon_image = tk.PhotoImage(file=self.SEARCH_ICON_PATH)
        self.insert_icon_image = tk.PhotoImage(file=self.INSERT_ICON_PATH)
        self.update_icon_image = tk.PhotoImage(file=self.UPDATE_ICON_PATH)
        self.change_icon_image = tk.PhotoImage(file=self.CHANGE_ICON_PATH)

        # Initialize the geometry of the window
        self.geometry_data = getWindowGeometryData(self.window)
        self.width = self.geometry_data['width']
        self.height = self.geometry_data['height']
        self.spawn_x = self.geometry_data['spawn_x']
        self.spawn_y = self.geometry_data['spawn_y']
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Ιnitialize all the font options
        self.font_size = self.geometry_data['font_size']
        self.button_font = ('Arial', int(self.font_size*1.2))

        # Initialize the title, the icon, and the background color of the window
        self.window.title("Ελληνική Αστυνομία, Ατομικοί Φάκελοι")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

        # Create the search, insert and update windows
        self.search_window = SearchWindow()
        self.insert_window = InsertWindow()
        self.update_window = UpdateWindow()
        self.change_password_window = ChangePasswordWindow()
        self.password_for_update_window = PasswordWindow(self.update_window)
        self.password_for_change_password_window = PasswordWindow(self.change_password_window)
        self.app_description_info_window = AppDescriptionWindow()
        self.app_licence_info_window = AppLicenceInfoWindow()


    def create_main_label(self):
        self.main_label_image = resizeImage(self.police_icon_image, int((2/15)*self.width))
        self.main_label = tk.Label(
            self.window,
            text="ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΑΤΟΜΙΚΩΝ ΦΑΚΕΛΩΝ ΠΟΛΙΤΩΝ",
            font=("Arial", self.font_size, 'bold'),
            bg="#2A508C",
            fg="white",
            image=self.main_label_image,  # Use the stored reference to the image
            compound="left",
            padx=int((1/25)*self.width),
            pady=int((1/40)*self.width)
        )
        self.main_label.pack(pady=int((1/40)*self.height))

    def create_buttons(self):
        # Create the images we need
        self.search_icon = resizeImage(self.search_icon_image, int((2/40)*self.width))
        self.insert_icon = resizeImage(self.insert_icon_image, int((2/40)*self.width))
        self.update_icon = resizeImage(self.update_icon_image, int((2/40)*self.width))

        # Create a frame for all the buttons
        self.buttons_frame = tk.Frame(self.window, bg="#2A508C"); self.buttons_frame.pack(pady=int((1/50)*self.height))

        # create the buttons
        search_button = tk.Button(self.window, text="ΑΝΑΖΗΤΗΣΗ", font=self.button_font, image=self.search_icon, compound="left", 
                                  padx=self.font_size, pady=int((2/3)*self.font_size), width=int((4/10)*self.width), command=self.search_window.run)
        insert_button = tk.Button(self.window, text="ΚΑΤΑΧΩΡΗΣΗ", font=self.button_font, image=self.insert_icon, compound="left", 
                                  padx=self.font_size, pady=int((2/3)*self.font_size), width=int((4/10)*self.width), command=self.insert_window.run)
        update_button = tk.Button(self.window, text="  ΔΙΟΡΘΩΣΗ  ", font=self.button_font, image=self.update_icon, compound="left", 
                                  padx=self.font_size, pady=int((2/3)*self.font_size), width=int((4/10)*self.width), command=self.password_for_update_window.run)
        
        search_button.pack(pady=int((1/20)*self.height)); insert_button.pack(pady=int((1/20)*self.height)); update_button.pack(pady=int((1/20)*self.height))

    def create_current_file_label(self):
        self.change_file_frame = tk.Frame(self.window, bg="#2A508C"); self.change_file_frame.pack()

        self.current_file_label = tk.Label(self.change_file_frame, text=f"ΕΝΕΡΓΟ ΑΡΧΕΙΟ:      {get_file_name(get_active_database())}", font=('Arial', int((9/10)*self.font_size), 'bold'), fg="white", bg="#2A508C")
        self.current_file_label.pack(side="left")

        self.change_icon = resizeImage(self.change_icon_image, int((9/10)*self.font_size))
        self.change_file_button = tk.Button(self.change_file_frame, text="ΑΛΛΑΓΗ", font=('Arial', int((5/10)*self.font_size)), 
                                            image=self.change_icon, compound="left", padx=int((5/10)*self.font_size), pady=int((2/10)*self.font_size),
                                            command=self.change_file)
        self.change_file_button.pack(side="left", padx=int((1/50)*self.width))

    def change_file(self):
        with open(ACTIVE_FILE_PATH_, "w", encoding="utf-8") as file:
            file.write('')
        self.window.destroy()
        self.choose_database_window.run()

    def quit_app(self):
        with open(ACTIVE_FILE_PATH_, "w", encoding="utf-8") as file:
            file.write('')
        self.window.destroy()

    def change_password(self):
        self.password_for_change_password_window.run()

    def app_description_info(self):
        self.app_description_info_window.run()

    def app_licence_info(self):
        self.app_licence_info_window.run()

    def create_menu_bar(self):
        # Creating the menu bar of the window
        self.menu_bar = tk.Menu(self.window)

        # Creating a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_cascade(label="Exit", command=self.quit_app)

        # Creating an Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_cascade(label="Αλλαγή Κωδικού", command=self.change_password)

        # Creating a Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_cascade(label="Σχετικά με την εφαρμογή", command=self.app_description_info)
        self.help_menu.add_cascade(label="Άδεια Χρήσης", command=self.app_licence_info)

        # Adding the menus to the window
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.window.config(menu=self.menu_bar)

    def run(self, choose_database_window):
        self.choose_database_window = choose_database_window
        self.initialize_window()
        self.create_main_label()
        self.create_current_file_label()
        self.create_buttons()
        self.create_menu_bar()

        self.window.mainloop()
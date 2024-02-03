import tkinter as tk
from mainMenuWindow import MainMenuWindow
from initialization import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from deleteFilesWindow import DeleteFilesWindow
from initialization import *
from appDescriptionWindow import AppDescriptionWindow
from appLicenceInfoWindow import AppLicenceInfoWindow
from passwordWindow import PasswordWindow
from changePasswordWindow import ChangePasswordWindow

class ChooseDatebaseWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_
    ADD_LOGO_IMAGE_PATH = ADD_LOGO_IMAGE_PATH_
    DELETE_LOGO_IMAGE_PATH = DELETE_LOGO_IMAGE_PATH_

    def initialize_window(self):
        # Initialize the window
        self.window = tk.Tk()
        
        # Initialize the images
        self.police_icon_image = tk.PhotoImage(file=self.POLICE_LOGO_IMAGE_PATH)
        self.add_icon_image = tk.PhotoImage(file=self.ADD_LOGO_IMAGE_PATH)
        self.delete_icon_image = tk.PhotoImage(file=self.DELETE_LOGO_IMAGE_PATH)

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

        # Initialize the windows
        self.change_password_window = ChangePasswordWindow()
        self.password_for_change_password_window = PasswordWindow(self.change_password_window)
        self.app_description_info_window = AppDescriptionWindow()
        self.app_licence_info_window = AppLicenceInfoWindow()

    def on_mousewheel(self, event):
        self.file_picker_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_main_label(self):
        self.main_label_frame = tk.Frame(self.window, bg="#2A508C"); self.main_label_frame.pack()
        
        self.main_label_image = resizeImage(self.police_icon_image, int((2/15)*self.width))
        self.main_label = tk.Label(
            self.main_label_frame,
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

        self.main_label_message = tk.Label(self.main_label_frame, 
                                           text="Γ Ι Α    Σ Υ Ν Ε Χ Ε Ι Α    Ε Π Ι Λ Ε Ξ Τ Ε    Α Ρ Χ Ε Ι Ο :", font=('Arial', int((8/10)*self.font_size), 'bold'), fg="white", bg="#2A508C")
        self.main_label_message.pack()

    def create_file_button(self, frame, index, path, row, column):
        self.button_gap = int((1/63)*self.width)
        self.button_width = (self.file_picker_canvas.winfo_width()-4*self.button_gap)//3
        button = tk.Button(frame, text=get_file_name(path)[:-1], font=('Arial', int((17/30)*self.font_size)), width=self.button_width, command=lambda: self.select_file(path))
        button.grid(row=row, column=column, padx=self.button_gap, pady=self.button_gap)

        return button
    
    def select_file(self, text):
        with open(ACTIVE_FILE_PATH_, "w", encoding="utf-8") as file:
            file.write(text)

        self.window.destroy()
        self.main_menu_window = MainMenuWindow()
        self.main_menu_window.run(self)

    def create_file_picker(self):
        def show_context_menu(event, button, index):
            def delete_button(button, index):
                if messagebox.askyesno("Διαγραφή Προεπιλεγμένου Αρχείου", "Θέλετε σίγουρα να διαγράψετε το αρχείο;"):
                    button.destroy()
                    self.files.pop(index)
                    with open(FILES_PATH_, "w", encoding="utf-8") as f:
                        for file in self.files:
                            f.write(file)
                    self.buttons_frame.destroy()
                    self.file_picker_canvas.destroy(); self.main_label_frame.destroy()
                    self.create_main_label()
                    self.create_file_picker()
                    self.create_buttons()

            self.context_menu.post(event.x_root, event.y_root)
            self.context_menu.entryconfigure(0, command=lambda: delete_button(button, index))

        with open(FILES_PATH_, "r", encoding="utf-8") as file:
            self.files = file.readlines()

        self.file_picker_canvas = tk.Canvas(self.window, background="#2A508C", highlightbackground="#2A508C", width=int((9/10)*self.width), height=int((5/10)*self.height))
        self.file_picker_canvas.pack(padx=int((1/20)*self.width), pady=int((1/25)*self.height))
        self.file_picker_canvas.bind('<Configure>', lambda e: self.file_picker_canvas.configure(scrollregion=self.file_picker_canvas.bbox("all")))
        self.file_picker_canvas.bind('<MouseWheel>', self.on_mousewheel)

        self.file_picker_label = ttk.Label(self.file_picker_canvas, background="#2A508C")
        self.file_picker_canvas.create_window((0, 0), window=self.file_picker_label, anchor=tk.NW)
        self.file_picker_label.bind('<MouseWheel>', self.on_mousewheel)

        self.context_menu = tk.Menu(self.window, tearoff=False)
        self.context_menu.add_command(label="Διαγραφή Αρχείου")

        self.file_buttons = []
        for i in range(len(self.files)):
            row = i // 3; column = i % 3
            button = self.create_file_button(self.file_picker_label, i, self.files[i], row, column)
            button.bind('<MouseWheel>', self.on_mousewheel)
            button.bind('<Button-3>', lambda event, button=button, index=i: show_context_menu(event, button, index))
            self.file_buttons.append(button)

    def delete_single_file(self, button):
        if messagebox.askyesno("Διαγραφή Προεπιλεγμένου Αρχείου", "Σίγουρα θέλετε να διαγράψετε το αρχείο;"):
            button.destroy()

    def add_file(self):
        filetypes = (("Excel files", "*.xls"),)
        new_file_path = filedialog.askopenfilename(title="Επιλογή Αρχείου", filetypes=filetypes)
        if f"{new_file_path}\n" in self.files:
            messagebox.showwarning("Ήδη Υπάρχον Αρχείο", f"Το αρχείο {new_file_path} έχει ήδη οριστεί ως προεπιλογή")
            return
        if new_file_path:
            with open(FILES_PATH_, "a", encoding="utf-8") as file:
                file.write(f"{new_file_path}\n")
        self.buttons_frame.destroy()
        self.file_picker_canvas.destroy()
        self.create_file_picker()
        self.create_buttons()

    def delete_files(self):
        self.delete_files_window = DeleteFilesWindow()
        self.delete_files_window.run()

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.window, bg="#2A508C"); self.buttons_frame.pack()
        
        self.add_icon = resizeImage(self.add_icon_image, int((13/10)*self.font_size))
        self.add_button = tk.Button(self.buttons_frame, text="ΠΡΟΣΘΗΚΗ ΑΡΧΕΙΟΥ", font=('Arial', int((8/10)*self.font_size)), image=self.add_icon, compound="left", padx=int((7/10)*self.font_size), command=self.add_file)
        self.add_button.pack(padx=int((1/35)*self.width))

        # self.delete_icon = resizeImage(self.delete_icon_image, int((13/10)*self.font_size))
        # self.delete_button = tk.Button(self.buttons_frame, text="ΔΙΑΓΡΑΦΗ ΑΡΧΕΙΩΝ", font=('Arial', int((8/10)*self.font_size)), image=self.delete_icon, compound="left", padx=int((7/10)*self.font_size), command=self.delete_files)
        # self.delete_button.grid(row=0, column=1, padx=int((1/35)*self.width))

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

    def run(self):
        self.initialize_window()
        self.create_main_label()
        self.create_file_picker()
        self.create_buttons()
        self.create_menu_bar()

        self.window.mainloop()
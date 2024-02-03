import tkinter as tk
from initialization import *
from tkinter import messagebox

class ChangePasswordWindow:

    POLICE_LOGO_IMAGE_PATH = POLICE_LOGO_IMAGE_PATH_
    HIDE_PASSWORD_IMAGE_PATH = HIDE_LOGO_IMAGE_PATH_
    VIEW_PASSWORD_IMAGE_PATH = VIEW_LOGO_IMAGE_PATH_

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
        self.height = int((8/10)*self.geometry_data['height'])
        self.spawn_x = self.geometry_data['spawn_x'] + (self.geometry_data['width'] - self.width)//2
        self.spawn_y = self.geometry_data['spawn_y'] + (self.geometry_data['height'] - self.height)//2
        self.window.geometry(f"{self.width}x{self.height}+{self.spawn_x}+{self.spawn_y}")

        # Initialize all the font options
        self.font_size = self.geometry_data['font_size']
        self.label_font = ('Arial', int(self.font_size*(0.8)), 'bold')
        self.password_font = ('Arial', int(self.font_size*(1)))
        self.button_font = ('Arial', int(self.font_size*(0.9)))

        # Initialize the title, the icon, and the background color of the window
        self.window.title("Εισαγωγή Νέου Κωδικού Πρόσβασης")
        self.window.iconphoto(True, self.police_icon_image)
        self.window.config(bg="#2A508C")

        # Initialize some other options
        self.pad_y = int((1/15)*self.width)

    def create_main_label1(self):
        self.main_label_image = resizeImage(self.police_icon_image, int((1/15)*self.height))
        self.main_label = tk.Label(self.window, text="ΕΙΣΑΓΕΤΕ ΤΟΝ ΝΕΟ ΚΩΔΙΚΟ ΠΡΟΣΒΑΣΗΣ:", font=self.label_font, fg="white", bg="#2A508C",
                                   image=self.main_label_image, compound="left", padx=int((1/50)*self.width))
        self.main_label.pack(pady=self.pad_y)

    def create_main_label2(self):
        self.main_label = tk.Label(self.window, text="ΕΠΑΛΗΘΕΥΣΤΕ ΤΟΝ ΝΕΟ ΚΩΔΙΚΟ ΠΡΟΣΒΑΣΗΣ:", font=self.label_font, fg="white", bg="#2A508C",
                                   padx=int((1/50)*self.width))
        self.main_label.pack(pady=self.pad_y)

    def change_state1(self):
        if self.view1:
            self.password_entry1['show'] = '*'
            self.hide_unhide_button1['image'] = self.hide_icon1
            self.view1 = False
        else:
            self.password_entry1['show'] = ''
            self.hide_unhide_button1['image'] = self.view_icon1
            self.view1 = True
    
    def change_state2(self):
        if self.view2:
            self.password_entry2['show'] = '*'
            self.hide_unhide_button2['image'] = self.hide_icon2
            self.view2 = False
        else:
            self.password_entry2['show'] = ''
            self.hide_unhide_button2['image'] = self.view_icon2
            self.view2 = True

    def create_password_entry1(self):
        self.password_entry_frame1 = tk.Frame(self.window, bg="#2A508C")
        self.password_entry_frame1.pack()
        self.password_entry1 = tk.Entry(self.password_entry_frame1, font=self.password_font, borderwidth=int((1/100)*self.width), show="*")
        self.password_entry1.pack(side="left", pady=self.pad_y)

        self.view1 = False
        desired_size = int((3/48)*self.width)
        self.hide_icon1 = resizeImage(self.hide_password_icon_image, desired_size)
        self.view_icon1 = resizeImage(self.view_password_icon_image, desired_size)
        self.hide_unhide_button1 = tk.Button(self.password_entry_frame1, image=self.hide_icon1, command=self.change_state1)
        self.hide_unhide_button1.pack(side="left")
        self.password_entry1.focus()

    def create_password_entry2(self):
        self.password_entry_frame2 = tk.Frame(self.window, bg="#2A508C")
        self.password_entry_frame2.pack()
        self.password_entry2 = tk.Entry(self.password_entry_frame2, font=self.password_font, borderwidth=int((1/100)*self.width), show="*")
        self.password_entry2.pack(side="left", pady=self.pad_y)

        self.view2 = False
        desired_size = int((3/48)*self.width)
        self.hide_icon2 = resizeImage(self.hide_password_icon_image, desired_size)
        self.view_icon2 = resizeImage(self.view_password_icon_image, desired_size)
        self.hide_unhide_button2 = tk.Button(self.password_entry_frame2, image=self.hide_icon2, command=self.change_state2)
        self.hide_unhide_button2.pack(side="left")

    def create_submit_button(self):
        self.submit_button = tk.Button(self.window, text="ΕΠΙΒΕΒΑΙΩΣΗ", font=self.button_font, command=self.check)
        self.submit_button.pack(pady=self.pad_y)

    def check(self, temp=None):
        if self.password_entry1.get() != self.password_entry2.get():
            self.window.attributes('-topmost', False)
            messagebox.showerror("Ανισότητα Στους Κωδικούς", "Οι κωδικοί πρόσβασης δεν ταιριάζουν.")
            self.window.attributes('-topmost', True)
            self.password_entry2.focus()
            return
        
        with open(PASSWORD_PATH_, "w", encoding="utf-8") as file:
            file.write(self.password_entry1.get())
        self.window.attributes('-topmost', False)
        messagebox.showinfo("Επιτυχής Ανανέωση Κωδικού Πρόσβασης", "Ο κωδικός πρόσβασης ανανεώθηκε με επιτυχία.")
        self.window.destroy()

    def run(self):
        self.initialize_window()
        self.create_main_label1()
        self.create_password_entry1()
        self.create_main_label2()
        self.create_password_entry2()
        self.create_submit_button()
        self.password_entry1.bind('<Return>', lambda e: self.password_entry2.focus())
        self.password_entry2.bind('<Return>', lambda e: self.check())

        self.window.mainloop()
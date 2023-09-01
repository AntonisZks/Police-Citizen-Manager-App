import tkinter as tk
from tkinter import ttk
from support import *


""" The DatabasePickerFrame class stands for the starting frame of the Application """
class DatabasePickerFrame:
    def __init__(self, data):
        """ Initialize some options """
        self.setupStructureOptions(data)

        """ Initializing all the images used in the frame """
        self.initializeImages()

        """ Creating the actual frame """
        self.parent_widget = self.parent_data['window'] # The parent widget is goin to be the main window
        self.frame = tk.Frame(self.parent_widget, bg=self.parent_data['bg-color']) # creating the actual frame

        """ Creating the structure of the frame """
        self.createHeaderFrame() # First create the header
        self.createBodyFrame() # Then create the body
        self.createFooterFrame() # Finally create the footer

        """ Packing the frame into the parent window """
        self.frame.pack()

    def initializeImages(self):
        self.police_logo_image = tk.PhotoImage(file=self.header_options['image-path'])
        self.add_image = tk.PhotoImage(file=self.footer_options['add-button-image-path'])

    def setupStructureOptions(self, data):
        self.parent_data = data
        self.header_options = {
            "title": "ΕΛΛΗΝΙΚΗ ΑΣΤΥΝΟΜΙΑ\nΑ.Τ. ΗΡΑΚΛΕΙΟΥ ΑΤΤΙΚΗΣ\nΠΡΟΓΡΑΜΜΑ ΑΡΧΕΙΟΘΕΤΗΣΗΣ\nΥΠΟΘΕΣΕΩΝ ΠΟΛΙΤΩΝ",
            "image-path": POLICE_LOGO_PNG_PATH,
            "font": ('Arial', round(0.022*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold')}
        
        self.body_options = {
            "message-title": textSpaced("ΓΙΑ  ΣΥΝΕΧΕΙΑ  ΕΠΙΛΕΞΤΕ  ΑΡΧΕΙΟ:"),
            "font": ('Arial', round(0.018*max(self.parent_data['window-width'], self.parent_data['window-height'])), 'bold')}
        
        self.footer_options = {
            "add-button-text": "ΠΡΟΣΘΗΚΗ ΑΡΧΕΙΟΥ",
            "add-button-image-path": ADD_PNG_PATH,
            "font": ('Arial', round(0.018*max(self.parent_data['window-width'], self.parent_data['window-height'])))}

    def onMousewheel(self, event):
        # Get the current scroll position (as a fraction) relative to the maximum scroll
        current_scroll_frac = self.file_picker_area.yview()[0]
        
        if event.delta > 0:  # Scrolling upwards
            if current_scroll_frac <= 0.0: return  # Don't scroll further up if already at the top
            self.file_picker_area.yview_scroll(int(-1*(event.delta/120)), "units")
        else:  # Scrolling downwards
            if current_scroll_frac >= 1.0: return  # Don't scroll further down if already at the bottom
            self.file_picker_area.yview_scroll(int(-1*(event.delta/120)), "units")

    def createHeaderFrame(self):
        self.header = tk.Frame(self.frame, bg=self.parent_data['bg-color']) # Creating the header frame

        """ Creating the Header Label """
        self.header_image = resizeImage(self.police_logo_image, round(0.13*self.parent_data['window-width']))
        self.header_label = tk.Label(self.header, 
                                     text=self.header_options['title'],
                                     font=self.header_options['font'], 
                                     bg=self.parent_data['bg-color'], 
                                     fg=self.parent_data['label-fg-color'], 
                                     image=self.header_image, compound=tk.LEFT, 
                                     padx=round(0.04*self.parent_data['window-width']),
                                     pady=round(0.04*(self.parent_data['window-height'])))

        """ Packing the header and its widgets """
        self.header_label.pack()
        self.header.pack()

    def createBodyFrame(self):
        self.body = tk.Frame(self.frame, bg=self.parent_data['bg-color']) # Creating the body frame

        """ Creating the Body Label Message """
        self.body_label_message = tk.Label(self.body, text=self.body_options['message-title'],
                                           font=self.body_options['font'], 
                                           bg=self.parent_data['bg-color'], 
                                           fg=self.parent_data['label-fg-color'])

        """ Creating the file picker area containining the databases' buttons """
        self.file_picker_area = tk.Canvas(self.body, 
                                          background=self.parent_data['bg-color-dark'], 
                                          highlightbackground=self.parent_data['bg-color'],
                                          width=round(0.9*self.parent_data['window-width']), 
                                          height=round(0.5*self.parent_data['window-height']))
        
        self.file_picker_area.bind('<Configure>', lambda e: self.file_picker_area.configure(scrollregion=self.file_picker_area.bbox("all")))
        self.file_picker_area.bind('<MouseWheel>', self.onMousewheel)

        self.file_picker_frame = ttk.Label(self.file_picker_area, background=self.parent_data['bg-color-dark'])
        self.file_picker_area.create_window((0, 0), window=self.file_picker_frame, anchor=tk.NW)
        self.file_picker_frame.bind('<MouseWheel>', self.onMousewheel)

        """ Creating a scrollbar for the file picker area """
        self.file_picker_scrollbar = tk.Scrollbar(self.file_picker_area, orient=tk.VERTICAL, command=self.file_picker_area.yview)
        self.file_picker_area.config(yscrollcommand=self.file_picker_scrollbar.set)

        """ Packing the body and its widgets """
        self.body_label_message.pack()
        self.file_picker_area.pack(padx=round(0.05*self.parent_data['window-width']), pady=round(0.04*self.parent_data['window-height']))
        self.file_picker_scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.body.pack()

    def createFooterFrame(self):
        self.footer = tk.Frame(self.frame, bg=self.parent_data['bg-color']) # creating the footer frame

        """ Creating the 'Add File' button """
        self.add_file_image = resizeImage(self.add_image, round(1.3*self.footer_options['font'][1]))
        self.add_file_button = tk.Button(self.footer, text=self.footer_options['add-button-text'],
                                         font=self.footer_options['font'], 
                                         image=self.add_file_image, 
                                         compound=tk.LEFT, 
                                         padx=round(0.7*self.footer_options['font'][1]))

        """ Packing the footer and its widgets """
        self.footer.pack()
        self.add_file_button.pack(padx=round(0.028*self.parent_data['window-width']))

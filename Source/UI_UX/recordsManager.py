import tkinter as tk
from tkinter import ttk
from support import *
from .record import Record

def makeRecordButtonText(i, record):
    # Creating the text of the button
    button_text = f"{i+1})    " if (i+1) < 10 else f"{i+1})  "
    if record.father_name == "": button_text += f"{record.surname} {record.name}"
    else:
        ending = record.father_name[-2:]
        if ending == "ΗΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending == "ΑΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending == "ΟΣ": button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}Υ"
        elif ending in ("ης", "ησ"): button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending in ("ας", "ασ"): button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}"
        elif ending in ("ος", "οσ"): button_text += f"{record.surname} {record.name}   του {record.father_name[:-1]}υ"
        else: button_text += f"{record.surname} {record.name}   του {record.father_name}"

    return button_text

class RecordsManager:
    def __init__(self, parent_widget, app_data, width, height, bg_color, no_record_message_options):
        self.app_data = app_data
        self.no_records_message_options = no_record_message_options
        self.notebook = ttk.Notebook(parent_widget, width=width, height=height)
        self.area = tk.Canvas(self.notebook, width=width, height=height, background=bg_color, highlightbackground=bg_color)
        self.frame = ttk.Label(self.area, background=bg_color)
        self.area.create_window((0, 0), window=self.frame, anchor=tk.NW, width=width)
        self.area.bind('<MouseWheel>', lambda e: onMousewheel(e, self.area))

        self.scrollbar = None
        self.selected_buttons = {}
        self.visualiser = None

    def __onButtonClick(self, records):
        selected_indeces = [i for i, value in enumerate(self.checkbuttons_var) if value.get() == 1]
        for index in selected_indeces:
            if index == len(self.checkbuttons_var) - 1:
                index = -1
            if index not in self.selected_buttons:
                self.visualiser.createTab(index, records[index+1])

        for index in list(self.selected_buttons.keys()):
            solve = False
            if index == -1:
                index = len(self.checkbuttons_var) - 1
                solve = True
            if index not in selected_indeces:
                self.visualiser.removeTab(-1) if solve else self.visualiser.removeTab(index)

    def createRecordButtons(self, records_df, font):
        # Cleaning any previous results and destroying the 'No Records' message and the Scrollbar
        for child_widget in self.frame.winfo_children():
            child_widget.destroy()
        if self.scrollbar is not None:
            self.scrollbar.destroy()
        
        records = []
        for _, record in records_df.iterrows():
            records.append(Record(*record.to_list()))

        # Checking if there is any record as a result
        if len(records) == 0:
            self.createNoRecordsMessage()
            self.notebook.tab(0, text="")
            return
        
        # Creating the side scrollbar
        self.createScrollBar()

        # Creating the record buttons
        self.checkbuttons_var = [tk.IntVar() for _ in range(len(records))]
        for i, record in enumerate(records):
            new_record_button = tk.Checkbutton(
                self.frame, 
                text=makeRecordButtonText(i, record), 
                font=font, anchor=tk.W, 
                onvalue=1, offvalue=0, 
                variable=self.checkbuttons_var[i-1]
            )
            new_record_button.config(indicatoron=False, selectcolor=self.app_data['theme-color-light'])  
            new_record_button.bind('<MouseWheel>', lambda e: onMousewheel(e, self.area))  
            new_record_button.pack(side="top", fill="x")

        # Updating the tab title to be the number of records returned
        if i+1 > 1: self.notebook.tab(0, text=f"{i+1} αποτελέσματα")
        else: self.notebook.tab(0, text=f"{i+1} αποτέλεσμα")

        for var in self.checkbuttons_var:
            var.trace("w", lambda *args: self.__onButtonClick(records))

        # Updating the scrollregion of the record area
        self.area.update_idletasks()
        self.area.configure(scrollregion=self.area.bbox("all"))

    def createNoRecordsMessage(self):
        self.no_records_message = tk.Label(
            self.frame, 
            text=self.no_records_message_options['text'], 
            font=self.no_records_message_options['font'], 
            bg=self.no_records_message_options['bg'], 
            fg=self.no_records_message_options['fg']
        )
        self.no_records_message.pack(pady=round(0.3*self.app_data['window-height']))

    def createScrollBar(self):
        self.scrollbar = tk.Scrollbar(self.area, orient=tk.VERTICAL, command=self.area.yview)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        self.area.config(yscrollcommand=self.scrollbar.set)

    def show(self, row, column, padx, pady):
        self.notebook.grid(row=row, column=column, padx=padx, pady=pady)
        self.area.pack()
        self.notebook.add(self.area, text="")

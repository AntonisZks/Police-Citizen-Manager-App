import tkinter as tk
from tkinter import ttk


class RecordsVisualiser:
    def __init__(self, parent_widget, app_data, width, height, bg_color, no_record_selected_message_options):
        self.no_record_selected_message_options = no_record_selected_message_options
        self.app_data = app_data
        self.bg_color = bg_color
        self.notebook = ttk.Notebook(parent_widget, width=width, height=height)

        self.manager = None
        self.n_selected_results = 0

    def createTab(self, index, record):
        tab_frame = record.createDataFrame(self.notebook, self.app_data)

        # Deleting the first temporary tab
        if self.n_selected_results == 0:
            self.notebook.forget(0)

        self.notebook.add(tab_frame, text=record.surname)
        self.manager.selected_buttons[index] = tab_frame
        self.n_selected_results += 1

        self.notebook.select(tab_frame)

    def removeTab(self, index):
        tab_frame = self.manager.selected_buttons.pop(index)
        self.notebook.forget(tab_frame)
        self.n_selected_results -= 1
        
        if self.n_selected_results == 0:
            self.addTemporaryTab()
            self.notebook.add(self.temp_tab, text="")

    def addTemporaryTab(self):
        self.temp_tab = tk.Frame(self.notebook, background=self.bg_color)
        self.temp_label = tk.Label(
            self.temp_tab, 
            text=self.no_record_selected_message_options['text'],
            font=self.no_record_selected_message_options['font'],
            bg=self.no_record_selected_message_options['bg'],
            fg=self.no_record_selected_message_options['fg']
        )
        self.temp_label.pack(pady=round(0.26*self.app_data['window-height']))

    def show(self, row, column, padx, pady):
        self.notebook.grid(row=row, column=column, padx=padx, pady=pady)
        self.notebook.add(self.temp_tab, text="")

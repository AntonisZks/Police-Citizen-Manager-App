"""
The 'recordsVisualizer.py' file includes the RecordVisualizer class, which implements the idea of visualizing people's data. Its structure is a tkinter notebook that contains as many tabs as the user wants.
Each tab contains the information about a specific person (their data). The user can navigate through these tabs, and in that way they have a look at the data on various people at the same time. The selected
tabs in the notebook are being chosen by the user in the 'recordsManager.py' file.

"""

import tkinter as tk
from tkinter import ttk
from typing import Any
from Source.UI_UX.RecordsStuff.record import Record


class ResultRecordDataVisualizer:
    def __init__(self, parentWidget: tk.Widget, applicationSettings: dict[str, Any], width: int, height: int, bgColor: str, noRecordSelectedMessageSettings: dict[str, Any]) -> None:
        """ The constructor of the records' visualizer.

        Args:
            parentWidget (tkinter.Widget): The widget that contains the visualizer.
            applicationSettings (dict[str, Any]): The settings of the application.
            width (int): The width of the notebook.
            height (int): The height of the notebook.
            bgColor (str): The background color of the notebook and each tab.
            noRecordSelectedMessageSettings (dict[str, Any]): Some settings that refer to the 'No Record Selected' label.

        """

        # Initializing some temporary data
        self.tempLabel = None
        self.tempTab = None
        self.listVisualizer = None

        # Initializing the attributes
        self.noRecordSelectedMessageSettings = noRecordSelectedMessageSettings
        self.applicationSettings = applicationSettings
        self.bgColor = bgColor
        self.notebook = ttk.Notebook(parentWidget, width=width, height=height)

        self.selectedResultsCounter = 0  # Counter of the records that have been selected by the user

    def createTab(self, index: int, record: Record) -> None:
        """ Creates and adds a new tab to the notebook. Each tab contains the data of a specific person.

        Args:
            index (int): An index referring to the selected record.
            record (Record): The actual record we want to add its data to the tab.

        """
        tab_frame = record.createDataFrame(self.notebook, self.applicationSettings)

        # Deleting the first temporary tab
        if self.selectedResultsCounter == 0:
            self.notebook.forget(0)

        # Adding a new tab to the notebook
        self.notebook.add(tab_frame, text=record.surname)
        self.listVisualizer.selected_buttons[index] = tab_frame
        self.selectedResultsCounter += 1  # Increase the selected results counter by 1

        self.notebook.select(tab_frame)  # Setting the new tab in the notebook, as an active one

    def removeTab(self, index: int) -> None:
        """ Removes a tab from the notebook.

        Args:
            index (int): The index of the tab we want to remove

        """

        # Getting the tab at the given index
        tab_frame = self.listVisualizer.selected_buttons.pop(index)
        self.notebook.forget(tab_frame)   # Removing the tab from the notebook
        self.selectedResultsCounter -= 1  # Decreasing the selected records counter by 1

        # If there are no selected records (no tabs) then create a temporary tab with no title, and its interior contains a 'No Selected Records' message
        if self.selectedResultsCounter == 0:
            self.addTemporaryTab()                    # Creating the temporary tab
            self.notebook.add(self.tempTab, text="")  # Adding the temporary tab in the notebook

    def addTemporaryTab(self) -> None:
        """ Adds a temporary tab in the notebook. The temporary tab of the RecordVisualizer class, is a special tab used only to notify the user that no record has been selected by them. """

        # Creating the temporary tab and its 'No Selected Record' label
        self.tempTab = tk.Frame(self.notebook, background=self.bgColor)
        self.tempLabel = tk.Label(self.tempTab, text=self.noRecordSelectedMessageSettings['text'], font=self.noRecordSelectedMessageSettings['font'], bg=self.noRecordSelectedMessageSettings['bg'], fg=self.noRecordSelectedMessageSettings['fg'])
        self.tempLabel.pack(pady=round(0.30 * self.applicationSettings['window-height']))  # Packing the label in the temporary tab

    def show(self, row, column, padx, pady):
        self.notebook.grid(row=row, column=column, padx=padx, pady=pady)
        self.notebook.add(self.tempTab, text="")

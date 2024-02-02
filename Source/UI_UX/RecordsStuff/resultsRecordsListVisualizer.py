"""
The 'recordsManager.py' file contains the RecordsManager class the implements the basic visualizer of the results records from the search process. Is used to display the results onto the screen, as list of check buttons.
When the user want toy view the data of a specific record, they just click on the button the want to inspect. The data of that record are being transferred to the recordVisualizer class and from there they appear onto the
screen. The user has the advantage of selecting multiple records and reviewing their data at the same time. That's why the check button is preferred here, rather than the regular button. To have the option of selecting
multiple records at the same time. The way it is implemented is actually by making a tkinter notebook with only one tab. And that tab contains the whole structure of the record's manager widget.

"""

from tkinter import ttk
from Extras.support import *
from UI_UX.RecordsStuff.record import Record
from typing import Any


def makeRecordButtonText(index: int, record: Record):
    """ Creates a record button that contains a main text describing the person that is being described inside the button.

    Args:
        index (int): The index of the button
        record (Record): The actual record, the button describes.

    """

    # Creating the text of the button
    button_text = f"{index + 1})    " if (index + 1) < 10 else f"{index + 1})  "
    if record.father_name == "":
        button_text += f"{record.surname} {record.name}"
    else:
        ending_map = {"ΗΣ": "", "ΑΣ": "", "ΟΣ": "Υ", "ης": "", "ησ": "", "ας": "", "ασ": "", "ος": "υ"}

        ending = record.father_name[-2:]
        button_text = button_text + f"{record.surname} {record.name} του {record.father_name[:-1]}{ending_map[ending]}" if ending in ending_map else button_text + f"{record.surname} {record.name} του {record.father_name}"

    return button_text


class ResultsRecordsListVisualizer:
    def __init__(self, parentWidget: tk.Widget, applicationSettings: dict[str, Any], width: int, height: int, bgColor: str, noRecordMessageSettings: dict[str, Any]):
        """ The constructor of the record's manager.

        Args:
            parentWidget (tkinter.Widget): The widget that contains the manager.
            applicationSettings (dict[str, Any]): The settings of the application.
            width (int): The width of the notebook.
            height (int): The height of the notebook.
            bgColor (str): The background color of the notebook and each tab.
            noRecordMessageSettings (dict[str, Any]): Some settings that refer to the 'No Record' label.

        """

        # initializing some temporary data
        self.records = None
        self.checkButtonsVar = None
        self.no_records_message = None
        self.scrollbar = None
        self.dataVisualiser = None

        # Initializing the attributes
        self.app_data = applicationSettings
        self.no_records_message_options = noRecordMessageSettings
        self.notebook = ttk.Notebook(parentWidget, width=width, height=height)
        self.area = tk.Canvas(self.notebook, width=width, height=height, background=bgColor, highlightbackground=bgColor)
        self.frame = ttk.Label(self.area, background=bgColor)
        self.area.create_window((0, 0), window=self.frame, anchor=tk.NW, width=width)
        self.area.bind('<MouseWheel>', lambda e: onMousewheel(e, self.area))

        self.selected_buttons = {}  # A dictionary that contains the buttons that are being selected during the process, as values and as keys their indexes

    def __onButtonClick(self, records: list[Record]) -> None:
        """ Runs after the user clicks on a button. When this happens the method allocates witch button has been clicked and figures out if it is pressed or not. If it is, the method
            removes the tab corresponding to the button from the record's visualizer notebook, and if it isn't then the method adds a new tab in the record's visualizer notebook, containing
            the data of that record button.

        Args:
            records (list[Record]): A list that contains the indexes of the record buttons.

        """

        selected_indices = [i for i, value in enumerate(self.checkButtonsVar) if value.get() == 1]  # Selecting the indexes of the buttons that are selected

        # Iterate through the selected buttons indexes and decide whether to create a new tab, or not
        for index in selected_indices:
            if index == len(self.checkButtonsVar) - 1:
                index = -1

            if index not in self.selected_buttons:
                self.dataVisualiser.createTab(index, records[index + 1])  # if the current index is not in the current selected button indexes, then create a new tab

        # Iterate through the list of the selected buttons keys and decide whether to remove a tab from the record's visualizer notebook, or not
        for index in list(self.selected_buttons.keys()):
            solve = False
            if index == -1:
                index = len(self.checkButtonsVar) - 1
                solve = True

            if index not in selected_indices:
                self.dataVisualiser.removeTab(-1) if solve else self.dataVisualiser.removeTab(index)  # If the current index is not in the current selected buttons indexes, then remove its tab

    def createRecordButtons(self, records_df: pd.DataFrame, font: tuple[str, int]) -> None:
        """ Creates the result list that contains the check buttons corresponding to the result records after the search process.

        Args:
            records_df (pandas.DataFrame): A dataframe that contains the data of all the result records, the search process returned.
            font (tuple[str, int]): the font of the check buttons.

        """

        rowIndexes = [index for index in records_df.index]

        # Cleaning any previous results and destroying the 'No Records' message and the Scrollbar
        for child_widget in self.frame.winfo_children():
            child_widget.destroy()

        if self.scrollbar is not None:
            self.scrollbar.destroy()

        self.records = []  # Creating an empty list that will contain all the records

        # Iterate through the records dataframe and add every line to the records list
        i = 0
        for _, record in records_df.iterrows():
            newRecord = Record(*record.to_list())
            newRecord.databaseIndex = rowIndexes[i]
            self.records.append(newRecord)  # Convert every line of the dataframe to a python list and add it to the records list

            i += 1

        # Checking if there is any record as a result
        if len(self.records) == 0:
            self.createNoRecordsMessage()  # If there is no record, create a 'No Records' message
            self.notebook.tab(0, text="")  # Applying the text of the only tab in the record's manager notebook, to be nothing ("")
            return

        self.createScrollBar()  # Creating the side scrollbar

        # Creating the record buttons
        self.checkButtonsVar = [tk.IntVar() for _ in range(len(self.records))]  # Creating a list containing the states of every button (ON/OFF)
        index: int = 0
        for i, record in enumerate(self.records):
            new_record_button = tk.Checkbutton(self.frame, text=makeRecordButtonText(i, record), font=font, anchor=tk.W, onvalue=1, offvalue=0, variable=self.checkButtonsVar[i - 1])
            new_record_button.config(indicatoron=False, selectcolor=self.app_data['theme-color-light'])
            new_record_button.bind('<MouseWheel>', lambda e: onMousewheel(e, self.area))
            new_record_button.pack(side="top", fill="x")

            index += 1

        # Updating the tab title to be the number of records returned
        self.notebook.tab(0, text=f"{index} αποτελέσματα") if index > 1 else self.notebook.tab(0, text=f"{index} αποτέλεσμα")

        # Tracing every state in the check buttons list with the __onButtonClick() method
        for var in self.checkButtonsVar:
            var.trace("w", lambda *args: self.__onButtonClick(self.records))

        # Updating the scroll-region of the record area
        self.area.update_idletasks()
        self.area.configure(scrollregion=self.area.bbox("all"))

    def createNoRecordsMessage(self) -> None:
        """ Creates a 'No Records' label message onto the screen. """

        # Creating the label
        self.no_records_message = tk.Label(self.frame, text=self.no_records_message_options['text'], font=self.no_records_message_options['font'], bg=self.no_records_message_options['bg'], fg=self.no_records_message_options['fg'])
        self.no_records_message.pack(pady=round(0.26 * self.app_data['window-height']))  # Packing the label onto the screen

    def createScrollBar(self):
        """ Creates a side scrollbar in order to let the user navigate through all the returned result record buttons in the list. """

        self.scrollbar = tk.Scrollbar(self.area, orient=tk.VERTICAL, command=self.area.yview)  # Creating the scrollbar
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE)                        # Placing the scrollbar onto the screen
        self.area.config(yscrollcommand=self.scrollbar.set)                                    # Setting the functionality of the scrollbar

    def show(self, row: int, column: int, padx: int, pady: int) -> None:
        """ Places the manager onto the scene. the manager is in fact a tkinter notebook with only one tab and this tab contains every time the list of returned record buttons.

        Args:
            row (int): The row the notebook is being placed at.
            column (int): The column the notebook is being placed at.
            padx (int): Some padding on the x-axis.
            pady (int): Some padding on the y-axis.


        """
        self.notebook.grid(row=row, column=column, padx=padx, pady=pady)  # Griding the notebook to the scene
        self.area.pack()                                                  # Packing the area containing the notebook
        self.notebook.add(self.area, text="")                             # Add the only tab existing in the notebook

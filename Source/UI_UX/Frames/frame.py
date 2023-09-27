"""
The 'frame.py' module contains the abstract base class for frames used in the application. The main window application contains 5 basic frames,
the databasePickerFrame, the mainMenuFrame, the searchFrame, the insertFrame and the updateFrame which are all described in their own implementation file.
The basic structure idea of a frame is to have 3 parts. The header, the body and the footer. Note that some of these parts can be excluded from the
frame's structure, especially the footer one. In every frame there is a variety of images that can be used in it. So each frame must contain a special method
that initializes all the appropriate images, that are going to be used. the structure of each frame contains some useful options about the functionality and the
graphical look of the frame and as a result every frame has to implement a method for it, in order to initialize all these options and then use them. the structure
of the frame is being built threw special methods like createHeader(), createBody() and createFooter(). The previous ideas are implemented with abstract methods in
this file, and all the classes that inherits the main Frame class, have to implement them.

"""

import tkinter as tk
from abc import ABC, abstractmethod
from typing import Any


class IFrame(ABC, tk.Frame):
    """ The abstract base class for frames used in the application. Contains some useful methods for the UI and UX of the application,
    most of them being abstract methods.

    Attributes:
        parent_widget (Tk): The parent widget, which is the main window.
        app (object): The application object.
        applicationSettings (dict[str, Any]): Some settings of the applications

    Methods:
        __init__(data): The constructor of the Frame class.
        build(): Abstract method to build the frame.
        destroy(): Destroy the frame.
        _initializeImages(): Abstract method to initialize frame-specific images.
        _setupStructureOptions(data): Abstract method to set up frame structure options.
        _buildStructure(): Abstract method to build the general structure of the frame.
        _createHeaderFrame(): Abstract method to create the header frame.
        _createBodyFrame(): Abstract method to create the body frame.
        _createFooterFrame(): Abstract method to create the footer frame.

    """

    def __init__(self, applicationSettings: dict[str, Any]) -> None:
        """ The constructor of the Frame class. Here the actual frame is being built while some additional data
            are being initialized such as application options.

        Args:
            applicationSettings (dict[str, any]): The settings of the parent widget (Application Window).

        Attributes:
            parent_widget (Tk): The parent widget is the main window.
            app (object): Storing the application object.
            application_data (dict[str, Any]): the settings of the application.

        """
        super().__init__(applicationSettings['window'], bg=applicationSettings['theme-color'])  # Calling the constructor of the tkinter.Frame class
        self.applicationSettings = applicationSettings                                          # Applying the application settings
        self.parent_widget = applicationSettings['window']                                      # The parent widget is going to be the main window
        self.app = applicationSettings['object']                                                # Storing the application object

        # Set up the header, body, and footer options and initialize the images used
        self._setupStructureOptions(self.applicationSettings)
        self._initializeImages()

    def build(self) -> None:
        """ The build() method builds the actual frame. This method is common for all the frames because all it does is calling
            the _buildStructure() abstract method of each frame. """

        self._buildStructure()                                 # Building the structure
        self._setupStructureOptions(self.applicationSettings)  # Setting up the structure options

    def destroy(self) -> None:
        """ The destroy() method 'unpacks' the frame and destroys its children widgets. This method is common for all frames.
            Each frame has a specific frame object and the method just unpacks it from the main window, after destroying all
            its children widgets. """

        # Destroying all the frame's children widgets
        for child_widget in self.winfo_children():
            child_widget.destroy()
        
        self.pack_forget()  # Unpacking the frame from its parent

    @abstractmethod
    def _initializeImages(self) -> None:
        """ Abstract method to initialize all the images used in the frame. Each frame has a different number of images used,
            so each one implements its own _initializeImages() method. """

    @abstractmethod
    def _setupStructureOptions(self, parentWidgetSettings: dict[str, Any]) -> None:
        """ Abstract method to initialize some options for all three frames that form the whole structure of the frame.
            Some of these options are images, colors, fonts, texts, etc. Each frame has its own type of structure, so every frame
            has its own _initializeStructure() method.

        Args:
            parentWidgetSettings (dict[str, Any]): The settings of the parent widget.
        """

    @abstractmethod
    def _buildStructure(self) -> None:
        """ Abstract method to build the general structure of the frame (Header, Body, Footer). Each frame has a different type of structure,
            so each one implements its own _initializeStructure() method. """

    @abstractmethod
    def _createHeaderFrame(self) -> None:
        """ Abstract method used by the _buildStructure() method to build the header frame of the main structure. Each frame has its own header type,
            so it also has its own _createHeaderFrame() method. """

    @abstractmethod
    def _createBodyFrame(self) -> None:
        """ Abstract method used by the _buildStructure() method to build the body frame of the main structure. Each frame has its own body type,
            so it also has its own _createBodyFrame() method. """

    @abstractmethod
    def _createFooterFrame(self) -> None:
        """ Abstract method used by the _buildStructure() method to build the footer frame of the main structure. Each frame has its own footer type,
            so it also has its own _createFooterFrame() method. """

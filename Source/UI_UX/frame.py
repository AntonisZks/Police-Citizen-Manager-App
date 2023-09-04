"""
The 'frame.py' module contains the abstract base class for frames used in the application.

"""

import tkinter as tk
from abc import ABC, abstractmethod


class Frame(ABC):
    """
    The abstract base class for frames used in the application.

    Attributes:
        parent_widget (Tk): The parent widget, which is the main window.
        app (object): The application object.
        frame (Frame): The actual frame widget.

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

    def __init__(self, data: dict[str, any]) -> None:
        """
        The constructor of the Frame class. Here the actual frame is being built while some additional data
        are being initialized such as application options.

        Args:
            data (dict[str, any]): The data of the parent widget.

        Attributes:
            parent_widget (Tk): The parent widget is the main window.
            app (object): Storing the application object.
            frame (Frame): The actual frame widget.

        """
        self.parent_widget = data['window']  # The parent widget is going to be the main window
        self.app = data['object']  # Storing the application object
        self.frame = tk.Frame(self.parent_widget, bg=data['theme-color'])
        self.frame.pack()

    def build(self) -> None:
        """
        The build() method builds the actual frame. This method is common for all the frames because all it does is calling
        the _buildStructure() abstract method of each frame.

        """
        self._buildStructure()

    def destroy(self) -> None:
        """
        The sestroy() method destroy the frame. This method is common for all frames. Each frame has a specific frame object,
        and the method just destroys it.

        """
        self.frame.destroy()

    @abstractmethod
    def _initializeImages(self) -> None:
        """
        Abstract method to initialize all the images used in the frame.
        Each frame has a different number of images used, so each one implements its own _initializeImages() method.
        
        """
        pass

    @abstractmethod
    def _setupStructureOptions(self, data: dict[str, any]) -> None:
        """
        Abstract method to initialize some options for all three frames that form the whole structure of the frame.
        Some of these options are images, colors, fonts, texts, etc.
        Each frame has its own type of structure, so every frame has its own _initializeStructure() method.

        Args:
            data (dict[str, any]): The data of the parent widget.

        """
        pass

    @abstractmethod
    def _buildStructure(self) -> None:
        """
        Abstract method to build the general structure of the frame (Header, Body, Footer).
        Each frame has a different type of structure, so each one implements its own _initializeStructure() method.

        """
        pass

    @abstractmethod
    def _createHeaderFrame(self) -> None:
        """
        Abstract method used by the _buildStructure() method to build the header frame of the main structure.
        Each frame has its own header style, so it also has its own _createHeaderFrame() method.

        """
        pass

    @abstractmethod
    def _createBodyFrame(self) -> None:
        """
        Abstract method used by the _buildStructure() method to build the body frame of the main structure.
        Each frame has its own body style, so it also has its own _createBodyFrame() method.

        """
        pass

    @abstractmethod
    def _createFooterFrame(self) -> None:
        """
        Abstract method used by the _buildStructure() method to build the footer frame of the main structure.
        Each frame has its own footer style, so it also has its own _createFooterFrame() method.

        """
        pass

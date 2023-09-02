"""
The support.py file contains some usefull constants and functions that is used by the program. Some of the constants are
colors used in the application and some paths corresponding to usefull files, for example images, json files etc.

"""

import tkinter as tk
import sys
import os


def resourcePath(relative_path: str) -> str:
    """
    The resourcePath() function returns the general path of a file on the current machine that is running the application.
    In this way we can make sure that all the files that we are using will not cause an error whenver we call them on any machine.
    This function was provided by Stack Overflow. The link is the following:
    https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

    Args:
        relative_path (str): The path to the file we want to use

    Returns:
        str: the full path of the given file on the current machine

    """
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resizeImage(img: tk.PhotoImage, desired_size: int) -> tk.PhotoImage:
    """
    The resizeImage() function is used to resize an image according to a given size. This function is often used in situations
    where we want to add an image in the application.

    Args:
        img (PhotImage): The image to resize
        desired_size (int): The given size the image has to be resized by

    Returns:
        PhotoImage: The final resized image
    
    """
    width_factor = img.width() // desired_size
    height_factor = img.height() // desired_size

    resized_img = img.subsample(width_factor, height_factor)
    return resized_img

def textSpaced(text: str, times:int = 1) -> str:
    """
    The textSpaced() function is used to return a given string but with spaces. The function let the user select the
    number of spaces he/she wants the string to have.

    Args:
        text (str): The string to be spaced
        times (int): The number of times

    Returns:
        str: The new string
    
    """
    new_text = text[0]
    for i in range(1, len(text)):
        new_text += " "*times
        new_text += text[i]
    return new_text

def getFileName(file_path: str) -> str:
    """
    The getFileName() function returns the name of the given file path.

    Args:
        file_path (str): The given file path

    Returns:
        str: The name of the file
    
    """
    if file_path[len(file_path)-1] == 's': return os.path.basename(file_path)[:-4]
    else: return os.path.basename(file_path)[:-5]

def onMousewheel(event: any, canvas: tk.Canvas) -> None:
    """
    The onMousewheel() function controls the behavious of the mouse wheel scrolling. It's often been used to situations where
    there is a scrollable item such as canvas etc in the program and we want to let the user scroll.

    Args:
        event (any): The event is usually the position of the mouse wheel in scrollable item.
        canvas (Canvas): The scrollable item where the user needs to scroll
    
    """
    # Get the current scroll position (as a fraction) relative to the maximum scroll
    current_scroll_frac = canvas.yview()[0]

    if event.delta > 0:  # Scrolling upwards
        if current_scroll_frac <= 0.0: return  # Don't scroll further up if already at the top
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    else:  # Scrolling downwards
        if current_scroll_frac >= 1.0: return  # Don't scroll further down if already at the bottom
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Defining all the colors used for the Application
BACKGROUND_COLOR_1 = "#2A508C"
BACKGROUND_COLOR_2 = "#1C3E73"
BACKGROUND_COLOR_3 = "#0D2750"

# Defining all the images used for the Application
POLICE_LOGO_PNG_PATH = resourcePath("..\\Assets\\Images\\greek_police_logo.png")
ADD_PNG_PATH = resourcePath("..\\Assets\\Images\\add.png")
CHANGE_PNG_PATH = resourcePath("..\\Assets\\Images\\change.png")
SEARCH_PNG_PATH = resourcePath("..\\Assets\\Images\\search.png")
INSERT_PNG_PATH = resourcePath("..\\Assets\\Images\\insert.png")
UPDATE_PNG_PATH = resourcePath("..\\Assets\\Images\\update.png")

# Defining the App Data path
APP_DATA_PATH = resourcePath('..\\Data\\appData.json')

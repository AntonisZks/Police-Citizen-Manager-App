import tkinter as tk
import sys
import os


""" https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file """
def resourcePath(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

""" The reisizeImage function resizes an image to a given size """
def resizeImage(img, desired_size):
    width_factor = img.width() // desired_size
    height_factor = img.height() // desired_size

    resized_img = img.subsample(width_factor, height_factor)
    return resized_img

""" The textSpaced function returns the given string but with spaces """
def textSpaced(text, times=1):
    new_text = text[0]
    for i in range(1, len(text)):
        new_text += " "*times
        new_text += text[i]
    return new_text

""" the getFileName function returns the name of the file path """
def getFileName(file_path):
    if file_path[len(file_path)-1] == 's': return os.path.basename(file_path)[:-4]
    else: return os.path.basename(file_path)[:-5]

""" The onMousewheel function controls the behavious of the mouse wheel scrolling """
def onMousewheel(event: any, canvas: tk.Canvas) -> None:
    # Get the current scroll position (as a fraction) relative to the maximum scroll
    current_scroll_frac = canvas.yview()[0]

    if event.delta > 0:  # Scrolling upwards
        if current_scroll_frac <= 0.0: return  # Don't scroll further up if already at the top
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    else:  # Scrolling downwards
        if current_scroll_frac >= 1.0: return  # Don't scroll further down if already at the bottom
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

""" Defining all the colors used for the Application """
BACKGROUND_COLOR_1 = "#2A508C"
BACKGROUND_COLOR_2 = "#1C3E73"
BACKGROUND_COLOR_3 = "#0D2750"

""" Defining all the images used for the Application """
POLICE_LOGO_PNG_PATH = resourcePath("..\\Assets\\Images\\greek_police_logo.png")
ADD_PNG_PATH = resourcePath("..\\Assets\\Images\\add.png")

""" Defining the App Data path """
APP_DATA_PATH = resourcePath('..\\Data\\appData.json')

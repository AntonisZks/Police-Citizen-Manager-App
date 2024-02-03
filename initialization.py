import sys
import os

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

POLICE_LOGO_IMAGE_PATH_ = resource_path("Imgs\\greek_police.png")
ADD_LOGO_IMAGE_PATH_ = resource_path("Imgs\\add.png")
DELETE_LOGO_IMAGE_PATH_ = resource_path("Imgs\\delete.png")
SAVE_LOGO_IMAGE_PATH_ = resource_path("Imgs\\save.png")
CHANGE_LOGO_IMAGE_PATH_ = resource_path("Imgs\\change.png")
SEARCH_LOGO_IMAGE_PATH_ = resource_path("Imgs\\search.png")
INSERT_LOGO_IMAGE_PATH_ = resource_path("Imgs\\insert.png")
UPDATED_LOGO_IMAGE_PATH_ = resource_path("Imgs\\update.png")
HIDE_LOGO_IMAGE_PATH_ = resource_path("Imgs\\hide_password.png")
VIEW_LOGO_IMAGE_PATH_ = resource_path("Imgs\\view_password.png")
BACK_LOGO_IMAGE_PATH_ = resource_path("Imgs\\back.png")

ACTIVE_FILE_PATH_ = resource_path("Files\\active_file.txt")
FILES_PATH_ = resource_path("Files\\files.txt")
PASSWORD_PATH_ = resource_path("Password\\password.txt")

APPLICATION_DESCRIPTION_INFO_PATH_ = resource_path("Info_about_app\\app_info.txt")
APPLICATION_LICENCE_INFO_PATH_ = resource_path("License\\license.txt")


def getWindowGeometryData(window):
    # Getting the screen width and height data
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Initializing the window width and height
    window_height = int((9/10)*screen_height)
    window_width =  int((8/10)*window_height)

    # Initializing the window spawn x and y coordinates
    window_spawn_x = int((screen_width - window_width)//2)
    window_spawn_y = int((screen_height - window_height)//2)-40 

    # Initializing the font size of the window
    font_size = int((1/35)*window_width)

    # Making the window geometry data dictionary
    window_geometry_data = {
        "width": window_width,
        "height": window_height,
        "spawn_x": window_spawn_x,
        "spawn_y": window_spawn_y,
        "font_size": font_size
    }
    return window_geometry_data

def get_file_name(file_path):
    return os.path.basename(file_path)[:-4]

def get_active_database():
    with open(ACTIVE_FILE_PATH_, "r", encoding="utf-8") as file:
        database = file.readline()
    return database[:-1]

def resizeImage(img, desired_size):
    width_factor = img.width() // desired_size
    height_factor = img.height() // desired_size

    resized_img = img.subsample(width_factor, height_factor)
    return resized_img
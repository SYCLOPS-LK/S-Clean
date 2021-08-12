# Import Modules
from tkinter import *
from classes import ColorPrint
from time import strftime, sleep
import os, shutil, asyncio, subprocess, getenv
from threading import Thread

# Constants
NAME = "S Clean"
WIDTH = 250
HEIGHT = 400
BACKGROUND = "#1A2128"
FOREGROUND = "#FFFFFF"
TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"
RED = "red"
BLUE = "blue"
GREEN = "green"
YELLOW = "yellow"

# Defining Variables Outside The Mainloop
prefetch_folder_path = ('C:\\Windows\\Prefetch')
local_temp_folder_path = (os.getenv('LOCALAPPDATA') + '\\Temp')
windows_folder_path = ('C:\\Windows\\temp')

# Defining Functions
def mouse_wheel_click_event(event):
    ColorPrint.print_info(f"X : {event.x}")
    ColorPrint.print_info(f"Y : {event.y}")

def cleaning_proccess():
    optimize_button.config(state = DISABLED)
    if os.path.isdir(prefetch_folder_path):
        optimize_status_label.config(text = "Prefetch Folder Found", fg = BLUE)
        sleep(1)
        for filename in os.listdir(prefetch_folder_path):
            file_path = os.path.join(prefetch_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue
        optimize_status_label.config(text = "Prefetch Folder Cleaned", fg = GREEN)
        sleep(1)
    else:
        optimize_status_label.config(text = "Prefetch Folder Not Found", fg = RED)
        sleep(1)

    if os.path.isdir(local_temp_folder_path):
        optimize_status_label.config(text = "Local Temp Folder Found", fg = BLUE)
        sleep(1)
        for filename in os.listdir(local_temp_folder_path):
            file_path = os.path.join(local_temp_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue
        optimize_status_label.config(text = "Local Temp Folder Cleaned", fg = GREEN)
        sleep(1)
    else:
        optimize_status_label.config(text = "Local Temp Folder Not Found", fg = RED)
        sleep(1)

    if os.path.isdir(windows_folder_path):
        optimize_status_label.config(text = "Windows Temp Folder Found", fg = BLUE)
        sleep(1)
        for filename in os.listdir(windows_folder_path):
            file_path = os.path.join(windows_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                continue
        optimize_status_label.config(text = "Windows Temp Folder Cleaned", fg = GREEN)
        sleep(1)
    else:
        optimize_status_label.config(text = "Windows Temp Folder Not Found", fg = RED)
        sleep(1)

    try:
        subprocess.check_output('bcdedit /set disabledynamictick yes', shell=True)
        subprocess.check_output('bcdedit /set useplatformtick yes', shell=True)
        subprocess.check_output('Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d "0" /f', shell=True)
        optimize_status_label.config(text = "System Latency Lowered", fg = GREEN)
        sleep(1)
    except Exception as e:
        optimize_status_label.config(text = "Failed to Lower System Latency", fg = RED)
        sleep(1)

    try:
        subprocess.check_output('ipconfig /flushdns', shell=True)
        optimize_status_label.config(text = "DNS Flushed", fg = GREEN)
        sleep(1)
    except Exception as e:
        optimize_status_label.config(text = "Failed to Flush DNS", fg = RED)
        sleep(1)

    
    optimize_button.config(state = NORMAL)
    optimize_status_label.config(text = "Waiting For Action", fg = YELLOW)

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text = current_time)
    time_label.after(1000, update_time)

def optimize_button_click():
    cleaning_proccess_task = Thread(target = cleaning_proccess)
    cleaning_proccess_task.start()

main_window = Tk() # Definging Main Window
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.title(NAME)
main_window.iconphoto(True, PhotoImage(file = "assets\\images\\icon.png"))
main_window.config(bg = BACKGROUND)
main_window.resizable(0, 0)

# Defining Variables inside The Mainloop

# Defining Events
main_window.bind("<Button-2>", mouse_wheel_click_event)

# Defining Widgets
logo_photo_image = PhotoImage(
    file = "assets\\images\\logo.png"
)

clean_label_photo_image = PhotoImage(
    file = "assets\\images\\boost.png"
)

logo_label = Label(
    main_window,
    image = logo_photo_image,
    bg = BACKGROUND
)

name_label = Label(
    main_window,
    text = NAME,
    fg = FOREGROUND,
    bg = BACKGROUND,
    font = (
        "Aquire",
        30
    ),
)

author_label = Label(
    main_window,
    text = "by syclopS",
    font = (
        None,
        10
    ),
    fg = FOREGROUND,
    bg = BACKGROUND
)

optimize_button = Button(
    main_window,
    text = "OPTIMIZE",
    fg = FOREGROUND,
    bg = BACKGROUND,
    activeforeground = FOREGROUND,
    activebackground = BACKGROUND,
    font = (
        None,
        20,
        "bold"
    ),
    relief = "ridge",
    image = clean_label_photo_image,
    compound = TOP,
    command = optimize_button_click
)

optimize_status_label = Label(
    main_window,
    fg = YELLOW,
    bg = BACKGROUND,
    text = "Waiting For Action"
)

time_label = Label(
    main_window,
    width = int(WIDTH/10),
    fg = FOREGROUND,
    bg = BACKGROUND,
    font = (
        None,
        7
    )
)

# Rendering Widgets
logo_label.pack(pady = 15)
ColorPrint.print_pass("logo_label Rendered")
name_label.pack()
ColorPrint.print_pass("name_label Rendered")
author_label.pack()
ColorPrint.print_pass("author_label Rendered")
optimize_button.pack(pady = 20)
ColorPrint.print_pass("optimize_button Rendered")
optimize_status_label.pack()
ColorPrint.print_pass("optimize_status_label Rendered")
time_label.place(x = 150, y = 381)
ColorPrint.print_pass("time_label Rendered")

update_time()

if __name__ == "__main__": # Executing Main file
    ColorPrint.print_pass("App Started")
    main_window.mainloop()
    ColorPrint.print_pass("App Stopped")
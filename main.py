# Import Modules
from tkinter                import *
from tkinter                import messagebox
from time                   import strftime, sleep
from threading              import Thread
from PIL                    import Image
import os
import ctypes
import shutil
import asyncio
import subprocess
import getenv
import asyncio

# Constants
NAME = "S CLEAN"
VERSION = "1.2.1"
WIDTH = 250
HEIGHT = 420
BACKGROUND = "#1A2128"
FOREGROUND = "#FFFFFF"
TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"
RED = "red"
BLUE = "blue"
GREEN = "green"
PURPLE = "#5865F2"
CYAN = "cyan"
ORANGE = "#E73E24"
BOLD = "bold"

# Defining Variables Outside The Mainloop
prefetch_folder_path = ('C:\\Windows\\Prefetch')
local_temp_folder_path = (os.getenv('LOCALAPPDATA') + '\\Temp')
windows_temp_folder_path = ('C:\\Windows\\temp')
softwaredistribution_folder_path = ("C:\\Windows\\SoftwareDistribution\\Download")

# Defining Functions
def cleaning_proccess():
    # Checking Admin privileges
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if is_admin == True:
        optimize_button.config(state = DISABLED, text = "OPTIMIZING")

        # Clean Prefetch Folder
        if os.path.isdir(prefetch_folder_path):
            optimize_status_label.config(text = "Prefetch Folder Found", fg = PURPLE)
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
            optimize_status_label.config(text = "Prefetch Folder Cleaned", fg = PURPLE)
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{prefetch_folder_path} not found")

        # Clean Local Temp Folder
        if os.path.isdir(local_temp_folder_path):
            optimize_status_label.config(text = "Local Temp Folder Found", fg = PURPLE)
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
            optimize_status_label.config(text = "Local Temp Folder Cleaned", fg = PURPLE)
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{local_temp_folder_path} not found")

        # Clean Windows Temp Folder
        if os.path.isdir(windows_temp_folder_path):
            optimize_status_label.config(text = "Windows Temp Folder Found", fg = PURPLE)
            sleep(1)
            for filename in os.listdir(windows_temp_folder_path):
                file_path = os.path.join(windows_temp_folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except:
                    continue
            optimize_status_label.config(text = "Windows Temp Folder Cleaned", fg = PURPLE)
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{windows_temp_folder_path} not found")

        # Clean SoftwareDistribution Downloads

        if os.path.isdir(softwaredistribution_folder_path):
            optimize_status_label.config(text = "SoftwareDistribution Folder Found", fg = PURPLE)
            sleep(1)

            try:
                os.system('net stop "wuauserv"')
                optimize_status_label.config(text = "wuauserv Service Stopped", fg = PURPLE)
                sleep(1)
            except:
                messagebox.showwarning(title = "Warning", message = "Failed to stop wuauserv service")

            try:
                os.system('net stop "bits"')
                optimize_status_label.config(text = "bits Service Stopped", fg = PURPLE)
                sleep(1)
            except:
                messagebox.showwarning(title = "Warning", message = "Failed to stop bits service")

            for filename in os.listdir(softwaredistribution_folder_path):
                file_path = os.path.join(softwaredistribution_folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except:
                    continue
            optimize_status_label.config(text = "SoftwareDistribution Folder Cleaned", fg = PURPLE)
            sleep(1)

            try:
                os.system('net start "bits"')
                optimize_status_label.config(text = "bits Service Started", fg = PURPLE)
                sleep(1)
            except:
                messagebox.showwarning(title = "Warning", message = "Failed to start bits service")

        else:
            messagebox.showerror(title = "Error", message = f"{softwaredistribution_folder_path} not found")

        # Adjust System Latency
        try:
            subprocess.check_output('bcdedit /set disabledynamictick yes', shell=True)
            subprocess.check_output('bcdedit /set useplatformtick yes', shell=True)
            subprocess.check_output('Reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d "0" /f', shell=True)
            optimize_status_label.config(text = "System Latency Lowered", fg = PURPLE)
            sleep(1)
        except Exception as e:
            messagebox.showerror(title = "Error", message = "Failed to reduce system latency")

        # Flush DNS Resolver Cache
        try:
            subprocess.check_output('ipconfig /flushdns', shell=True)
            optimize_status_label.config(text = "DNS Flushed", fg = PURPLE)
            sleep(1)
        except Exception as e:
            messagebox.showerror(title = "Error", message = "Failed to flush DNS resolver cache")

        optimize_button.config(state = NORMAL, text = "OPTIMIZE")
        optimize_status_label.config(text = "Waiting For Action", fg = PURPLE)
        messagebox.showinfo(title = "Success", message = "Tasks completed successfully")
    else:
        messagebox.showwarning(title = "Warning", message = "Admin privilege required !")

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text = current_time)
    time_label.after(1000, update_time)

def optimize_button_click():
    cleaning_proccess_task = Thread(target = cleaning_proccess)
    cleaning_proccess_task.start()

def drag_window_start_event(event):
    root.start_x = event.x
    root.start_y = event.y

def drag_window_event(event):
    x = root.winfo_x() - root.start_x + event.x
    y = root.winfo_y() - root.start_y + event.y
    root.geometry(f"+{x}+{y}")

def return_key_event(event):
    optimize_button_click()

def stop_mainloop():
    if messagebox.askyesno(title = "S Clean", message = "Are you sure you want to quit ?"):
        root.destroy()
    else:
        pass

def escape_key_event(event):
    stop_mainloop()

root = Tk() # Definging Main Window
root.geometry(f"{WIDTH}x{HEIGHT}")
root.config(bg = BACKGROUND)
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file = "assets\\images\\icon.png"))
root.overrideredirect(True)

# Defining Variables inside The Mainloop

# Defining Widgets
logo_photo_image = PhotoImage(
    file = "assets\\images\\logo.png"
)

optimize_label_photo_image = PhotoImage(
    file = "assets\\images\\boost.png"
)

close_button_photo_image = PhotoImage(
    file = "assets\\images\\close.png"
)

title_bar_frame = Frame(
    root,
    bg = BACKGROUND,
    height = 20
)

logo_label = Label(
    root,
    image = logo_photo_image,
    bg = BACKGROUND
)

name_label = Label(
    root,
    text = NAME,
    fg = FOREGROUND,
    bg = BACKGROUND,
    font = (
        None,
        30,
        "bold"
    ),
)

author_label = Label(
    root,
    text = "by syclopS",
    font = (
        None,
        10,
        "bold"
    ),
    fg = FOREGROUND,
    bg = BACKGROUND
)

optimize_button = Button(
    root,
    text = "OPTIMIZE",
    fg = FOREGROUND,
    bg = BACKGROUND,
    bd = 0,
    activeforeground = FOREGROUND,
    activebackground = BACKGROUND,
    font = (
        None,
        20,
        "bold"
    ),
    relief = FLAT,
    image = optimize_label_photo_image,
    compound = TOP,
    command = optimize_button_click
)

optimize_status_label = Label(
    root,
    fg = PURPLE,
    bg = BACKGROUND,
    text = "Waiting For Action",
    font = (
        None,
        8,
        BOLD
    )
)

time_label = Label(
    root,
    width = int(WIDTH/10),
    fg = ORANGE,
    bg = BACKGROUND,
    font = (
        None,
        8
    )
)

date_label = Label(
    root,
    text = strftime("%d %b, %Y"),
    font = (
        None,
        8
    ),
    fg = ORANGE,
    bg = BACKGROUND
)

version_label = Label(
    root,
    text = VERSION,
    bg = BACKGROUND,
    fg = CYAN
)

close_button = Button(
    title_bar_frame,
    image = close_button_photo_image,
    command = stop_mainloop,
    bd = 0,
    bg = BACKGROUND,
    activebackground = BACKGROUND,
    width = 24,
    height = 24
)

# Rendering Widgets
title_bar_frame.pack(side = "top", fill = "both")
close_button.pack(side = "right")
logo_label.pack(pady = 15)
name_label.pack()
version_label.place(x = 182, y = 140)
author_label.pack()
optimize_button.pack(pady = 20)
optimize_status_label.pack()
time_label.place(x = 148, y = 403)
date_label.place(x = 1, y = 403)

# Defining Events
root.bind("<Return>", return_key_event)
root.bind("<Escape>", escape_key_event)
root.bind("<Button-1>", drag_window_start_event)
title_bar_frame.bind("<B1-Motion>", drag_window_event)

if __name__ == "__main__": # Executing Main file
    update_time()
    root.mainloop()
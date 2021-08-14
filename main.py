# Import Modules
import os
from os import getenv
from tkinter                        import *
from tkinter                        import messagebox
from time                           import strftime, sleep
from threading                      import Thread
from PIL                            import Image

from functions.admin_privilege      import check_admin_privilege
from functions.optimize             import OptimizeProcess

# Constants
NAME = "S CLEAN"
VERSION = "1.2.6"
WIDTH = 250
HEIGHT = 420
BACKGROUND = "#1A2128"
FOREGROUND = "#FFFFFF"
TOP = "top"
BOTTOM = "bottom"
LEFT = "left"
RIGHT = "right"
BOLD = "bold"
PURPLE = "#5865F2"
CYAN = "cyan"
ORANGE = "#E73E24"

# Defining Variables Outside The Mainloop
prefetch_folder_path = ('C:\\Windows\\Prefetch')
local_temp_folder_path = (getenv('LOCALAPPDATA') + '\\Temp')
windows_temp_folder_path = ('C:\\Windows\\temp')
softwaredistribution_folder_path = ("C:\\Windows\\SoftwareDistribution\\Download")

# Defining Functions
def cleaning_proccess():

    # Checking Admin privilege
    if check_admin_privilege() == True:
        optimize_status_label.config(text = f"Admin Privilege Granted".upper())
        sleep(1)
        optimize_button.config(state = DISABLED, text = "OPTIMIZING")

        # Clean Prefetch Folder
        if os.path.isdir(prefetch_folder_path):
            optimize_status_label.config(text = f"{prefetch_folder_path}\nFound".upper())
            sleep(1)
            OptimizeProcess.clean_prefetch_folder()
            optimize_status_label.config(text = f"{prefetch_folder_path}\nCleaned".upper())
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{prefetch_folder_path} not found")

        # Clean Local Temp Folder
        if os.path.isdir(local_temp_folder_path):
            optimize_status_label.config(text = f"{local_temp_folder_path}\nFound".upper())
            sleep(1)
            OptimizeProcess.clean_local_temp_folder()
            optimize_status_label.config(text = f"{local_temp_folder_path}\nCleaned".upper())
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{local_temp_folder_path} not found")

        # Clean Windows Temp Folder
        if os.path.isdir(windows_temp_folder_path):
            optimize_status_label.config(text = f"{windows_temp_folder_path}\nFound".upper())
            sleep(1)
            OptimizeProcess.clean_windows_temp_folder()
            optimize_status_label.config(text = f"{windows_temp_folder_path}\nCleaned".upper())
            sleep(1)
        else:
            messagebox.showerror(title = "Error", message = f"{windows_temp_folder_path} not found")

        # Clean SoftwareDistribution Downloads
        if os.path.isdir(softwaredistribution_folder_path):
            optimize_status_label.config(text = f"{softwaredistribution_folder_path}\nFound".upper())
            sleep(1)

            OptimizeProcess.clean_softwaredistribution_folder()
            optimize_status_label.config(text = f"{softwaredistribution_folder_path}\nCleaned".upper())
            sleep(1)

        else:
            messagebox.showerror(title = "Error", message = f"{softwaredistribution_folder_path} not found")

        # Adjust System Latency
        try:
            OptimizeProcess.refuce_system_latency()
            optimize_status_label.config(text = "System Latency Lowered".upper())
            sleep(1)
        except Exception as e:
            messagebox.showerror(title = "Error", message = "Failed to reduce system latency")

        # Flush DNS Resolver Cache
        try:
            OptimizeProcess.flush_dns()
            optimize_status_label.config(text = "DNS Flushed".upper())
            sleep(1)
        except Exception as e:
            messagebox.showerror(title = "Error", message = "Failed to flush DNS resolver cache")

        optimize_button.config(state = NORMAL, text = "OPTIMIZE")
        optimize_status_label.config(text = "Waiting For Action".upper())
        messagebox.showinfo(title = "Success", message = "Tasks completed successfully")

    else:
        messagebox.showwarning(title = "Warning", message = "Admin privilege required !")

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text = current_time)
    time_label.after(1000, update_time)

def optimize_button_click_event(event):
    cleaning_proccess_task = Thread(target = cleaning_proccess)
    cleaning_proccess_task.start()

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

def stop_mainloop():
    if messagebox.askyesno(title = NAME, message = "Are you sure you want to quit ?"):
        root.destroy()
    else:
        pass

def escape_key_event(event):
    stop_mainloop()

global root
root = Tk() # Definging Main Window
root.config(bg = BACKGROUND)
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file = "YOUR ICON PATH"))
root.overrideredirect(True)

# Defining Variables inside The Mainloop
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (WIDTH/2))
y_cordinate = int((screen_height/2) - (HEIGHT/2))

root.geometry(f"{WIDTH}x{HEIGHT}+{x_cordinate}+{y_cordinate}")

# Defining Widgets
logo_photo_image = PhotoImage(
    file = "YOUR LOGO PATH"
)

optimize_label_photo_image = PhotoImage(
    file = "BOOST IMAGE PATH"
)

close_button_photo_image = PhotoImage(
    file = "CLOSE IMAGE PATH"
)

minimize_button_photo_image = PhotoImage(
    file = "MINIMIZE IMAGE PATH"
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
        BOLD
    ),
)

author_label = Label(
    root,
    text = "by syclopS",
    font = (
        None,
        10,
        BOLD
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
        BOLD
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
    text = "WAITING FOR ACTION",
    font = (
        None,
        7,
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
title_bar_frame.pack(side = TOP, fill = "both")
close_button.pack(side = RIGHT)
logo_label.pack(pady = 15)
name_label.pack()
version_label.place(x = 182, y = 140)
author_label.pack()
optimize_button.pack(pady = 20)
optimize_status_label.pack()
time_label.place(x = 148, y = 403)
date_label.place(x = 1, y = 403)

# Defining Events
root.bind("<Return>", optimize_button_click_event)
root.bind("<Escape>", escape_key_event)
root.bind("<Button-1>", drag_window_start_event)
title_bar_frame.bind("<B1-Motion>", drag_window_event)

if __name__ == "__main__": # Executing Main file
    update_time()
    root.mainloop()
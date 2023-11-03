import os
import shutil
import sys
import pyautogui
import shutil


boot_location = r'%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\mod.py' % os.environ['USERPROFILE']
print(boot_location)
temp_location = "./temp_folder/rooter.py"


class Main:
    def __init__(self):
        print("BEGINNING...")
        shutil.copy2('./rooter.py', temp_location)
        



new = Main()
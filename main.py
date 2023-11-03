import subprocess
import threading
import sys
import requests
import platform
import socket
import os
from modules.utensils import log 
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logger = log()



# Explanatory
# Every Class is constantly active from launch in a separate thread, Each thread is then tasked with actions from the primary class (Operator)


class Operator:
    def __init__(self):
        logger.console("Starting Operator...",2)
        self.active = False
        logger.console("Operator Active",1)
        self.active = True
        return


    def safeguard(self, state=True):
        if self.active == True:
            if state:
                logger.console("Activating the safeguard system thread",2)
                try:
                    self.event_handler = Monitor()
                    self.observer = Observer()
                    self.observer.schedule(self.event_handler, path="./", recursive=True)
                    self.observer.start()
                    logger.console("Activated the safeguard system thread",1)
                    return True
                except Exception as error:
                    logger.console(f"Error activating safeguard: {error}",3)
                    return False
            elif state == False:
                logger.console("Disabling the safeguard system thread",2)
                try:
                    self.observer.join()
                    self.observer.stop()
                    logger.console("Disabled the safeguard system thread",1)
                    return True
                except:
                    logger.console("Error disabling safeguard",3)
                    return False
            else:
                logger.console("Invalid safeguard state",3)
                return False

class Monitor(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

main = Operator()
main.safeguard()


class Acquirer:
    def __init__(self):
        # This class acquires everything required to perform a succesful smash and grab of all data.
        # Ultimately this class serves as the perfect template for a data heist of the device.
        self.jobs = []


def get_device_info():
    try:
        device_info = {}
        try:
            device_info['Hostname'] = socket.gethostname()
        except:
            pass
        try:
            device_info['IP Address'] = socket.gethostbyname(socket.gethostname())
        except:
            pass
        try:
            device_info['OS'] = platform.system()
        except:
            pass
        try:
            device_info['OS Version'] = platform.version()
        except:
            pass
        try:
            device_info['OS Release'] = platform.release()
        except:
            pass
        try:
            device_info['Architecture'] = platform.architecture()
        except:
            pass
        
        return device_info

    except Exception as error:
        return error


info = get_device_info()

print(info)

cmd_command = "DIR"

try:
    # Run the command and capture the output
    output = subprocess.check_output(cmd_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    
    # Print the output
    print("Command Output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")


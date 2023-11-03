import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directory to monitor
directory_to_monitor = "./"

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_monitor, recursive=True)
    observer.start()

    #try:
    #    while True:
    #        time.sleep(1)
    #except KeyboardInterrupt:
    #    observer.stop()

    observer.join()

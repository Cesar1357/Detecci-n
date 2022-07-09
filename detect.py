import sys
import os
import shutil
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/TOSHIBA/Downloads"
to_dir = "C:/Users/TOSHIBA/Downloads/downloadedFiles"

dir_tree = {
    "Files": ['.zip'],
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg', '.apk']
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("Se ha creado {event.src_path}")
    def on_deleted(self,event):
        print("Oye alguien borro {event.src_path}")
    def on_modify(self,event):
        print("Alguien a modificado {event.src_path}")
    def on_move(self,event):
        print("Alguien a movido {event.src_path}")

event = FileMovementHandler()
observer = Observer()
observer.schedule(event,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt:
    print("Detenido")
    observer.stop()

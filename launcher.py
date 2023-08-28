import os
from os import rename
from os.path import basename
import shutil
from pathlib import Path
from os import getlogin
import glob
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return



# Functions:
def create_dir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def change_file_ext(folder_destination, file_extensions):
    for filename in glob.iglob(os.path.join(folder_destination, '*')):
        os.rename(filename, filename + file_extensions)

def move_files_to_folder(source_dir, target_dir):
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)



# Main:

if __name__ == "__main__":
    images_path = "./Discord_Cache_Images"
    users_pc: str = getlogin()
    cache_folder_path = f'C:/Users/{users_pc}/AppData/Roaming/Discord/Cache/Cache_Data/'

    run_as_admin()
    print("Creating folder to store your images cache...")
    create_dir(images_path)
    print(f"Changing files extension in {cache_folder_path}")
    change_file_ext(cache_folder_path,'.png')
    print(f"Moving files in {cache_folder_path} to a new destination {images_path}")
    move_files_to_folder(cache_folder_path, images_path)
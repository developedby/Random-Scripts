"""Recursively removes ',v' from the ending of all files in a directory.
Used to correct the bbgames files.
"""

import os
from pathlib import Path


print('Script to remove ",v" from the end of all files in a directory recursively')

base_folder = Path(input('Please insert the path to folder where the files are: '))

def rename_files_in_folder(base_folder):
    folder_stack = [base_folder]
    while folder_stack:
        folder = folder_stack.pop()
        files = os.scandir(folder)
        for entry in files:
            if entry.is_dir():
                folder_stack.append(Path(entry.path))
            elif entry.is_file() and entry.name[-2:] == ',v':
                os.rename(folder/entry.name, folder/entry.name[:-2])

rename_files_in_folder(base_folder)
print("Files succesfully renamed")
#!/usr/bin/python3

import argparse
import os
import pathlib
import shlex
import subprocess
import sys
from typing import List

from click.types import StringParamType

parser = argparse.ArgumentParser(
    description="Convert files in a directory from one format to another using ffmpeg")
parser.add_argument("dir_path", help="Path to the directory with the files to be converted")
parser.add_argument("in_ext", help="Extension of the files to be converted")
parser.add_argument("out_ext", help="Extension the files will be converted to")
parser.add_argument("--options", help="Extra ffmpeg options")
parser.add_argument("--remove-old", help="Remove the old files", action="store_true", dest="remove_old")
parser.add_argument("-r", "--recursive", help="Search directories recursively", action="store_true", dest="recursive")

args = parser.parse_args()
if not args.in_ext.startswith('.'):
    args.in_ext = '.'+args.in_ext 
if not args.out_ext.startswith('.'):
    args.out_ext = '.'+args.out_ext 

dir_path = pathlib.Path(args.dir_path)

print(
    f"This will convert all \"{args.in_ext}\" files "
    f"to \"{args.out_ext}\" "
    f'in directory "{str(dir_path.absolute())}"'
    f"{ f', recursively' if args.recursive else '' }"
    f"{ f', with options [{args.options}]' if args.options is not None else '' }"
    f"{ f', deleting the old files' if args.remove_old else '' }"
)
answer = input("Continue [y/N]? ")

def convert_dir(dir_path: pathlib.Path):
    global args
    with os.scandir(dir_path) as it:
        to_delete: List[os.DirEntry] = []
        for entry in it:
            name, ext = os.path.splitext(entry.name)
            # If it's a file to convert
            if not entry.name.startswith('.') and entry.is_file() and ext == args.in_ext:
                new_name = name+ args.out_ext
                sp_args = ['ffmpeg', '-i', entry.path, str(dir_path/new_name)]
                if args.options is not None:
                    sp_args.extend(shlex.split(args.options))
                try:
                    subprocess.run(sp_args, check=True)
                except subprocess.CalledProcessError:
                    print(f"Error: Failed to convert {entry.path} to {new_name}. Cancelling")
                    sys.exit()
                else:
                    if args.remove_old:
                        to_delete.append(entry)
            # If it's a folder and we're searching recursively
            elif entry.is_dir() and args.recursive:
                convert_dir(pathlib.Path(entry.path))
        for entry in to_delete:
            os.remove(entry.path)

if answer.lower() in ['y', 'yes']:
    convert_dir(dir_path)
    print("\nSuccessfully converted all files")
else:
    print("\nCancelled")

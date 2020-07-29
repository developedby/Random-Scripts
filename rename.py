"""Script to rename Bandcamp songs downloaded through youtube-dl"""
import os
from pathlib import Path

COLUMN_SPACE = 50

print('Script to rename Bandcamp songs downloaded through youtube-dl')

path = Path(input('Please insert the path to folder where the songs are: '))
os.chdir(path)
old_names = os.listdir('.')

print('\nFound the following files:')
print(old_names)

keep_author = input('\nKeep Author name at the start of the file (y/N)? ')
keep_author = keep_author == 'y'

new_names = []
for name in old_names:
    song_name = '-'.join(name.split('-')[1:-2]).strip()
    author_name = name.split('-')[0].strip()
    extension = name.split('.')[-1].strip()
    if keep_author:
        new_names.append(f'{author_name} - {song_name}.{extension}')
    else:
        new_names.append(f'{song_name}.{extension}')

print(f"{'Old name':50} {'New name'}")
for name_pair in zip(old_names, new_names):
    print(f'{name_pair[0]:50} {name_pair[1]}')

confirm = input('\nAre you sure you want to rename these files (y/N)? ')
if confirm == 'y':
    for name_pair in zip(old_names, new_names):
        os.rename(name_pair[0], name_pair[1])
    print("Successfully renamed the files")
else:
    print("Cancelled")

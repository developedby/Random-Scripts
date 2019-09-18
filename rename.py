import os
files = os.listdir('.')
print(files)
confirm = input('Vai renomear, tem certeza?\ny para continuar: ')
if confirm == 'y':
  for file in files:
    name = file.split('-')[0]
    extension = file.split('.')[-1]
    os.rename(file, name + '.' + extension)

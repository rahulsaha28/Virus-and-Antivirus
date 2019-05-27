import os

directory = os.getcwd()

virus = ".ferosas"

for dirpath, dirname, filenames in os.walk(directory):
    for file in filenames:
        if virus in file:
            name = file.split(virus)
            os.rename(file, name[0])
            print(name[0])

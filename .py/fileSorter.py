import os
import shutil

files = [file for file in os.listdir() if os.path.isfile(file)]

for file in files:
    filename, extension = os.path.splitext(file)
    if not os.path.exists(extension):
        os.makedirs(extension)
    shutil.move(file, extension)
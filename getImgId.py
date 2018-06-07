import os
import cv2

file_dir = 'Annotations0/'
num=500
for root, dirs, files in os.walk(file_dir):
    for file in files:
        [filename, extension]=os.path.splitext(file)
        file_full_name = filename + extension
        newname='0'+file_full_name
        os.rename(file_dir+file_full_name, file_dir+newname)

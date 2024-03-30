# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os
 
# This is to get the directory that the program
# is currently running in.
dir_path = "C:\\Users\\cats\\Documents"
 
for root, dirs, files in os.walk(dir_path):
    for file in files:
 
        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith('.mp3'):
            print (root+'/'+str(file))

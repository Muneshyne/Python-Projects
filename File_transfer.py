

import shutil
import os

#set where the source of the files are
source = '/Users/8 7/Desktop/Python-Projects/FolderA/'

#set the destination path to folderb
destination = '/Users/8 7/Desktop/Python-Projects/FolderB/'
files = os.listdir(source)

for i in files:
            #saying move the files represented by 'i' to their new destination
            shutil.move(source+i, destination)

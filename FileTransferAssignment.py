
# Importing modules
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
	

# CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
	link_Label = Label(root, text ="Select The File To Transfer : ", bg = "#E8D579")
	link_Label.grid(row = 1, column = 0, pady = 5, padx = 5)
	
	root.sourceText = Entry(root, width = 50, textvariable = sourceLocation)
	root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2)
	
	source_browseButton = Button(root, text ="Browse", command = SourceBrowse, width = 15)
	source_browseButton.grid(row = 1, column = 3, pady = 5, padx = 5)
	
	destinationLabel = Label(root, text ="Select The Destination : ", bg ="#E8D579")
	destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
	
	root.destinationText = Entry(root, width = 50, textvariable = destinationLocation)
	root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5, columnspan = 2)
	
	dest_browseButton = Button(root, text ="Browse",command = DestinationBrowse, width = 15)
	dest_browseButton.grid(row = 2, column = 3, pady = 5, padx = 5)
	
	moveButton = Button(root, text ="Move File", command = MoveFile, width = 15)
	moveButton.grid(row = 3, column = 2, pady = 5, padx = 5)

def SourceBrowse():
	root.files_list = list(filedialog.askopenfilenames(initialdir ="/Users/8 7/Desktop/Python-Projects/FolderA/"))
	# displaying the selected files in the root.sourceText
	# Entry using root.sourceText.insert()
	root.sourceText.insert('1', root.files_list)
	
def DestinationBrowse():
	destinationdirectory = filedialog.askdirectory(initialdir ="/Users/8 7/Desktop/Python-Projects/FolderA/")
	root.destinationText.insert('1', destinationdirectory)
	
	
def MoveFile():
	files_list = root.files_list
	destination_location = destinationLocation.get()
	# Looping through the files present in the list
	for f in files_list:
		# Moving the file to the destination using the move() of shutil module 
		shutil.move(f, destination_location)
	messagebox.showinfo("SUCCESSFUL")
# creating object of tk class
root = tk.Tk()
	
# disabling the resizing so its not to large or to small
root.geometry("830x120")
root.title("File_Transfer GUI")
root.config(background = "black")
	
sourceLocation = StringVar()
destinationLocation = StringVar()
CreateWidgets()
#infinite loop to keep open
root.mainloop()

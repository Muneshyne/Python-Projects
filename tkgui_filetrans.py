
import shutil
import os
import tkinter as tk
from tkinter import *

win = Tk()
frm = Frame(win)
btn1 = Button(frm, text='Submit')
btn2 = Button(frm, text='Cancel')
btn3 = Button(frm, text='Browse')
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
btn3.pack(side = LEFT)
lbl = Label(win, text="Please choose a file path.")
lbl.pack()
frm.pack()



class ParentWindow(Frame):
      def __init__ (self, master): #self is the class, master is the frame
            Frame.__init__ (self)

            self.master = master
            self.master.resizable (width=False, height=False)
            self.master.geometry(' {}x{} '.format(600, 400))
            self.master.title('File Transfer')
            self.master.config(bg='lightgray')

            varbtn = StringVar()
            






      """
      #set where the source of the files are
      source = '/Users/8 7/Desktop/Python-Projects/FolderA/'

      #set the destination path to folderb
      destination = '/Users/8 7/Desktop/Python-Projects/FolderB/'
      files = os.listdir(source)

      for i in files:
                  #saying move the files represented by 'i' to their new destination
                  shutil.move(source+i, destination)
      """




if __name__ == "__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()


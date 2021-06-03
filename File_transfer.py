

import shutil
import os
import tkinter as tk
from tkinter import *


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

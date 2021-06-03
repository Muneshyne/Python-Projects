

import os,time
import datetime
import shutil
from tkinter import *
import datetime as dt

def Submit(): 
      now = dt.datetime.now()
      ago = now-dt.timedelta(hours=24)
      strftime = "%H:%M %m/%d/%Y"
      created = '/Users/8 7/Desktop/Python-Projects/FolderB/'
      dest = '/Users/8 7/Desktop/Python-Projects/FolderA/'

for root, dirs,files in os.walk(created):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
            # this is actual move

window=Tk()
btn=Button(window, text="To confirm body click here", fg='blue', command=Submit) #calls submit function and opens page
btn.place(x=80, y=100)
lbl=Label(window, text="Please Enter Header", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Web Generator')
window.geometry("300x200+10+10") #window size 
window.mainloop()

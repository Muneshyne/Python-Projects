
import webbrowser
import os
from tkinter import *


def Submit():
    text = txtfld.get()
    html_template = """
    <html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>
    """.format(text)
    f = open("webgen.html", "w")
    #writing code into file
    f.write(html_template)
    f.close()

    filename = 'file:///'+os.getcwd()+'/' + 'webgen.html'
    webbrowser.open_new_tab(filename)
window=Tk()
btn=Button(window, text="To confirm body click here", fg='blue', command=Submit)
btn.place(x=80, y=100)
lbl=Label(window, text="Please Enter Header", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Web Generator')
window.geometry("300x200+10+10")
window.mainloop()

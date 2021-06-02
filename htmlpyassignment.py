
import webbrowser
import os
from tkinter import *

f = open("webgen.html", "w")

html_template = """
<html>

<body>

<h1>

Stay tuned for our amazing summer sale!

</h1>

</body>

</html>
"""
#writing code into file
f.write(html_template)
f.close()

filename = 'file:///'+os.getcwd()+'/' + 'webgen.html'
webbrowser.open_new_tab(filename)

window=Tk()
btn=Button(window, text="To confirm body click here", fg='blue')
btn.place(x=80, y=100)
txtfld=Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Web Generator')
window.geometry("300x200+10+10")
window.mainloop()

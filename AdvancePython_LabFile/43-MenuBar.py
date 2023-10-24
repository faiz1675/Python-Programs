#43
from tkinter import *

root=Tk()
root.geometry("600x600+50+50")
root.config(bg='yellow')
root.title("Menu Bar")
root.resizable(False,False)

menubar=Menu(root)
file=Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Open')
file.add_command(label='Save')
menubar.add_cascade(label='File',menu=file)

edit=Menu(menubar,tearoff=0)
edit.add_command(label='Update')
edit.add_command(label='Delete')
menubar.add_cascade(label='Edit',menu=edit)

about=Menu(menubar, tearoff=0)
about.add_command(label='About Us')
about.add_command(label='Help')
menubar.add_cascade(label='About',menu=about)

root.config(menu=menubar)
mainloop()
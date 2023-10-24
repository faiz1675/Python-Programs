#42

from tkinter import *

root=Tk()
root.geometry("600x600+100+100")
root.title("Gender")
root.resizable(False,False)

def show():
    if g.get()=='male':
        lbl.config(text='Male')
    elif g.get()=='female':
        lbl.config(text='Female')
    elif g.get()=='transgender':
        lbl.config(text='Transgender')

lbl=Label(root, text='Female',font=('Arial',15),bg='yellow')
lbl.place(x=30,y=40)

g=StringVar()
g.set(' ')
rd1=Radiobutton(root, text='Male', value='male', variable=g, command=show)
rd1.place(x=30,y=60)

rd2=Radiobutton(root, text='Female', value='female', variable=g,command=show)
rd2.place(x=30,y=90)

rd3=Radiobutton(root, text='Transgender', value='transgender', variable=g,command=show)
rd3.place(x=30,y=120)

mainloop()
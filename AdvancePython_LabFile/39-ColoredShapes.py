#39-WAP to draw colored shapes(line, rectangle and oval) on canvas
from tkinter import *
root=Tk()

c=Canvas(root, bg='hotpink')
line=c.create_line(300,50,200,200,fill='red')
rec=c.create_rectangle(200,200,150,100, fill='black')
ov=c.create_oval(100,200,150,100)
c.pack()
mainloop()

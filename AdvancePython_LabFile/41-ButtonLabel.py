#41-WAP to create a button and a label inside the frame widget. Button should
#change the color upon hovering over the button and label should be 
#disappear on clicking the button

from tkinter import *
root=Tk()
root.geometry("500x500+150+150")
root.title("Frame Widget")
root.configure(bg='yellow')
root.resizable(False,False)

def disappear():
    lbl.destroy()


lbl=Label(root,text='Hello Faiz',font=('Times New Roman',20))
lbl.place(x=140,y=80,height=30,width=150)

btn=Button(root,text="Click Me",bg='red',activebackground='blue', font=('Times New Roman',20),command=disappear)
btn.bind('<Enter>',func=lambda e:btn.config(bg='pink'))
btn.bind('<Leave>',func=lambda e:btn.config(bg='orange'))
btn.place(x=150,y=130,height=30,width=120)
mainloop()
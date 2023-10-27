#40- Write a program to create a window which automatically disappears after 5 seconds.
from tkinter import *

def close_window():
    root.destroy()

root = Tk()
root.title("Auto Close Window")
root.geometry("500x500+200+200")
root.resizable(False,False)
root.configure(bg='green')
lbl=Label(root,text='Welcome to NIET',bg='red',font=('Arial',20))
lbl.place(x=100,y=100,height=50,width=300)

# Call the close_window function after 5 seconds (5000 milliseconds)
root.after(5000, close_window)

root.mainloop()

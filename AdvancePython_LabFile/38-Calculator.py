#38-WAP to create an Arithmetic Calculator using Tkinter
from tkinter import *
root =Tk()
root.geometry("430x320+80+100")
root.resizable(False,False)
root.configure(bg='yellow')
root.title("Calculator")

a=StringVar()
ent=Entry(root,font=('Arial',20,'bold'),justify='right',textvariable=a)
ent.place(x=10,y=0,height=45,width=400)

# function on any button-show()
def show(op):
    a.set(a.get()+op)

# function on equal button
def eql():
    exp=a.get()
    a.set(eval(exp))

#function on clear button
def clr():
    a.set(" ")

#Row-1
btn7=Button(root,text='7',font=('Arial',22))
btn7.place(x=15,y=55,height=45,width=90)
btn7.configure(command=lambda:show('7'))

btn8=Button(root,text='8',font=('Arial',22))
btn8.place(x=115,y=55,height=45,width=90)
btn8.configure(command=lambda:show('8'))

btn9=Button(root,text='9',font=('Arial',22))
btn9.place(x=215,y=55,height=45,width=90)
btn9.configure(command=lambda:show('9'))

btnPlus=Button(root,text='+',font=('Arial',22))
btnPlus.place(x=315,y=55,height=45,width=90)
btnPlus.configure(command=lambda:show('+'))

#Row-2
btn4=Button(root,text='4',font=('Arial',22))
btn4.place(x=15,y=115,height=45,width=90)
btn4.configure(command=lambda:show('4'))

btn5=Button(root,text='5',font=('Arial',22))
btn5.place(x=115,y=115,height=45,width=90)
btn5.configure(command=lambda:show('5'))

btn6=Button(root,text='6',font=('Arial',22))
btn6.place(x=215,y=115,height=45,width=90)
btn6.configure(command=lambda:show('6'))

btnMinus=Button(root,text='-',font=('Arial',22))
btnMinus.place(x=315,y=115,height=45,width=90)
btnMinus.configure(command=lambda:show('-'))

#Row-3
btn1=Button(root,text='1',font=('Arial',22))
btn1.place(x=15,y=175,height=45,width=90)
btn1.configure(command=lambda:show('1'))

btn2=Button(root,text='2',font=('Arial',22))
btn2.place(x=115,y=175,height=45,width=90)
btn2.configure(command=lambda:show('2'))

btn3=Button(root,text='3',font=('Arial',22))
btn3.place(x=215,y=175,height=45,width=90)
btn3.configure(command=lambda:show('3'))

btnMul=Button(root,text='*',font=('Arial',22))
btnMul.place(x=315,y=175,height=45,width=90)
btnMul.configure(command=lambda:show('*'))


#Row-4
btnClear=Button(root,text='C',font=('Arial',22))
btnClear.place(x=15,y=235,height=45,width=90)
btnClear.configure(command=clr)

btn0=Button(root,text='0',font=('Arial',22))
btn0.place(x=115,y=235,height=45,width=90)
btn0.configure(command=lambda:show('0'))

btnEqual=Button(root,text='=',font=('Arial',22))
btnEqual.place(x=215,y=235,height=45,width=90)
btnEqual.configure(command=eql)


btnDiv=Button(root,text='/',font=('Arial',22))
btnDiv.place(x=315,y=235,height=45,width=90)
btnDiv.configure(command=lambda:show('/'))

mainloop()
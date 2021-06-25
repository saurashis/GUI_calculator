from tkinter import *
root =Tk()


e=Entry(root,width=10,font=('Helvetica',35))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#for Number
def buttonpress(a):
    value=str(e.get())
    e.delete(0,END)
    a=str(a)
    global string #decleare string as global
    string=value+a
    e.insert(0,string) #display numbers pressed

def clear(): #to cleare the display
    e.delete(0,END)

def add():
    x=e.get()
    global first
    first=x
    e.delete(0, END)
    global math
    math="plus"

def sub():
    x=e.get()
    global first
    first=x
    e.delete(0, END)
    global math
    math = "minus"

def div():
    x=e.get()
    global first
    first=x
    e.delete(0, END)
    global math
    math = "div"

def mul():
    x=e.get()
    global first
    first=x
    e.delete(0, END)
    global math
    math = "mul"

def result():
    y=e.get()
    e.delete(0,END)
    if math=='plus':
        e.insert(0,(int(first)+int(y)))
    elif math=='minus':
        e.insert(0, (int(first) - int(y)))
    elif math=='div':
        e.insert(0, (int(first) / int(y)))
    elif math=='mul':
        e.insert(0, (int(first) * int(y)))

button1=Button(root,text='1',font=(12),padx=35,pady=10,command= lambda : buttonpress(1))
button2=Button(root,text='2',font=(12),padx=35,pady=10,command= lambda : buttonpress(2))
button3=Button(root,text='3',font=(12),padx=35,pady=10,command= lambda : buttonpress(3))
button4=Button(root,text='4',font=(12),padx=35,pady=10,command= lambda : buttonpress(4))
button5=Button(root,text='5',font=(12),padx=35,pady=10,command= lambda : buttonpress(5))
button6=Button(root,text='6',font=(12),padx=35,pady=10,command= lambda : buttonpress(6))
button7=Button(root,text='7',font=(12),padx=35,pady=10,command= lambda : buttonpress(7))
button8=Button(root,text='8',font=(12),padx=35,pady=10,command= lambda : buttonpress(8))
button9=Button(root,text='9',font=(12),padx=35,pady=10,command= lambda : buttonpress(9))
button0=Button(root,text='0',font=(12),padx=35,pady=10,command= lambda : buttonpress(0))

buttonplus=Button(root,text='+',font=(12),padx=35,pady=10,command=add)
buttonsub=Button(root,text='-',font=(12),padx=35,pady=10,command=sub)
buttondiv=Button(root,text='/',font=(12),padx=38,pady=10,command=div)
buttonmul=Button(root,text='*',font=(12),padx=35,pady=10,command=mul)

buttonclr=Button(root,text='clear',font=(9),padx=20,pady=42,command=clear)
buttoneql=Button(root,text='=',font=(10),padx=85,pady=14,command=result)

buttonclr.grid(row=5,column=0,rowspan=2)
buttoneql.grid(row=6,column=1,columnspan=2)

button0.grid(row=4,column=0)
buttonplus.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttondiv.grid(row=5,column=1)
buttonmul.grid(row=5,column=2)

button7.grid(row=3 , column=0)
button8.grid(row=3, column=1)
button9.grid(row=3 , column=2)

button4.grid(row=2 , column=0)
button5.grid(row=2, column=1)
button6.grid(row=2 , column=2)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

root.mainloop()

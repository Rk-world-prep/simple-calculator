#GUI based simple calculated.
from tkinter import *
win=Tk()
win.geometry("500x350")
win.title("simple calculator")
win.resizable(0,0)

def add():
 n1=eval(entn1.get())
 n2=eval(entn2.get())
 res=n1+n2
 lblres.config(text="result="+str(res))

def sub():
 n1=eval(entn1.get())
 n2=eval(entn2.get())
 res=n1-n2
 lblres.config(text="result="+str(res))

def mult():
 n1=eval(entn1.get())
 n2=eval(entn2.get())
 res=n1*n2
 lblres.config(text="result="+str(res))

def div():
 n1=eval(entn1.get())
 n2=eval(entn2.get())
 res=n1/n2
 lblres.config(text="result="+str(res))

lbln1=Label(win,text="Enter First No",font=("Arial 15 bold"),fg="blue")
lbln1.place(x=10,y=30)

entn1=Entry(win,font=("arial 15"),fg="white",bg="orange", bd=5)
entn1.place(x=200,y=30)

lbln2=Label(win,text="Enter Second No",font=("Arial 15 bold"),fg="blue")
lbln2.place(x=10,y=100)

entn2=Entry(win,font=("arial 15"),fg="white",bg="orange",bd=5)
entn2.place(x=200,y=100)

lblres=Label(win,text="result",fg="blue",font=("Arial 15 bold"))
lblres.place(x=10,y=170)

btnadd=Button(win,text="+",font=("Arial 15 bold"),fg="blue",bd=5,command=add)
btnadd.place(x=10,y=240)

btnsub=Button(win,text="-",font=("Arial 15 bold"),fg="blue",bd=5,command=sub)
btnsub.place(x=80,y=240)

btnmult=Button(win,text="*",font=("Arial 15 bold"),fg="blue",bd=5,command=mult)
btnmult.place(x=150,y=240)

btndiv=Button(win,text="/",font=("Arial 15 bold"),fg="blue",bd=5,command=div)
btndiv.place(x=220,y=240)


win.mainloop()

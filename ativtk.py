from Tkinter import *
from functools import partial

def btcolorgreen(bt):
	bt.configure(bg="green",fg="white")
        bt1["state"] = bt2["state"] = bt3["state"] = bt4["state"] = DISABLED
	btnext["state"] = ACTIVE
	lb1.configure(text="BO - NE - CA", fg="green")

def btcolorred(bt):
	bt.configure(bg="red",fg="white",state=DISABLED)

root = Tk()
root["bg"] = "white"

setaE = PhotoImage(file="setaE.jpg")
setaE = setaE.zoom(2)
setaE = setaE.subsample(35)
btprev = Button(root,state=DISABLED,image=setaE)
btprev.grid(row=0,column=0,sticky=W)

setaD = PhotoImage(file="setaD.jpg")
setaD = setaD.zoom(1)
setaD = setaD.subsample(63)
btnext = Button(root,state=DISABLED,image=setaD)
btnext.grid(row=0,column=1,sticky=E)

img = PhotoImage(file="boneca.jpg")
img = img.zoom(15)
img = img.subsample(32)
w = Label(root,image=img,bg="white")
w.image = img
w.grid(columnspan=2)

lb1 = Label(root,text="BO - NE - ??",font="Helvetica 18 bold",bg="white",height=2)
lb1.grid(columnspan=2)

bt1 = Button(root,text="CO",width=15,pady=10)
bt2 = Button(root,text="SI",width=15,pady=10)
bt3 = Button(root,text="CA",width=15,pady=10)
bt4 = Button(root,text="BI",width=15,pady=10)

bt1["command"] = partial(btcolorred, bt1)
bt2["command"] = partial(btcolorred, bt2)
bt3["command"] = partial(btcolorgreen, bt3)
bt4["command"] = partial(btcolorred, bt4)

bt1.grid(row=3,column=0,padx=1,pady=1)
bt2.grid(row=3,column=1,padx=1,pady=1)
bt3.grid(row=4,column=0,padx=1,pady=1)
bt4.grid(row=4,column=1,padx=1,pady=1)

root.mainloop()

#root.geometry("500x500+-500+200")

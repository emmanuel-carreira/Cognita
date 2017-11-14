from Tkinter import *
from functools import partial

def btcolorgreen(bt,lb,solution):
	bt.configure(bg="green")
        bt1["state"] = bt2["state"] = bt3["state"] = bt4["state"] = DISABLED
	btnext["state"] = ACTIVE
	lb.configure(text=solution, fg="green")

def btcolorred(bt):
	bt.configure(bg="red",state=DISABLED)

def btdefault():
	bt1["state"] = bt2["state"] = bt3["state"] = bt4["state"] = ACTIVE
	btnext["state"] = DISABLED
	bt1["bg"] = bt2["bg"] = bt3["bg"] = bt4["bg"] = btcolor

def principal(path,word1,a,b,c,d,word2):
	
	img = PhotoImage(file=path)
	img = img.zoom(15)
	img = img.subsample(32)
	w["image"] = img
	w.image = img
	
	lb1.configure(text=word1,fg="black")
	
	bt1["text"] = a
	bt2["text"] = b
	bt3["text"] = c
	bt4["text"] = d

	bt1["command"] = partial(btcolorred, bt1)
	bt2["command"] = partial(btcolorred, bt2)
	bt3["command"] = partial(btcolorgreen, bt3, lb1, word2)
	bt4["command"] = partial(btcolorred, bt4)

def next():
	btdefault()
	principal("boneca.jpg","BO - NE - ??","CO","SI","CA","BI","BO - NE - CA")	

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
btnext = Button(root,state=DISABLED,image=setaD,command=next)
btnext.grid(row=0,column=1,sticky=E)

img = PhotoImage(file="sapo.jpg")
img = img.zoom(15)
img = img.subsample(32)
w = Label(root,image=img,bg="white")
w.image = img
w.grid(columnspan=2)

lb1 = Label(root,text="?? - PO",font="Helvetica 18 bold",bg="white",height=2)
lb1.grid(columnspan=2)

bt1 = Button(root,text="CA",width=15,pady=10)
bt2 = Button(root,text="SU",width=15,pady=10)
bt3 = Button(root,text="LE",width=15,pady=10)
bt4 = Button(root,text="SA",width=15,pady=10)

btcolor=bt1["bg"]

bt1["command"] = partial(btcolorred, bt1)
bt2["command"] = partial(btcolorred, bt2)
bt3["command"] = partial(btcolorred, bt3)
bt4["command"] = partial(btcolorgreen, bt4,lb1,"SA - PO")

bt1.grid(row=3,column=0,padx=1,pady=1)
bt2.grid(row=3,column=1,padx=1,pady=1)
bt3.grid(row=4,column=0,padx=1,pady=1)
bt4.grid(row=4,column=1,padx=1,pady=1)

img2 = PhotoImage(file="boneca.jpg")
img2 = img2.zoom(15)
img2 = img2.subsample(32)

#root.geometry("500x500+-500+200")
root.mainloop()


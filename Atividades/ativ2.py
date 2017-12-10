from Tkinter import *
from functools import partial

def btcolorgreen(bt,lb,solution):
	bt.configure(bg="green")
	for i in range (0,4):
		four_bt[i]["state"] = DISABLED
	btnext["state"] = ACTIVE
	lb.configure(text=solution, fg="green")

def btcolorred(bt):
	bt.configure(bg="red",state=DISABLED)

def btdefault():
	for i in range (0,4):
		four_bt[i]["state"] = ACTIVE
		four_bt[i]["bg"] = btcolor
	btnext["state"] = DISABLED


def principal(path,word1,a,b,c,d,word2,e,f):
	
	img = PhotoImage(file=path)
	img = img.zoom(8)
	img = img.subsample(32)
	w["image"] = img
	w.image = img
	
	lb1.configure(text=word1,fg="black")

	btnext["command"] = partial(next,f+1)
	
	four_bt[0]["text"] = a
	four_bt[1]["text"] = b
	four_bt[2]["text"] = c
	four_bt[3]["text"] = d

	for i in range (0,4):
		if i==e:
			four_bt[i]["command"] = partial(btcolorgreen, four_bt[i], lb1, word2)
		else:
			four_bt[i]["command"] = partial(btcolorred, four_bt[i])
def finish():
	img = PhotoImage(file="fim.jpg")
	img = img.zoom(20)
	img = img.subsample(32)
	w["image"] = img
	w.image = img
	
	lb1.configure(text="Parabens",fg="black")

	for i in range (0,4):
		four_bt[i].destroy()

def next(aux):
	btdefault()
	if(aux == 2):	
		principal("sapo.jpg","SA - PO","1","3","5","2","SAPO",3,aux)
	if(aux == 3):
		principal("telefone.jpg","TE - LE - FO - NE","2","1","6","4","TELEFONE",3,aux)
	if(aux == 4):
		principal("sapato.jpg","SA - PA - TO","3","4","7","2","SAPATO",0,aux)
	if(aux == 5):
		finish()

root = Tk()
root["bg"] = "white"

setaE = PhotoImage(file="setaE.jpg")
setaE = setaE.zoom(2)
setaE = setaE.subsample(35)
btprev = Button(root,state=DISABLED,image=setaE)
btprev.image = setaE
btprev.grid(row=0,column=0,sticky=W)

setaD = PhotoImage(file="setaD.jpg")
setaD = setaD.zoom(1)
setaD = setaD.subsample(63)
btnext = Button(root,state=DISABLED,image=setaD,command=next)
btnext.image = setaD
btnext.grid(row=0,column=1,sticky=E)

w = Label(root,bg="white",height=120,width=480)
w.grid(columnspan=2)

lb1 = Label(root,font="Helvetica 18 bold",bg="white",height=1)
lb1.grid(columnspan=2)

four_bt = []
for i in range(0,4):
	four_bt.append(Button(root,width=26,pady=7))
	
btcolor=four_bt[0]["bg"]

four_bt[0].grid(row=3,column=0,padx=1,pady=1)
four_bt[1].grid(row=3,column=1,padx=1,pady=1)
four_bt[2].grid(row=4,column=0,padx=1,pady=1)
four_bt[3].grid(row=4,column=1,padx=1,pady=1)

principal("boneca.jpg","BO - NE - CA","4","5","3","8","BONECA",2,1)

root.geometry("480x320")

root.mainloop()


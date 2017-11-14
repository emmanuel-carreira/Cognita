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
	img = img.zoom(15)
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
		principal("sapo.jpg","?? - PO","BA","LE","JO","SA","SA - PO",3,aux)
	if(aux == 3):
		principal("telefone.jpg","TE - ?? - FO - NE","LE","GO","ZU","PE","TE - LE - FO - NE",0,aux)
	if(aux == 4):
		principal("sapato.jpg","SA - PA - ??","XI","TO","VU","DO","SA - PA - TO",1,aux)
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

w = Label(root,bg="white")
w.grid(columnspan=2)

lb1 = Label(root,font="Helvetica 18 bold",bg="white",height=2)
lb1.grid(columnspan=2)

four_bt = []
for i in range(0,4):
	four_bt.append(Button(root,width=15,pady=10))
	
btcolor=four_bt[0]["bg"]

four_bt[0].grid(row=3,column=0,padx=1,pady=1)
four_bt[1].grid(row=3,column=1,padx=1,pady=1)
four_bt[2].grid(row=4,column=0,padx=1,pady=1)
four_bt[3].grid(row=4,column=1,padx=1,pady=1)

principal("boneca.jpg","BO - NE - ??","CO","SI","CA","BI","BO - NE - CA",2,1)

#root.geometry("500x500+-500+200")
root.mainloop()


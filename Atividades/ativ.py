from Tkinter import *
from functools import partial
from time import clock
from PIL import Image

#--------------

root = Tk()
	
frameMaster = Frame(root)
frameMaster1 = Frame(root)
frameMaster2 = Frame(root)
	
#--------------

frameSetas = Frame(frameMaster,bg="white")

botaoSair = Button(frameSetas,text="Sair",state=DISABLED,command=root.destroy)

botaoNext = Button(frameSetas,state=DISABLED,command=next)

#------------------

frameImg = Frame(frameMaster,bg="white")

labelImg = Label(frameImg,bg="white",height=173,width=480)

labelString = Label(frameImg,font="Helvetica 18 bold",bg="white",height=1)

#------------------

frameBotao1 = Frame(frameMaster,bg="white")

frameBotao2 = Frame(frameMaster,bg="white")

botaoAlternativas = []
for i in range(0,4):
	if(i <= 1):
		botaoAlternativas.append(Button(frameBotao1,width=27,pady=7))
	else:
		botaoAlternativas.append(Button(frameBotao2,width=27,pady=7))
	
	btcolor = botaoAlternativas[0]["bg"]

#---------------

frameQuit = Frame(frameMaster,bg="white")

botaoQuit = Button(frameQuit,text="Sair",command=root.destroy)

frameWait = Frame(frameMaster,bg="white")

labelWait = Label(frameWait,font="Arial 25 bold",text="Esperando atividade",bg="white",fg="red",height=300)

#----------------

frameLogin1 = Frame(frameMaster,bg="white")
frameLogin2 = Frame(frameMaster,bg="white")

#---------------

def btcolorgreen(bt,lb,solution):
	bt.configure(bg="green")
	for i in range (0,4):
		botaoAlternativas[i]["state"] = DISABLED
	botaoNext["state"] = ACTIVE
	lb.configure(text=solution, fg="green")

def btcolorred(bt):
	bt.configure(bg="red",state=DISABLED)

def btdefault():
	for i in range (0,4):
		botaoAlternativas[i]["state"] = ACTIVE
		botaoAlternativas[i]["bg"] = btcolor

	botaoNext["state"] = DISABLED


def principal(path,word1,a,b,c,d,word2,e,f):
	
	img = PhotoImage(file=path)
	img = img.zoom(10)
	img = img.subsample(32)
	labelImg["image"] = img
	labelImg.image = img
	
	labelString.configure(text=word1,fg="black")

	botaoNext["command"] = partial(next,f+1)
	
	botaoAlternativas[0]["text"] = a
	botaoAlternativas[1]["text"] = b
	botaoAlternativas[2]["text"] = c
	botaoAlternativas[3]["text"] = d

	for i in range (0,4):
		if i==e:
			botaoAlternativas[i]["command"] = partial(btcolorgreen, botaoAlternativas[i], labelString, word2)
		else:
			botaoAlternativas[i]["command"] = partial(btcolorred, botaoAlternativas[i])

def finish():
	img = PhotoImage(file="professor.gif")
	img = img.zoom(6)
	img = img.subsample(32)
	labelImg["image"] = img
	labelImg.image = img
	
	labelString.configure(text="Muito bem!",fg="black",height=10)
	
	botaoSair["state"] = ACTIVE

	frameBotao1.destroy()
	frameBotao2.destroy()

	'''atual = clock()
	k = 0
	while(clock() - atual < 10):
		k = k + 1 #encher pneu de trem'''

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

def ativ():

	frameLogin1.destroy()
	frameLogin2.destroy()
	
	frameMaster.pack(fill=X)
	
	#--------------

	frameSetas.pack(fill=X)

	botaoSair.pack(side=LEFT,fill=Y)

	setaD = PhotoImage(file="setaD.jpg")
	setaD = setaD.zoom(1)
	setaD = setaD.subsample(63)
	botaoNext["image"] = setaD
	botaoNext.image = setaD
	botaoNext.pack(side=RIGHT)

	#------------------

	frameImg.pack(fill=X)

	labelImg.pack()

	labelString.pack()

	#------------------

	frameBotao1.pack(fill=X)

	frameBotao2.pack(fill=X)

	botaoAlternativas[0].pack(side=LEFT)
	botaoAlternativas[1].pack(side=RIGHT)
	botaoAlternativas[2].pack(side=LEFT)
	botaoAlternativas[3].pack(side=RIGHT)

	principal("boneca.jpg","BO - NE - ??","CO","SI","CA","BI","BO - NE - CA",2,1)

#------------------------------

botaoAluno1 = Button(frameLogin1,text="Maria",bg="white",height=150,width=212,command=ativ)
botaoAluno2 = Button(frameLogin1,text="Joaquim",bg="white",height=150,width=212,command=ativ)

botaoAluno3 = Button(frameLogin2,text="Carol",bg="white",height=150,width=212,command=ativ)
botaoAluno4 = Button(frameLogin2,text="Josyscleiton",bg="white",height=150,width=212,command=ativ)

#----------------------------

def telaInicial():
	frameMaster.pack(fill=X)

	frameQuit.pack(fill=X)
	botaoQuit.pack()
	frameWait.pack(fill=X)

	logo = PhotoImage(file="cognita.jpg")
	logo = logo.zoom(12)
	logo = logo.subsample(32)
	labelWait["image"] = logo
	labelWait.image = logo
	labelWait.pack()

def login(x):
	frameQuit.destroy()
	frameWait.destroy()

	frameLogin1.pack(fill=X)
	frameLogin2.pack(fill=X)	

	foto1 = PhotoImage(file="foto1r.gif")
	foto1 = foto1.zoom(11)
	foto1 = foto1.subsample(32)
	botaoAluno1.configure(image=foto1,compound=TOP)
	botaoAluno1.image=foto1

	foto2 = PhotoImage(file="foto2r.gif")
	foto2 = foto2.zoom(11)
	foto2 = foto2.subsample(32)
	botaoAluno2.configure(image=foto2,compound=TOP)
	botaoAluno2.image=foto2

	foto3 = PhotoImage(file="foto3r.gif")
	foto3 = foto3.zoom(11)
	foto3 = foto3.subsample(32)
	botaoAluno3.configure(image=foto3,compound=TOP)
	botaoAluno3.image=foto3

	foto4 = PhotoImage(file="foto4r.gif")
	foto4 = foto4.zoom(11)
	foto4 = foto4.subsample(32)
	botaoAluno4.configure(image=foto4,compound=TOP)
	botaoAluno4.image=foto4
	
	botaoAluno1.pack(side=LEFT,fill=X)
	botaoAluno2.pack(side=RIGHT,fill=X)
	botaoAluno3.pack(side=LEFT,fill=X)
	botaoAluno4.pack(side=RIGHT,fill=X)

#---------------------

labelWait.bind("<Double-Button-1>",login)

#---------------------

def main():
	telaInicial()

	root.geometry("480x320")
	root.mainloop()
	
if __name__ == "__main__":
	main()


'''
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
'''


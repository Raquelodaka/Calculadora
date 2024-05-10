from tkinter import *

#Forma/Figura/Desenho Calculadora
import tkinter as tkin
win = tkin.Tk()

#Titulo
win.title("Calculadora")

#Cor
win["bg"] = "pink"
win["background"] = "pink"

#funções
campotxt=""
def add_campotxt(sth):
    global campotxt
    campotxt=campotxt+str(sth)
    campo.delete("1.0","end")
    campo.insert("1.0",campotxt)

def calculo():
    global campotxt
    result=str(eval(campotxt))
    campo.delete("1.0", "end")
    campo.insert("1.0", result)

def limpar():
    global campotxt
    campotxt=""
    campo.delete("1.0", "end")

campo=tkin.Text(win,height=2,width=26,font=("Verdana", 20))
campo.grid(row=1, column=1, columnspan=4)

#botões dos números
#grid= grade, coluna onde esta o botão do respectivo número
bt1=tkin.Button(win, text="1",command=lambda: add_campotxt(1),width=5,font=("Verdana", 15))
bt1.grid(row=5,column=1)

bt2=tkin.Button(win, text="2",command=lambda: add_campotxt(2),width=5,font=("Verdana", 15))
bt2.grid(row=5,column=2)

bt3=tkin.Button(win, text="3",command=lambda: add_campotxt(3),width=5,font=("Verdana", 15))
bt3.grid(row=5,column=3)

bt4=tkin.Button(win, text="4",command=lambda: add_campotxt(4),width=5,font=("Verdana", 15))
bt4.grid(row=4,column=1)

bt5=tkin.Button(win, text="5",command=lambda: add_campotxt(5),width=5,font=("Verdana", 15))
bt5.grid(row=4,column=2)

bt6=tkin.Button(win, text="6",command=lambda: add_campotxt(6),width=5,font=("Verdana", 15))
bt6.grid(row=4,column=3)

bt7=tkin.Button(win, text="7",command=lambda: add_campotxt(7),width=5,font=("Verdana", 15))
bt7.grid(row=3,column=1)

bt8=tkin.Button(win, text="8",command=lambda: add_campotxt(8),width=5,font=("Verdana", 15))
bt8.grid(row=3,column=2)

bt8=tkin.Button(win, text="9",command=lambda: add_campotxt(8),width=5,font=("Verdana", 15))
bt8.grid(row=3,column=3)

bt0=tkin.Button(win, text="0",command=lambda: add_campotxt(0),width=5,font=("Verdana", 15))
bt0.grid(row=6,column=1)

#adicionando os botões de +,-,/,*,.,=,CE
btmais=tkin.Button(win, text="+",command=lambda: add_campotxt('+'),width=5,font=("Verdana", 15))
btmais.grid(row=5,column=4)

btmenos=tkin.Button(win, text="-",command=lambda: add_campotxt('-'),width=5,font=("Verdana", 15))
btmenos.grid(row=4,column=4)

btmulti=tkin.Button(win, text="*",command=lambda: add_campotxt('*'),width=5,font=("Verdana", 15))
btmulti.grid(row=3,column=4)

btdivi=tkin.Button(win, text="/",command=lambda: add_campotxt('/'),width=5,font=("Verdana", 15))
btdivi.grid(row=2,column=4)

btporc=tkin.Button(win, text="%",command=lambda: add_campotxt('%'),width=5,font=("Verdana", 15))
btporc.grid(row=2,column=3)

btporc=tkin.Button(win, text="^",command=lambda: add_campotxt('^'),width=5,font=("Verdana", 15))
btporc.grid(row=2,column=2)

btporc=tkin.Button(win, text="AC",command=lambda: limpar(),width=5,font=("Verdana", 15))
btporc.grid(row=2,column=1)

btdel=tkin.Button(win, text="CE",command=lambda: limpar(),width=5,font=("Verdana", 15))
btdel.grid(row=6,column=3)

btp=tkin.Button(win, text=".",command=lambda: add_campotxt('.'),width=5,font=("Verdana", 15))
btp.grid(row=6,column=2)

btigual=tkin.Button(win, text="=",command=lambda: calculo(),width=5,font=("Verdana", 15))
btigual.grid(row=6,column=4)

#não deixar maximizar ou minimizar
win.resizable(False, False)

#tamanho = Larg x Alt
#300 pixels X 300 pixels
win.geometry('350x215')

#Visualização da calculadora
win.mainloop()

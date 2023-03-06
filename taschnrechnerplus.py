import tkinter
from tkinter import ttk

# Erstellen des Hauptfensters
frmMain = tkinter.Tk()
frmMain.title("Taschenrechner")
frmMain.wm_geometry("300x300")


# Funktionen

def btnBeenden():
    frmMain.destroy()


def berechne():
    global ganzZahl
    rechner = (feld.get())
    feld.delete(0, "end")
    feld.insert(5, eval(rechner))
    ganzZahl =""

def clear_click():
    global ganzZahl

    feld.delete(0, "end")

    ganzZahl=""

ganzZahl = ""

def einfügen(x):
    global ganzZahl
    ganzZahl += str(x)
    print(ganzZahl)
    feld.delete(0, "end")
    feld.insert([0], ganzZahl)


# Erstellen der Entrys

feld = ttk.Entry(frmMain)
feld["width"] = 30
feld.place(x=50, y=50)

# Erstellen der Buttons
#auswahl = tkinter.StringVar
#auswahl.set("0")

eins = ttk.Button(frmMain, text="1", command=lambda: einfügen(1))
eins["width"] = 3
eins.place(x=50, y=200)

zwei = ttk.Button(frmMain, text="2", command=lambda: einfügen(2))
zwei["width"]= 3
zwei.place(x=90, y=200)

drei = ttk.Button(frmMain, text="3", command=lambda: einfügen(3))
drei["width"] = 3
drei.place(x=130, y=200)

vier = ttk.Button(frmMain, text="4", command=lambda: einfügen(4))
vier["width"] = 3
vier.place(x=50, y=160)

fünf = ttk.Button(frmMain, text="5", command=lambda: einfügen(5))
fünf["width"] = 3
fünf.place(x=90, y=160)

sechs = ttk.Button(frmMain, text="6", command=lambda: einfügen(6))
sechs["width"] = 3
sechs.place(x=130, y= 160)

sieben = ttk.Button(frmMain, text="7", command=lambda: einfügen(7))
sieben["width"] = 3
sieben.place(x=50, y=120)

acht= ttk.Button(frmMain, text="8", command=lambda: einfügen(8))
acht["width"] = 3
acht.place(x=90, y=120)

neun = ttk.Button(frmMain, text="9", command=lambda: einfügen(9))
neun["width"] = 3
neun.place(x=130, y=120)

null = ttk.Button(frmMain, text="0", command=lambda: einfügen("0"))
null["width"] = 3
null.place(x=50, y=240)

geteilt = ttk.Button(frmMain, text="/", command=lambda: einfügen("/"))
geteilt["width"] = 5
geteilt.place(x=170, y=120)

mal = ttk.Button(frmMain, text="*", command=lambda: einfügen("*"))
mal["width"] = 5
mal.place(x=170, y=160)

plus = ttk.Button(frmMain, text="+", command=lambda: einfügen("+"))
plus["width"] = 5
plus.place(x=170, y=240)

minus = ttk.Button(frmMain, text="-", command=lambda: einfügen("-"))
minus["width"] = 5
minus.place(x=170, y=200)

gleich = ttk.Button(frmMain, text="=", command=berechne)
gleich["width"] =3
gleich.place(x=130, y=240)

clear = ttk.Button(frmMain, text="C", command=clear_click)
clear["width"] = 3
clear.place(x=90, y=240)

beenden = ttk.Button(frmMain, text="Exit", command=btnBeenden)
beenden["width"] = 5
beenden.place(x=240, y=240)

#komma = ttk.Button(frmMain, text=",", command=lambda: einfügen(","))
#komma["width"]= 3
#komma.place(x=260, y=200)


# Erstellen der Endlosschleife

frmMain.mainloop()

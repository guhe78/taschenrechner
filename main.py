#Taschenrechner
import tkinter



#Funktionen
def _btn_Beenden_():
    frmMain.destroy()

def _button_null_():
    txt_ausgabe.insert('end', 0)

def _button_eins_():
    txt_ausgabe.insert('end', 1)

def _button_zwei_():
    txt_ausgabe.insert('end', 2)

def _button_drei_():
    txt_ausgabe.insert('end', 3)

def _button_vier_():
    txt_ausgabe.insert('end', 4)

def _button_fuenf_():
    txt_ausgabe.insert('end', 5)

def _button_sechs_():
    txt_ausgabe.insert('end', 6)

def _button_sieben_():
    txt_ausgabe.insert('end', 7)

def _button_acht_():
    txt_ausgabe.insert('end', 8)

def _button_neun_():
    txt_ausgabe.insert('end', 9)

def _button_komma_():
    txt_ausgabe.insert('end', ".")

def _button_plus_():
    txt_ausgabe.insert('end', "+")

def _button_minus_():
    txt_ausgabe.insert('end', "-")

def _button_multi_():
    txt_ausgabe.insert('end', "*")

def _button_divi_():
    txt_ausgabe.insert('end', "/")

def _button_klammer_auf_():
    txt_ausgabe.insert('end', "(")

def _button_klammer_zu_():
    txt_ausgabe.insert('end', ")")

def _button_back_():
    a = txt_ausgabe.get()
    laenge = len(a) -1
    txt_ausgabe.delete(laenge, 'end')

def _button_loeschen_():
    lbl_ausgabe.config(text="")
    txt_ausgabe.delete(0, 'end')

def _button_berechnen_():
    erg = txt_ausgabe.get()
    lbl_ausgabe.config(text=eval(erg))



#Hauptfenster
frmMain = tkinter.Tk()
frmMain.title("Taschenrechner")
frmMain.geometry('400x400')
frmMain.resizable(width=False, height=False)
frmMain.configure(bg='#FAEBD7')

#Buttons
btn_Beenden = tkinter.Button(frmMain, text="Ende", command=_btn_Beenden_)
btn_Beenden['height'] = 1
btn_Beenden['width'] = 5
btn_Beenden.place(x=350, y=370)

btn_null = tkinter.Button(frmMain, text="0", font="Arial 16 bold", command=_button_null_)
btn_null['height'] = 1
btn_null['width'] = 6
btn_null.place(x=100, y=350)

btn_komma = tkinter.Button(frmMain, text=",", font="Arial 16 bold", command=_button_komma_)
btn_komma['height'] = 1
btn_komma['width'] = 2
btn_komma.place(x=200, y=350)

btn_eins = tkinter.Button(frmMain, text="1", font="Arial 16 bold", command=_button_eins_)
btn_eins['height'] = 1
btn_eins['width'] = 2
btn_eins.place(x=100, y=300)

btn_zwei = tkinter.Button(frmMain, text="2", font="Arial 16 bold", command=_button_zwei_)
btn_zwei['height'] = 1
btn_zwei['width'] = 2
btn_zwei.place(x=150, y=300)

btn_drei = tkinter.Button(frmMain, text="3", font="Arial 16 bold", command=_button_drei_)
btn_drei['height'] = 1
btn_drei['width'] = 2
btn_drei.place(x=200, y=300)

btn_vier = tkinter.Button(frmMain, text="4", font="Arial 16 bold", command=_button_vier_)
btn_vier['height'] = 1
btn_vier['width'] = 2
btn_vier.place(x=100, y=250)

btn_fuenf = tkinter.Button(frmMain, text="5", font="Arial 16 bold", command=_button_fuenf_)
btn_fuenf['height'] = 1
btn_fuenf['width'] = 2
btn_fuenf.place(x=150, y=250)

btn_sechs = tkinter.Button(frmMain, text="6", font="Arial 16 bold", command=_button_sechs_)
btn_sechs['height'] = 1
btn_sechs['width'] = 2
btn_sechs.place(x=200, y=250)

btn_sieben = tkinter.Button(frmMain, text="7", font="Arial 16 bold", command=_button_sieben_)
btn_sieben['height'] = 1
btn_sieben['width'] = 2
btn_sieben.place(x=100, y=200)

btn_acht = tkinter.Button(frmMain, text="8", font="Arial 16 bold", command=_button_acht_)
btn_acht['height'] = 1
btn_acht['width'] = 2
btn_acht.place(x=150, y=200)

btn_neun = tkinter.Button(frmMain, text="9", font="Arial 16 bold", command=_button_neun_)
btn_neun['height'] = 1
btn_neun['width'] = 2
btn_neun.place(x=200, y=200)

btn_plus = tkinter.Button(frmMain, text="+", font="Arial 16 bold", command=_button_plus_)
btn_plus['height'] = 1
btn_plus['width'] = 2
btn_plus.place(x=50, y=350)

btn_minus = tkinter.Button(frmMain, text="-", font="Arial 16 bold", command=_button_minus_)
btn_minus['height'] = 1
btn_minus['width'] = 2
btn_minus.place(x=50, y=300)

btn_multi = tkinter.Button(frmMain, text="*", font="Arial 16 bold", command=_button_multi_)
btn_multi['height'] = 1
btn_multi['width'] = 2
btn_multi.place(x=50, y=250)

btn_division = tkinter.Button(frmMain, text="/", font="Arial 16 bold", command=_button_divi_)
btn_division['height'] = 1
btn_division['width'] = 2
btn_division.place(x=50, y=200)

btn_klammer_auf = tkinter.Button(frmMain, text="(", font="Arial 16 bold", command=_button_klammer_auf_)
btn_klammer_auf['height'] = 1
btn_klammer_auf['width'] = 2
btn_klammer_auf.place(x=100, y=150)

btn_klammer_zu = tkinter.Button(frmMain, text=")", font="Arial 16 bold", command=_button_klammer_zu_)
btn_klammer_zu['height'] = 1
btn_klammer_zu['width'] = 2
btn_klammer_zu.place(x=150, y=150)

btn_back = tkinter.Button(frmMain, text="<", font="Arial 16 bold", command=_button_back_)
btn_back['height'] = 1
btn_back['width'] = 2
btn_back.place(x=200, y=150)

btn_loeschen = tkinter.Button(frmMain, text="Clear", font="Arial 16 bold", command=_button_loeschen_)
btn_loeschen['height'] = 1
btn_loeschen['width'] = 4
btn_loeschen.place(x=250, y=150)

btn_berechnen = tkinter.Button(frmMain, text="=", font="Arial 16 bold", command=_button_berechnen_)
btn_berechnen['height'] = 1
btn_berechnen['width'] = 4
btn_berechnen.place(x=250, y=350)



#Labels
lbl_ausgabe = tkinter.Label(frmMain, bg='white', text="", font="Arial 25")
lbl_ausgabe['height'] = 1
lbl_ausgabe['width'] = 10
lbl_ausgabe.place(x=75, y=25)

#Entrys
txt_ausgabe = tkinter.Entry(frmMain, justify='right')
txt_ausgabe.place(x=110, y=100)






#Endlosschleife
frmMain.mainloop()

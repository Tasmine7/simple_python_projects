from tkinter import *
from tkinter.ttk import Combobox
import string
import random
tas_root = Tk()
tas_root.geometry("700x600")
tas_root.minsize(200,100)
tas_root.maxsize(600,500)
tas_root.title("ToDo List Application.")
title_label = Label(text="Welcome to the Password Generator.", bg="rosybrown3",fg="black", padx=15,pady=20, font=("comicsans,9,bold"), borderwidth=3, relief=GROOVE)
title_label.place(x=0, y=0)

def genpwd():
    length=pwd_value.get()
    t1 = string.ascii_lowercase
    t2 = string.ascii_uppercase
    t3 = string.digits
    t4 = string.punctuation
    tas = []
    tas.extend(list(t1))
    tas.extend(list(t2))
    tas.extend(list(t3))
    tas.extend(list(t4))
    random.shuffle(tas)
    pwd_value_entry.set("".join(tas[0:length]))

digits=["8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]

pwd_value = IntVar()
len_select = Combobox(tas_root, textvariable=pwd_value, state="readonly" )
len_select['values'] = [l for l in digits]
len_select.current(7)
len_select.place(x=260, y=100)

#label
pwd_length= Label(tas_root, text="Enter the length of the password", font=("comicsans,30,bold"),bg="thistle3",fg="black")
pwd_length.place(x=20,y=100)

#button
b1=Button(tas_root,text="Generate password",bg="orangered3",fg="black",font=("comicsans,30,bold") ,command=genpwd,cursor="hand2")
b1.place(x=20,y=170)

#entry
pwd_value_entry=StringVar()
pwd_entry = Entry(tas_root,textvariable=pwd_value_entry,font=("comicsans,30,bold"),state="readonly")
pwd_entry.place(x=20,y=230)


tas_root.mainloop()
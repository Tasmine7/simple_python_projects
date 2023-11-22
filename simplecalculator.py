from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if entryvalue.get().isdigit():
            value=int(entryvalue.get())
        else:
            value=eval(entry.get())
        entryvalue.set(value)
        entry.update()
    elif text=="C":
        entryvalue.set("")
        entry.update()
    elif text=="<--":
        entryvalue.set(entryvalue.get()[:-1])
        entry.update()
    else:
        entryvalue.set(entryvalue.get()+text)
        entry.update()



root=Tk()
root.geometry("320x360")
root.minsize(200, 100)
root.maxsize(400, 300)
root.title("Simple Calculator")





# frame
f1=Frame(root,borderwidth=3, bg="grey",relief=GROOVE,width=400,height=260)
f1.place(x=0,y=40)
#entry widget
entryvalue = StringVar()
entryvalue.set("")
entry = Entry(root,textvariable=entryvalue,width=64, font=("comicsans,80,bold"))
entry.place(x=5,y=9)
# buttons
b1 = Button(root,text="9", bg="black", font=("comicsans,9,bold"),height=3,width=6, borderwidth=3,fg="white")
b1.place(x=150,y=50)
b1.bind("<Button-1>",click)
b2= Button(root,text= "8",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b2.place(x=80,y=50)
b2.bind("<Button-1>",click)
b3= Button(root,text= "7",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b3.place(x=10,y=50)
b3.bind("<Button-1>",click)
b4= Button(root,text= "6",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b4.place(x=150,y=120)
b4.bind("<Button-1>",click)
b5= Button(root,text= "5",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b5.place(x=80,y=120)
b5.bind("<Button-1>",click)
b6= Button(root,text= "4",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b6.place(x=10,y=120)
b6.bind("<Button-1>",click)
b7= Button(root,text= "3",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b7.place(x=150,y=190)
b7.bind("<Button-1>",click)
b8= Button(root,text= "2",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b8.place(x=80,y=190)
b8.bind("<Button-1>",click)
b9= Button(root,text= "1",bg="black", font=("comicsans,9,bold"),height=3,width=6,borderwidth=3,fg="white")
b9.place(x=10,y=190)
b9.bind("<Button-1>",click)
b= Button(root,text= "0",bg="black", font=("comicsans,9,bold"),height=1,width=6,borderwidth=3,fg="white")
b.place(x=10,y=260)
b.bind("<Button-1>",click)
b_1=Button(root, text=".", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_1.place(x=80, y=260)
b_1.bind("<Button-1>",click)
b_2=Button(root, text="=", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_2.place(x=150, y=260)
b_2.bind("<Button-1>",click)
b_3=Button(root, text="C", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_3.place(x=220, y=50)
b_3.bind("<Button-1>",click)
b_4=Button(root, text="+", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_4.place(x=220, y=120)
b_4.bind("<Button-1>",click)
b_5=Button(root, text="-", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_5.place(x=220, y=155)
b_5.bind("<Button-1>",click)
b_6=Button(root, text="*", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_6.place(x=220, y=190)
b_6.bind("<Button-1>",click)
b_7=Button(root, text="/", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_7.place(x=220, y=225)
b_7.bind("<Button-1>",click)
b_8=Button(root, text="%", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_8.place(x=220, y=85)
b_8.bind("<Button-1>",click)
b_9=Button(root, text="<--", bg="black", font=("comicsans,9,bold"), height=1, width=6, borderwidth=3,fg="white")
b_9.place(x=220, y=260)
b_9.bind("<Button-1>",click)
root.mainloop()
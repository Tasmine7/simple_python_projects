from tkinter import *
import tkinter.messagebox
import json


root=Tk()
root.geometry("1200x900")
root.minsize(200, 100)
root.maxsize(1200, 1000)
root.title(" ToDo List Application")
task=[]
def getval():
    print("tasks entered")
    print(f"{taskvalue.get(), datevalue.get(),timevalue.get()}")

    with open("rec.txt","w") as f:
        pass
def add_task():
    task=task_entry.get()
    if task!="":
        list_box.insert(END,task)
        task_entry.delete(0,END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Add a task")
def add_date():
    Date=date_entry.get()
    if Date!="":
        list_box.insert(END,Date)
        date_entry.delete(0,END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Add a date")
def add_time():
    Time=time_entry.get()
    if Time!="":
        list_box.insert(END,Time)
        time_entry.delete(0,END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Add a specific time")
def load_task():
    try:
        tasks=json.load(open("rec.txt", "r"))
        list_box.delete(0, tkinter.END)
        for task in tasks:
            list_box.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="cannot be found")
def save_task():
    tasks=list_box.get(0,list_box.size())
    json.dump(tasks, open("rec.txt","w"))


def delete():
    try:
        task_1=list_box.curselection()[0]
        list_box.delete(task_1)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="you must enter something")



Label(text="Welcome to the ToDo List Application",bg="Deepskyblue2",padx=60,pady=30,font=("Georgia,30"), fg="black",relief=GROOVE,borderwidth=6).place(x=0,y=0)
Label(text="write down your tasks here :",bg="medium purple",padx=100,pady=30,font=("comicsans,30,bold"), fg="black",relief=GROOVE,borderwidth=6).place(x=0,y=90)
task=Label(root,text="Task",font=("comicsans,30,bold"),bg="Indian red",fg="black")


date=Label(root, text="Date", font=("comicsans,30,bold"),bg="SlateBlue2",fg="black")
time=Label(root,text="Time",font=("comicsans,30,bold"),bg="olive drab",fg="black")
task.place(x=40,y=200)
date.place(x=40,y=230)
time.place(x=40,y=260)
taskvalue=StringVar()
datevalue=StringVar()
timevalue=StringVar()
task_entry = Entry(root,textvariable=taskvalue,font=("comicsans,30,bold"))
date_entry = Entry(root,textvariable=datevalue,font=("comicsans,30,bold"))
time_entry = Entry(root,textvariable=timevalue,font=("comicsans,30,bold"))
task_entry.place(x=100, y=200)
date_entry.place(x=100, y=230)
time_entry.place(x=100, y=260)
#frame


# listbox and scrollbar
list_box= Listbox(root,width=160,height=15,bg="wheat2")
#scroller=Scrollbar(root,orient=VERTICAL,bg= "black", command=list_box.yview)
#scroller.place(x=260, y=50, height=232)
#list_box.config(yscrollcommand=scroller.set)
list_box.place(x=100,y=290)


b1 = Button(root, text="Add Task", command=add_task, bg="chocolate2")
b1.place(x=320,y=200)
b2=Button(root, text="Add  Date", command=add_date,bg="pink3")
b2.place(x=320,y=230)
b3=Button(root,text= "Add Time",command=add_time,bg="cadet blue")
b3.place(x=320,y=260)
b4=Button(root,text="Delete",command=delete,bg="red2")
b4.place(x=100,y=550)
b5 = Button(root,text="load previous task",command=load_task,bg="light coral")
b5.place(x=160,y=550)
b6 = Button(root,text="Save ",command=save_task, bg="Dodgerblue2")
b6.place(x=305,y=550)

root.mainloop()


from tkinter import *
from datetime import *
from os import system
import threading
root = Tk()
root.title("Library Management System")
root.geometry("360x460")
Lib = Label(text="Library Management System")
try:
    with open("Database.txt","r") as h:
        exec(h.read())
except:
    l1 = {}
    l2 = {}
    l3 = {}
# Function definitions
def unidgen():
    x=classent.get()
    y= secent.get()
    z = rollent.get()
    a = x+"_"+y+"_"+z
    unid = Label(text=a)
    unid.place(x=120,y=120)
def isdatelook():
    x=classent.get()
    y= secent.get()
    z = rollent.get()
    l1[x+"_"+y+"_"+z] = issueent.get()
    l2[x+"_"+y+"_"+z] = returnent.get()
    l3[x+"_"+y+"_"+z] = nament.get()
    date1 = date(*[int(x) for x in issueent.get().split("/")[::-1]])
    date2 = date(*[int(x) for x in returnent.get().split("/")[::-1]])
    noday = Label(text=f"{(date2-date1).days}")
    noday.place(x=250,y=165)
    with open("Database.txt","w") as x:
        x.writelines(f"l1 = {l1}\nl2 = {l2}\nl3 = {l3}")
def lookup():
    with open("Database.txt","r") as e:
        exec(e.read())
        issuedategive = Label(text=l1[entidbox.get()])
        issuedategive.place(x=80,y=390)
        returndategive = Label(text=l2[entidbox.get()])
        returndategive.place(x=230,y=390)
        namegive = Label(text=l3[entidbox.get()])
        namegive.place(x=50,y=360)
        date1 = date(*[int(x) for x in l2[entidbox.get()].split("/")[::-1]])
        if date.today() > date1:
            datediff= date.today() - date1
            datelabel = Label(text=f"₹{datediff.days}")
        else:
            datelabel = Label(text="Nil")
        datelabel.place(x=200,y=360)
def export():
    with open("Database.txt","r") as e:
        exec(e.read())
    d= []
    for i in l1:
        d.append(i)
        d.append(l3[i])
        d.append(l1[i])
        d.append(l2[i])
        d.append(" ")
    str = ",".join(d)
    str = str.split(" ,")
    str = "\n".join(str)
    with open("Database.csv","w") as f:
        f.writelines("Class_Sec_Roll,Name,Issue Date,Return Date,\n")
        f.writelines(str)
    t = threading.Thread(target=lambda:system("Database.csv"))
    t.start()
# Labels and Buttons assignment
namelabel = Label(text="Name of the student: ")
nament = Entry(root,width=25)
classlabel = Label(text="Class: ")
classent = Entry(root,width=5)
rolable = Label(text="Roll.No: ")
rollent = Entry(root,width=5)
seclable = Label(text="Section: ")
secent = Entry(root,width=5)
entbutt= Button(text="Enter", command= unidgen)
unidlab= Label(text="Unique Student ID: ")
issuedate = Label(text="Issue Date: ")
issueent= Entry(root,width=15)
returndate = Label(text="Return Date: ")
returnent = Entry(root, width = 15)
datent = Button(text="Enter",command=isdatelook)
__ = Label(text="_______________________________________________________________________")
lookup1 = Label(text="Lookup")
entid = Label(text="Enter Student ID: ")
entidbox = Entry(root,width=30)
namelabel2 = Label(text="Name: ")
issuedatelabel2 = Label(text="Issue Date: ")
returndatelabel2 = Label(text="Return Date: ")
gobutt = Button(text="GO!",command=lookup)
exportbutt = Button(text="Export",command=export)
late= Label(text="Late Fee: ")
noofday = Label(text="No. of days: ")
# Labels and Buttons placement
Lib.place(x=100,y=10)
namelabel.place(x=10,y=30)
nament.place(x=130,y=30)
classlabel.place(x=10,y=60)
classent.place(x=55,y=60)
seclable.place(x=100,y=60)
secent.place(x=150,y=60)
rolable.place(x=200,y=60)
rollent.place(x=250,y=60)
entbutt.place(x=160,y=90)
unidlab.place(x=10,y=120)
issuedate.place(x=10,y=150)
issueent.place(x=80,y=150)
returndate.place(x=5,y=180)
returnent.place(x=80,y=180)
noofday.place(x=180,y=165)
datent.place(x=160,y=210)
__.place(x=0,y=240)
lookup1.place(x=155,y=270)
entid.place(x=10,y=300)
entidbox.place(x=120,y=300)
gobutt.place(x=160,y=330)
namelabel2.place(x=10,y=360)
issuedatelabel2.place(x=10,y=390)
returndatelabel2.place(x=150,y=390)
late.place(x=150,y=360)
exportbutt.place(x=150,y=420)
# Main Loop
root.mainloop()

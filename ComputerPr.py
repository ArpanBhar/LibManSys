from tkinter import *
from datetime import *
from os import system
import threading
root = Tk()
root.title("Library Management System")
root.geometry("360x480")
root.resizable(False,False)
Lib = Label(text="Library Management System")
try:
    with open("Database.txt","r") as h:
        exec(h.read())
except:
    l1 = {}
    l2 = {}
    l3 = {}
    l4 = {}
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
    l4[x+"_"+y+"_"+z] = bookent.get()
    date1 = date(*[int(x) for x in issueent.get().split("/")[::-1]])
    date2 = date(*[int(x) for x in returnent.get().split("/")[::-1]])
    noday = Label(text=f"{(date2-date1).days}")
    noday.place(x=250,y=185)
    with open("Database.txt","w") as x:
        x.writelines(f"l1 = {l1}\nl2 = {l2}\nl3 = {l3}\nl4 = {l4}")
def lookup():
    with open("Database.txt","r") as e:
        exec(e.read())
        issuedategive = Label(text=l1[entidbox.get()])
        issuedategive.place(x=80,y=410)
        returndategive = Label(text=l2[entidbox.get()])
        returndategive.place(x=230,y=410)
        namegive = Label(text=l3[entidbox.get()])
        namegive.place(x=50,y=380)
        bookgive = Label(text = l4[entidbox.get()])
        bookgive.place(x=220,y=380)
        date1 = date(*[int(x) for x in l2[entidbox.get()].split("/")[::-1]])
        if date.today() > date1:
            datediff= date.today() - date1
            datelabel = Label(text=f"₹{datediff.days}")
        else:
            datelabel = Label(text="Nil")
        datelabel.place(x=60,y=440)
def export():
    with open("Database.txt","r") as e:
        exec(e.read())
    d= []
    for e,i in enumerate(l1,1):
        d.append(f"{(e)}")
        d.append(l3[i])
        d.append(",".join(i.split("_")))
        d.append(l4[i])
        d.append(l1[i])
        d.append(l2[i])
        d.append(" ")
    str = ",".join(d)
    str = str.split(" ,")
    str = "\n".join(str)
    with open("Database.csv","w") as f:
        f.writelines("Serial No.,Name,Class,Sec,Roll,Name of the Book,Issue Date,Return Date,\n")
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
booknameshow= Label(text="Book Name: ")
noofday = Label(text="No. of days: ")
bookname = Label(text="Book Name: ")
bookent = Entry(root,width=40)
late = Label(text="Late Fee: ")
# Labels and Buttons placement
Lib.place(x=100,y=5)
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
issuedate.place(x=10,y=175)
issueent.place(x=80,y=175)
returndate.place(x=5,y=200)
returnent.place(x=80,y=200)
noofday.place(x=180,y=185)
datent.place(x=160,y=230)
__.place(x=0,y=260)
lookup1.place(x=155,y=290)
entid.place(x=10,y=320)
entidbox.place(x=120,y=320)
gobutt.place(x=160,y=350)
namelabel2.place(x=10,y=380)
issuedatelabel2.place(x=10,y=410)
returndatelabel2.place(x=150,y=410)
booknameshow.place(x=150,y=380)
exportbutt.place(x=150,y=440)
late.place(x=10,y=440)
bookname.place(x=5,y=146)
bookent.place(x=80,y=146)
# Main Loop
root.mainloop()

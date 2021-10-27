from tkinter import *
import tkinter.messagebox as tm
from Data import ParMaSys

P=ParMaSys("MyDB.db")
GUI=Tk()

class First(object):
    e0=StringVar(GUI)
    e1=StringVar(GUI)
    e2=StringVar(GUI)
    e3=StringVar(GUI)
    e4=StringVar(GUI)
    def __init__(self,GUI):
        GUI.title("Project Python")
        width = 350
        height = 270
        screen_width = GUI.winfo_screenwidth()
        screen_height = GUI.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        GUI.geometry("%dx%d+%d+%d" % (width, height, x, y))
        GUI.resizable(0, 0)


        Label(GUI,text="ParMaSys",width=20,fg='White',bg='Black',font=("bold",23)).place(x=3,y=10)
        self.username=StringVar()
        self.passward=StringVar()
        Label(GUI, text="Username",bg="black",fg="white",height="3",width="25").place(x=10,y=70)
        e4 = Entry(GUI, textvariable=self.username)
        e4.place(x=205,y=85)

        Label(GUI, text="Passward",bg="black",fg="white",height="3",width="25").place(x=10,y=135)
        e2 = Entry(GUI, textvariable=self.passward,show=' ')
        e2.place(x=205,y=150)

        self.Place=StringVar()
        self.Name=StringVar()
        self.carno=StringVar()
        
        Button(GUI, text="Login",bg="Red", fg="white",width="20",height="2", command=self.show_entry_fields).place(x=20,y=200)
        Button(GUI, text="Exit", bg="Red", fg="White",width="20",height="2", command=self.Back).place(x=180,y=200)

    def Back(self):
        GUI.destroy()

    def Back1(self):
        GUI3.destroy()
        GUI2.deiconify()

    def Back2(self):
        GUI4.destroy()
        GUI3.deiconify()

    def Back3(self):
        GUI5.destroy()
        GUI2.deiconify()
        
    def Back4(self):
        GUI4.destroy()
        GUI2.deiconify()
    
    def show_entry_fields(self):
        if self.username.get()=="Python" and self.passward.get()=="Project":        
            tm.showinfo("Login info", "Welcome ")
            global GUI2
            GUI.withdraw()
            GUI2 = Toplevel()
            GUI2.title("ParMaSys")
            width = 600
            height = 350
            screen_width = GUI.winfo_screenwidth()
            screen_height = GUI.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            GUI2.geometry("%dx%d+%d+%d" % (width, height, x, y))
            GUI2.resizable(0, 0)
      
            Label(GUI2, text="WEL-COME",bg="Black",width="25",fg="white",height="2", font=('times new roman', 35)).place(y=1)
            Button(GUI2, text='Logout',bg="Red",fg="Black",width="10", height="1",command=self.Back).place(x=510,y=75)

            Button(GUI2, text='Empty', bg="Skyblue", fg="black",width="30", height="10" ,font=("bold",9),command=self.Empty).place(x=0,y=150)
            Button(GUI2, text='TOTAL',bg='Yellow', fg='black',width="30",height="10",font=("bold", 9),command=self.Total).place(x=200,y=150)
            Button(GUI2, text='Reserved', bg="Violet", fg="black",width="30", height="10",font=("bold",9),command=self.Full).place(x=400,y=150) 
        else:
            tm.showinfo("Login info","Please Enter Correct Username & Passward")
            self.username.set("")
            self.passward.set("")

    def Bill(self):
        if self.Place.get()=="" or self.Name.get()=="" or self.carno.get()=="":        
            tm.showinfo("Bill info","Please Enter Complete information")
        else:
            b=P.check1(self.Place.get())
            if(b==[]):
                tm.showinfo("Bill info", "Place is not Empty")
                self.Place.set("")
                self.Name.set("")
                self.carno.set("")
            else:
                tm.showinfo("Bill info", "User Added")
                global GUI5
                GUI4.withdraw()
                GUI5 = Toplevel()
                GUI5.title("ParMaSys:\Empty:\Bill")
                width = 380
                height = 300
                screen_width = GUI4.winfo_screenwidth()
                screen_height = GUI4.winfo_screenheight()
                x = (screen_width/2) - (width/2)
                y = (screen_height/2) - (height/2)
                GUI5.geometry("%dx%d+%d+%d" % (width, height, x, y))
                GUI5.resizable(0, 0)
                Label(GUI5,text="Bill",width=20,fg='White',bg='Black',font=("bold",23)).place(x=3,y=10)

                Label(GUI5, text="Location.",bg="black",fg="white",height="3",width="22").place(x=10,y=60)
                Label(GUI5, text=self.Place.get() ,bg="black",fg="white",height="3",width="22").place(x=205,y=60)

                Label(GUI5, text="Username",bg="black",fg="white",height="3",width="22").place(x=10,y=125)
                Label(GUI5, text=self.Name.get() , bg="black", fg="white",height="3",width="22").place(x=205,y=125)

                Label(GUI5, text="VehicleNo.",bg="black",fg="white",height="3",width="22").place(x=10,y=190)
                Label(GUI5, text=self.carno.get() , bg="black", fg="white",height="3",width="22").place(x=205,y=190)
                P.adduser(self.Place.get(),self.Name.get(), self.carno.get())
                Button(GUI5, text="Back", bg="Red", fg="White",width="50",height="2", command=self.Back3).place(x=10,y=250)  
    
    def Add(self):
        global GUI4
        GUI3.withdraw()
        GUI4 = Toplevel()
        GUI4.title("ParMaSys:\Empty:\Add Account")
        width = 350
        height = 300
        screen_width = GUI4.winfo_screenwidth()
        screen_height = GUI4.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        GUI4.geometry("%dx%d+%d+%d" % (width, height, x, y))
        GUI4.resizable(0, 0)
        Label(GUI4,text="Inofrmation",width=20,fg='White',bg='Black',font=("bold",23)).place(x=3,y=10)
        
        Label(GUI4, text="Place",bg="black",fg="white",height="3",width="25").place(x=10,y=60)
        e1= Entry(GUI4, textvariable=self.Place)
        e1.place(x=205,y=75)

        Label(GUI4, text="Username",bg="black",fg="white",height="3",width="25").place(x=10,y=120)
        self.e0 = Entry(GUI4, textvariable=self.Name)
        self.e0.place(x=205,y=140)

        Label(GUI4, text="VehicleNo.",bg="black",fg="white",height="3",width="25").place(x=10,y=180)
        self.e1 = Entry(GUI4, textvariable=self.carno)
        self.e1.place(x=205,y=200)
        self.Place.set("")
        self.Name.set("")
        self.carno.set("")
        Button(GUI4, text="Add",bg="Red", fg="white",width="20",height="2", command=self.Bill).place(x=20,y=240)
        Button(GUI4, text="Back", bg="Red", fg="White",width="20",height="2", command=self.Back2).place(x=180,y=240)


    def Empty(self):
        global GUI3
        GUI2.withdraw()
        GUI3 = Toplevel()
        GUI3.title("ParMaSys:\Empty")
        width = 600
        height = 450
        screen_width = GUI.winfo_screenwidth()
        screen_height = GUI.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        GUI3.geometry("%dx%d+%d+%d" % (width, height, x, y))
        GUI3.resizable(0, 0)
        Label(GUI3, text="Empty",bg="Black",width="25",fg="white",height="1", font=('times new roman', 35)).place(y=1)
        Button(GUI3, text='Add',bg="Red",fg="Black",width="10", height="1",command=self.Add).place(x=10,y=25)
        Button(GUI3, text='Back',bg="Red",fg="Black",width="10", height="1",command=self.Back1).place(x=510,y=25)

        self.output=Listbox(GUI3, height=24, width=99)
        self.output.place(x=1,y=61)
        for a in P.viewemp():
            self.output.insert(END, a)

    def Rm(self):
        b=P.check(self.Place.get())
        if(b==[]):
                tm.showinfo("Removing info", "This Place is Already Empty")
        else:
            P.delete(self.Place.get())
        self.Place.set("")
        
    def Del(self):
        a=P.view()
        if(a==[]):
            tm.showinfo("Delete info", "All Places are Empty ")
        else:   
            global GUI4
            GUI3.withdraw()
            GUI4 = Toplevel()
            GUI4.title("ParMaSys:\Empty:\Remove")
            width = 350
            height = 200
            screen_width = GUI4.winfo_screenwidth()
            screen_height = GUI4.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            GUI4.geometry("%dx%d+%d+%d" % (width, height, x, y))
            GUI4.resizable(0, 0)
            Label(GUI4, text="Place",bg="black",fg="white",height="3",width="25").place(x=10,y=60)
            self.Place.set("")
            self.e1= Entry(GUI4, textvariable=self.Place)
            self.e1.place(x=205,y=75)
            Button(GUI4, text="Remove",bg="Red", fg="white",width="20",height="2", command=self.Rm).place(x=20,y=140)
            Button(GUI4, text="Back",bg="Red", fg="white",width="20",height="2", command=self.Back4).place(x=180,y=140)
            
        
    def Full(self):
        global GUI3
        GUI2.withdraw()
        GUI3 = Tk()
        GUI3.title("ParMaSys:\Reserved")
        width = 600
        height = 450
        screen_width = GUI.winfo_screenwidth()
        screen_height = GUI.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        GUI3.geometry("%dx%d+%d+%d" % (width, height, x, y))
        GUI3.resizable(0, 0)
        Label(GUI3, text="Full",bg="Black",width="25",fg="white",height="1", font=('times new roman', 35)).place(y=1)
        Button(GUI3, text='Remove',bg="Red",fg="Black",width="10", height="1",command=self.Del).place(x=10,y=25)
        Button(GUI3, text='Back',bg="Red",fg="Black",width="10", height="1",command=self.Back1).place(x=510,y=25)
        
        self.output=Listbox(GUI3, height=23, width=55)
        self.output.place(x=150,y=65)
        self.output.insert(END, "Place  Name  Vehicleno")
        for a in P.view():
            self.output.insert(END, a,str(" "))
                
        
   
    def Call(self,i):
        a= P.check(i)
        if(a==[]):
            return "Yellow"
        else:
            return "Red"


    def Total(self):
        global GUI3
        GUI2.withdraw()
        GUI3 = Toplevel()
        GUI3.title("ParMaSys:\Total")
        width = 600
        height = 450
        screen_width = GUI.winfo_screenwidth()
        screen_height = GUI.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        GUI3.geometry("%dx%d+%d+%d" % (width, height, x, y))
        GUI3.resizable(0, 0)
        GUI3.config(bg="Pink")
        Label(GUI3, text="Total",bg="Black",width="25",fg="white",height="1", font=('times new roman', 35)).place(y=1)
        Button(GUI3, text='Back',bg="Red",fg="Black",width="10", height="1",command=self.Back1).place(x=510,y=25)
        for i in range(1,11,1):
            Label(GUI3, text=i,bg=self.Call(i),width="3",fg="black",height=3, font=('times new roman', 15)).place(x=((i-1)*50)+60,y=65)
        for i in range(11,21,1):
            Label(GUI3, text=i,bg=self.Call(i),width="3",fg="black",height=3, font=('times new roman', 15)).place(x=((i-11)*50)+60,y=180)
        for i in range(21,31,1):
            Label(GUI3, text=i,bg=self.Call(i),width="3",fg="black",height=3, font=('times new roman', 15)).place(x=((i-21)*50)+60,y=260)
        for i in range(31,41,1):
            Label(GUI3, text=i,bg=self.Call(i),width="3",fg="black",height=3, font=('times new roman', 15)).place(x=((i-31)*50)+60,y=375)

        Label(GUI3, text="-->",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=60)
        Label(GUI3, text="E",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=115)
        Label(GUI3, text="N",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=170)
        Label(GUI3, text="T",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=225)
        Label(GUI3, text="R",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=280)
        Label(GUI3, text="Y",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=335)
        Label(GUI3, text="-->",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(y=380)
   
        Label(GUI3, text="-->",bg="Black",width="3",fg="white",height=4, font=('times new roman', 15)).place(x=565,y=60)
        Label(GUI3, text="E",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(x=565,y=130)
        Label(GUI3, text="X",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(x=565,y=190)
        Label(GUI3, text="I",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(x=565,y=250)
        Label(GUI3, text="T",bg="Black",width="3",fg="white",height=3, font=('times new roman', 15)).place(x=565,y=310)
        Label(GUI3, text="-->",bg="Black",width="3",fg="white",height=4, font=('times new roman', 15)).place(x=565,y=370)

#Main Program
First(GUI)
GUI.mainloop()

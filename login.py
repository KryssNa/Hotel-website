from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

import sqlite3

conn=sqlite3.connect("kryss.db")
c=conn.cursor()
# c.execute("""CREATE TABLE  userdetail(
#     f_name text,
#     l_name text,
#     username text,
#     password text,
#     c_password text,
#     id_num integer
#     )""")
# print("Table created successfully")

root=Tk()
root.title("Hotel Management System")
root.geometry("1440x1024")

#for bg image
image1=Image.open("67.png")
photo=ImageTk.PhotoImage(image1)
image_label=Label(image=photo)
image_label.pack()


def reg():
        if first_name.get() == "" or last_name.get() == "" or username.get() == "":
            messagebox.showerror("Error", "All Fields are required to fill")
        elif password.get() != password.get():
            messagebox.showerror("Error", "Password must be same.Your password is not matched!!!")
        else:
            try:
                conn = sqlite3.connect("kryss.db")
                c = conn.cursor()
                c.execute("INSERT INTO userdetail values(:f_name,:l_name,:username,:password,:c_password,:id_num)",
                            {
                             "f_name":first_name.get(),
                             "l_name":last_name.get(),
                             "username":username.get(),
                             "password":password.get(),
                             "c_password":confirm_password.get(),
                             "id_num":ID.get()
                             
                             })
                conn.commit()
                conn.close()
                messagebox.showinfo("success", "Register Successfull")
            except Exception as es:
                    messagebox.showerror("Error", f"error due to:{str(es)}")
   
def login():
    if userentry.get() == "" or passentry.get() == "":
        messagebox.showerror("Error", "Please enter a correct Login Id")
    elif userentry.get() == "kryss" and passentry.get() == "123":
        messagebox.showinfo("Sucess", "Only Admin has premession to access this page")
    else:
        conn= sqlite3.connect("kryss.db")
        c=conn.cursor()
        #print(txtpass1)
        c.execute("SELECT * from userdetail WHERE userentry=%s and passentry=%s",(
                                                                    userentry.get(),
                                                                    passentry.get()))
        
        row=c.fetchone()
        
        if row==None:
            messagebox.showerror("Error","Invalid Username or password")
        else:
            open=messagebox.askyesno("Yes or No","This page is only accessbale by the Admin.Are you sure want to access this page?")
            if open>0:
                messagebox.showinfo("Information", "You are directing towards our main Page ")

                root14=Toplevel()
                root14.title('WELCOME TO HOTEL MANGEMENT SYSTEM')
                root14.geometry("1440x1024")
                global load,img
                load=Image.open("44.png")
                load=load.resize((1350,720),Image.ANTIALIAS)
                render=ImageTk.PhotoImage(load)
                img=Label(root14,image=render)
                img.place(x=0,y=0)
                logout_1=Button(root14,text="LOG OUT",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=1225,y=43)
                custmor=Button(root14,text="CUSTOMERS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=350,y=100)
                booking=Button(root14,text="BOOKING",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=520,y=100)
                # room=Button(root4,text="CUSTOMER BILLING DASHBOARD",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)
                contact=Button(root14,text="REPORT AN ISSUE",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=830,y=100)
                payment=Button(root14,text="FOOD ITEMS",font=('Consolas',12,"bold"),bg="#39065D",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=650,y=100)
            else:
                messagebox.showinfo("Error","you have no premission to access this page. Thank you for visitng our page!")
            conn.commit()
            conn.close()
def regis():
    root.title("REGISTRATION")
    root.geometry("1440x1024") 
    
    global first_name
    global last_name
    global username
    global password
    global confirm_password
    global ID
    
    image1=Image.open("67.png")
    photo=ImageTk.PhotoImage(image1)
    image_label=Label(image=photo)
    image_label.pack()

    #register frame window
    regframe=Frame(root,height=420,width=400,bg="black",pady=10,padx=5)
    regframe.place(x=505,y=110)

    #all label and entry widget
    label_newReg=Label(regframe,text="New Registration",font=("Montserrat light", 15, "bold"),fg="white",bg="black")
    label_newReg.place(x=120,y=20)

    f_name=Label(regframe,text="First Name:",fg="white",bg="black",font=("Normal", 10, ""))
    f_name.place(x=50,y=80)
    first_name=Entry(regframe,font=("Regular", 10,))
    first_name.place(x=140,y=80,width=155)

    L_name=Label(regframe,text="Last Name:",fg="white",bg="black",font=("Normal", 10, ""))
    L_name.place(x=50,y=120)
    last_name=Entry(regframe,font=("Regular", 10,))
    last_name.place(x=140,y=120,width=155)

    userlabel=Label(regframe,text="Username:",fg="white",bg="black",font=("Montserrat light", 10, ))
    userlabel.place(x=55,y=160)
    username=Entry(regframe,font=("Regular", 10,))
    username.place(x=140,y=160,width=155)

    labelpass=Label(regframe,text="Password:",fg="white",bg="black",font=("Montserrat light", 10,))
    labelpass.place(x=57,y=200)
    password=Entry(regframe,show="*",font=("Regular", 10,))
    password.place(x=140,y=200,width=155)

    labelCpass=Label(regframe,text="Confirm Password:",fg="white",bg="black",font=("Montserrat light", 10, ))
    labelCpass.place(x=10,y=240)
    confirm_password=Entry(regframe,show="*",font=("Regular", 10,))
    confirm_password.place(x=140,y=240,width=155)

    label_id=Label(regframe,text="ID Number:",fg="white",bg="black",font=("Montserrat light", 10, ))
    label_id.place(x=53,y=280)
    ID=Entry(regframe,font=("Regular", 10,))
    ID.place(x=140,y=280,width=155)
    
    #for register button
    registerbtn=Button(regframe,text="Register",command=reg,font=("Montserrat bold",11), bg="#F47F16",width=11,height=0,
                        fg="black", cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black")
    registerbtn.place(x=160,y=320)

    root.mainloop()

##login page

#for frame
myframe=Frame(root,height=350,width=290,bg="black",pady=20,padx=35)
myframe.place(x=505,y=110)

#for username &password, entry widget and submit button

label_getstarted=Label(myframe,text="Get started",font=("Montserrat SemiBold", 15, "bold"),fg="white",bg="black")
label_getstarted.place(x=50,y=0)

user=Label(myframe,text="Username",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
user.place(x=10,y=40)
userentry=Entry(myframe,font=("Regular", 12,))
userentry.place(x=10,y=65,height=25,width=185)

password=Label(myframe,text="Password",fg="white",bg="black",font=("Montserrat light", 11, "bold"))
password.place(x=10,y=100)
passentry=Entry(myframe,font=("Regular", 12,))
passentry.place(x=10,y=125,height=25,width=185)

b=Button(myframe,text="Login",bg="#F47F16",fg="black", cursor="hand2",command=login, borderwidth=0,width=9, activebackground="#F47F16",
          font=("Montserrat SemiBold", 11, "bold"))
b.place(x=65,y=160)


New_Reg = Button(myframe, text="NEW REGISTRATION",command=regis,font=("Montserrat SemiBold",9,), fg="white", bg="black", borderwidth=0,cursor="hand2",activebackground="black")
New_Reg.place(x=0, y=260)

For_got = Button(myframe, text="RESET PASSWORD?", font=("Montserrat SemiBold",9,), fg="white", bg="black",activebackground="black",
                         borderwidth=0, cursor="hand2")
For_got.place(x=0, y=285)

root.mainloop()
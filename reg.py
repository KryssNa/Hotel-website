##for registration

from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Hotel Management System")
root.geometry("1440x1024")

#for bg image
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
e1=Entry(regframe,font=("Regular", 10,))
e1.place(x=140,y=80,width=155)

L_name=Label(regframe,text="Last Name:",fg="white",bg="black",font=("Normal", 10, ""))
L_name.place(x=50,y=120)
e6=Entry(regframe,font=("Regular", 10,))
e6.place(x=140,y=120,width=155)

username=Label(regframe,text="Username:",fg="white",bg="black",font=("Montserrat light", 10, ))
username.place(x=55,y=160)
e2=Entry(regframe,font=("Regular", 10,))
e2.place(x=140,y=160,width=155)

password=Label(regframe,text="Password:",fg="white",bg="black",font=("Montserrat light", 10,))
password.place(x=57,y=200)
e3=Entry(regframe,font=("Regular", 10,))
e3.place(x=140,y=200,width=155)

c_password=Label(regframe,text="Confirm Password:",fg="white",bg="black",font=("Montserrat light", 10, ))
c_password.place(x=10,y=240)
e4=Entry(regframe,font=("Regular", 10,))
e4.place(x=140,y=240,width=155)

Id_num=Label(regframe,text="ID Number:",fg="white",bg="black",font=("Montserrat light", 10, ))
Id_num.place(x=53,y=280)
e5=Entry(regframe,font=("Regular", 10,))
e5.place(x=140,y=280,width=155)


#for register button
registerbtn=Button(regframe,text="Register",font=("Montserrat bold",11), bg="#F47F16",width=11,height=0,
                     fg="black", cursor="hand2", borderwidth=0, activeforeground="black", activebackground="black")
registerbtn.place(x=160,y=320)

root.mainloop()



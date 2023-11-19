from tkinter import *
from tkinter.messagebox import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\python_bus.png')
img_home=PhotoImage(file='.\\home.png')
bus=Label(root,image=img)
bus.grid(row=0,column=0,columnspan=20,padx=w//3)
title1=Label(root,text='Online Bus Booking System',bg='light blue',fg='Red',font='Arial 25 bold')
title1.grid(row=1,column=0,columnspan=20,padx=w//3)
title2=Label(root,text='Add Bus Operator Details',bg='seashell2',fg='green3',font='Arial 20 bold')
title2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

operator_id=Label(root,text='Operator ID',font='Arial 14')
operator_id.grid(row=3,column=1,pady=30)
name=Label(root,text='Name',font='Arial 14')
name.grid(row=3,column=3,pady=30)
add=Label(root,text='Address',font='Arial 14')
add.grid(row=3,column=5,pady=30)
phone=Label(root,text='Phone',font='Arial 14')
phone.grid(row=3,column=7,pady=30)
mail=Label(root,text='Email',font='Arial 14')
mail.grid(row=3,column=9,pady=30)
operatorf=Entry(root)
operatorf.grid(row=3,column=2,pady=30)
newf=Entry(root)
newf.grid(row=3,column=4,pady=30)
addf=Entry(root)
addf.grid(row=3,column=6,pady=30)
phonef=Entry(root)
phonef.grid(row=3,column=8,pady=30)
mailf=Entry(root)
mailf.grid(row=3,column=10,pady=30)

def addnew():
    op1=Label(root,text='{} {} {} {} {}'.format(operatorf.get(),newf.get(),addf.get(),phonef.get(),mailf.get()),font='Arial 12')
    op1.grid(row=4,columnspan=13)
    showinfo('Operator Entry Updated','Operator Record updated successfully')
    
addb=Button(root,text='Add',bg='SpringGreen2',font='Arial 14',command=addnew)
addb.grid(row=3,column=11,pady=30)
editb=Button(root,text='Edit',bg='SpringGreen2',font='Arial 14')
editb.grid(row=3,column=12,pady=30)

def home1():
    root.destroy()
    import Screen2_Home
home=Button(root,image=img_home,bg='light green',command=home1)
home.grid(row=4,column=9,pady=30)

root.mainloop()

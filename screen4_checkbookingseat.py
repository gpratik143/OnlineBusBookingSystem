from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\python_bus.png')
img_home=PhotoImage(file='.\\home.png')
Label(root, image=img).grid(row=0, column=0, columnspan=20, padx=w//3)
title=Label(root,text='Online Bus Booking System',bg='SkyBlue3',fg='Red3',font="Arial 20 bold")
title.grid(row=1, column=0,columnspan=20,padx=w//3)
title2=Label(root,text='Check Your Booking',bg='green3',fg='dark green',font='Arial 22 bold')
title2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

mobile=Label(root,text='Enter your mobile number',font='Arial 12')
mobile.grid(row=3,column=8,sticky=E)   
mobilef=Entry(root)
mobilef.grid(row=3,column=9,sticky=EW,padx=5)

def check_book():
    op1=Label(root,text="Here's your Ticket",font='Arial 12')
    op1.grid(row=4,columnspan=20,padx=w//3,)
chb=Button(root,text='Check Booking',font='Arial 14',command=check_book)
chb.grid(row=3,column=10,sticky=W)

root.mainloop()

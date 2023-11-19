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
title2=Label(root,text='Add Bus Details',bg='seashell2',fg='green3',font='Arial 20 bold')
title2.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)

bus_id=Label(root,text='Bus ID',font='Arial 14')
bus_id.grid(row=3,column=1,pady=40)
bus_idf=Entry(root)
bus_idf.grid(row=3,column=2,pady=40)
running_date=Label(root,text='Running Date',font='Arial 14')
running_date.grid(row=3,column=3,pady=40)
running_datef=Entry(root)
running_datef.grid(row=3,column=4,pady=40)
seat_available=Label(root,text='Seat Available',font='Arial 14')
seat_available.grid(row=3,column=5,pady=40)
seat_availablef=Entry(root)
seat_availablef.grid(row=3,column=6,pady=40)

def addnewrunning():
    op1=Label(root,text='{} {} {}'.format(bus_idf.get(),running_datef.get(),seat_availablef.get()),font='Arial 12')
    op1.grid(row=4,columnspan=13)
    showinfo('Bus Running Updated','Bus Running Record updated successfully')
    
addb=Button(root,text='Add Run',bg='SpringGreen2',font='Arial 14',command=addnewrunning)
addb.grid(row=3,column=8)
editb=Button(root,text='Delete Run',bg='SpringGreen2',fg='Red',font='Arial 14')
editb.grid(row=3,column=9)

def home4():
    root.destroy()
    import Screen2_Home
home=Button(root,image=img_home,bg='light green',command=home4)
home.grid(row=5,column=8)

root.mainloop()

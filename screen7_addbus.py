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
bus_type=Label(root,text='Bus Type',font='Arial 14')
bus_type.grid(row=3,column=3,pady=40)
bus_type=StringVar()
bus_type.set('--select--')
option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1']
d_menu=OptionMenu(root,bus_type,*option)
d_menu.grid(row=3,column=4,pady=40)
capacity=Label(root,text='Capacity',font='Arial 14')
capacity.grid(row=3,column=5,pady=40)
capacityf=Entry(root)
capacityf.grid(row=3,column=6,pady=40)
fare_rs=Label(root,text='Fare Rs',font='Arial 14')
fare_rs.grid(row=3,column=7,pady=40)
fare_rsf=Entry(root)
fare_rsf.grid(row=3,column=8,pady=40)
operator_id=Label(root,text='Operator ID',font='Arial 14')
operator_id.grid(row=3,column=9,pady=40)
operatorf=Entry(root)
operatorf.grid(row=3,column=10,pady=40)
route_id=Label(root,text='Route ID',font='Arial 14')
route_id.grid(row=3,column=11,pady=40)
route_idf=Entry(root)
route_idf.grid(row=3,column=12,pady=40)

def addnewbus():
    op1=Label(root,text='{} {} {} {} {} {}'.format(bus_idf.get(),bus_type.get(),capacityf.get(),fare_rsf.get(),operatorf.get(),route_idf.get()),font='Arial 12')
    op1.grid(row=4,columnspan=13)
    showinfo('Bus Entry','Bus Record added')
    
addb=Button(root,text='Add Bus',bg='SpringGreen2',font='Arial 14',command=addnewbus)
addb.grid(row=5,column=7)
editb=Button(root,text='Edit Bus',bg='SpringGreen2',font='Arial 14')
editb.grid(row=5,column=8)

def home2():
    root.destroy()
    import Screen2_Home
home=Button(root,image=img_home,bg='light green',command=home2)
home.grid(row=5,column=9)

root.mainloop()

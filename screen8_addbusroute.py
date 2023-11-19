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

route_id=Label(root,text='Route ID',font='Arial 14')
route_id.grid(row=3,column=2,pady=40)
route_idf=Entry(root)
route_idf.grid(row=3,column=3,pady=40)
station_name=Label(root,text='Station Name',font='Arial 14')
station_name.grid(row=3,column=4,pady=40)
station_namef=Entry(root)
station_namef.grid(row=3,column=5,pady=40)
station_id=Label(root,text='Station ID',font='Arial 14')
station_id.grid(row=3,column=6,pady=40)
station_idf=Entry(root)
station_idf.grid(row=3,column=7,pady=40)

def addnewbusroute():
    op1=Label(root,text='{} {} {}'.format(route_idf.get(),station_namef.get(),station_idf.get()),font='Arial 12')
    op1.grid(row=4,columnspan=13)
    showinfo('Route Entry Updated','Bus Route Record updated successfully')
    
addb=Button(root,text='Add Route',bg='SpringGreen2',font='Arial 14',command=addnewbusroute)
addb.grid(row=3,column=8)
editb=Button(root,text='Delete Route',bg='SpringGreen2',fg='Red',font='Arial 14')
editb.grid(row=3,column=9)

def home3():
    root.destroy()
    import Screen2_Home
home=Button(root,image=img_home,bg='light green',command=home3)
home.grid(row=5,column=9)

root.mainloop() 

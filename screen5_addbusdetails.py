from tkinter import *
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\python_bus.png')
Label(root, image=img).grid(row=0, column=0, columnspan=20, padx=w//3)
title=Label(root,text='Online Bus Booking System',bg='SkyBlue3',fg='Red3',font="Arial 25 bold")
title.grid(row=1, column=0,columnspan=20,padx=w//3)
title2=Label(root,text='Add New Details to DataBase',bg='seashell2',fg='green3',font='Arial 20 bold')
title2.grid(row=2,column=0,columnspan=5,padx=w//3,pady=20)

def b1o():
    root.destroy()
    import screen6_operator
def b2ab():
    root.destroy()
    import screen7_addbus
def b3abr():
    root.destroy()
    import screen8_addbusroute
def b4abrd():
    root.destroy()
    import screen9_addbusrunningdetail

operator=Button(root,text='New Operator',bg='light green',font='Arial 16',command=b1o)
operator.grid(row=3,column=1,pady=20)
new_bus=Button(root,text='New Bus',bg='orange red',font='Arial 16',command=b2ab)
new_bus.grid(row=3,column=2,pady=20)
route=Button(root,text='New Route',bg='steel blue1',font='Arial 16',command=b3abr)
route.grid(row=3,column=3,pady=20)
new_run=Button(root,text='New Run',bg='light coral',font='Arial 16',command=b4abrd)
new_run.grid(row=3,column=4,pady=20)

root.mainloop()


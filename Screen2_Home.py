from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\python_bus.png')
Label(root, image=img).grid(row=0, column=0, columnspan=3, padx=w//3)
Label(root,text='Online Bus Booking System', bg='SkyBlue3', fg='Red3', font="Arial 20 bold").grid(row=1, column=0, columnspan=3, padx=w//3)
def b1():
    root.destroy()
    import Screen3_seatbooking

def b2():
    root.destroy()
    import Screen4_checkbookingseat

def b3():
    root.destroy()
    import Screen5_addbusdetails


b1=Button(root, text='Seat Booking',bg='pale green', font="Arial 20 bold",command=b1)
b1.grid(row=2,column=0,pady=80)
b2=Button(root, text='Check Booked Seat',bg='lime green', font="Arial 20 bold",command=b2)
b2.grid(row=2,column=1,pady=80)
b3=Button(root, text='Add Bus Details',bg='dark green', font="Arial 20 bold",command=b3)
b3.grid(row=2,column=2,pady=80)
Label(root, text='For Admin Only',fg='Red3', font="Arial 13").grid(row=3,column=2)



root.mainloop()

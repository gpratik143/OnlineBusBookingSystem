from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
#bus image
bus=PhotoImage(file='.\\python_bus.png')
Label(root,image=bus).grid(row=0,columnspan=10,padx=w/2.5)
#online bus booking sysyetm
Label(root,text='Online Bus Booking',font='Arial 30',fg='red',bg='sky blue').grid(row=1,columnspan=10)
Label(root,text='').grid(row=2,columnspan=10,pady=20)
#Submiited to
Label(root,text='Submitted To : Dr. Mahesh Kumar',font='Arial 25',fg='red',bg='sky blue').grid(row=9,columnspan=10)
#Project Based Learning
Label(root,text='Project Based Learning',font='Arial 15',fg='blue').grid(row=10,columnspan=10)
#Student Name
Label(root,text='Name : Pratik Gupta',font='Calibri 20 bold',fg='blue').grid(row=3,columnspan=10)
Label(root,text='').grid(row=4,columnspan=10,pady=10)
#Enrollment Number
Label(root,text='Er. No. : 221B276',font='Calibri 20 bold',fg='blue').grid(row=5,columnspan=10)
Label(root,text='').grid(row=6,columnspan=10,pady=10)
#monibe number
Label(root,text='Mobile No. : 9340633168',font='Calibri 20 bold',fg='blue').grid(row=8,columnspan=10)
Label(root,text='').grid(row=8,columnspan=10,pady=20)

root.mainloop()

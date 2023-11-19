from tkinter import *
from tkinter.messagebox import *

root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\python_bus.png')          
Label(root,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=3)
Label(root,text='Online Bus Booking System',font='Arial 26 bold',bg='LightBlue',fg='Red').grid(row=1,column=0,columnspan=3)
Label(root,text="Bus Ticket",font='Arial 16 bold').grid(row=2,column=0,columnspan=3,pady=h//40)

cur.execute('select * from bookinghistory')
pp=cur.fetchall()
print(pp)
final = LabelFrame(root)
final.grid(row = 3, column =0, columnspan=3)

passenger_text = Label(final, text = "Passengers: ",font='Arial 11 bold')
passenger_text.grid(row =3, column=0)

seats_text = Label(final, text = "No of seats: ",font='Arial 11 bold')
seats_text.grid(row =4, column=0)

age_text = Label(final, text = "Age: ",font='Arial 11 bold')
age_text.grid(row =5, column=0)

bookingref=Label(final, text = "Booking Ref: ",font='Arial 11 bold')
bookingref.grid(row =6, column=0)

seats_text = Label(final, text = "Travel On:",font='Arial 11 bold')
seats_text.grid(row =7, column=0)

travel_text = Label(final, text = "No of Seats: ",font='Arial 11 bold')
travel_text.grid(row =8, column=0)

g_text = Label(final, text = "Gender: ",font='Arial 11 bold')
g_text.grid(row =3, column=1)

phone_text = Label(final, text = "Phone: ",font='Arial 11 bold')
phone_text.grid(row =4, column=1)

flare_text = Label(final, text = "Flare Rs: ",font='Arial 11 bold')
flare_text.grid(row =5, column=1)

detail_text = Label(final, text = "Bus Detail: ",font='Arial 11 bold')
detail_text.grid(row =6, column=1)

booked_text = Label(final, text = "Booked On: ",font='Arial 11 bold')
booked_text.grid(row =7, column=1)

point_text = Label(final, text = "Boarding Point: ",font='Arial 11 bold')
point_text.grid(row =8, column=1)

last_text = Label(final, text = "Total amount Rs X to br paid at the time of boarding the bus",font="Arial 10 italic")
last_text.grid(row =9, column=1)

showinfo("Success","Seat Booked....")

root.mainloop()

from tkinter import *
from tkinter.messagebox import *
root=Tk()

w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\python_bus.png')
img_home=PhotoImage(file='.\\home.png')
Label(root, image=img).grid(row=0, column=0, columnspan=8, padx=w//3)
title=Label(root,text='Online Bus Booking System', bg='SkyBlue3', fg='Red3', font="Arial 20 bold")
title.grid(row=1, column=0,columnspan=8, padx=w//3)

def home():
    root.destroy()
    import Screen2_Home

ejd=Label(root,text='Enter Journey Details',bg='pale green', fg='forest green', font="Arial 16 bold")
ejd.grid(row=2,column=0,columnspan=10,padx=w//3,pady=25)
to=Label(root,text='To')
From=Label(root,text='From')
jd=Label(root,text='Journey Date')
home=Button(root,image=img_home,bg='light green',command=home)
tof=Entry(root)
Fromf=Entry(root)
jdf=Entry(root)
to.grid(row=3,column=0,sticky=E)
tof.grid(row=3,column=1,sticky=W)
From.grid(row=3,column=2,sticky=E)
Fromf.grid(row=3,column=3,sticky=W)
jd.grid(row=3,column=4,sticky=E)
jdf.grid(row=3,column=5,sticky=W)
home.grid(row=3,column=7)

station_to=tof.get()
station_from=Fromf.get()
journey_date=jdf.get()



def showbus():
    

    t=tof.get()
    f=Fromf.get()
    jdate=jdf.get()
    if (t=="" or f=="" or jdate==""):
        showinfo("Insert Status", "All Fields are required")
    else:
        cur.execute('select t.station_name,f.station_name from route as t , route as f where t.station_name="{}" and f.station_name="{}" and t.station_id<f.station_id'.format(tof.get(),Fromf.get()))
        select_bus=Label(root,text='Select Bus',fg='forest green',font="Arial 13")
        select_bus.grid(row=4,column=1,pady=20)
        operator=Label(root,text='Operator',fg='forest green',font="Arial 13")
        operator.grid(row=4,column=2,pady=20)
        bus_type=Label(root,text='Bus Type',fg='forest green',font="Arial 13")
        bus_type.grid(row=4,column=3,pady=20)
        ava_cap=Label(root,text='Available/Capacity',fg='forest green',font="Arial 13")
        ava_cap.grid(row=4,column=4,pady=20)
        fare=Label(root,text='Fare',fg='forest green',font="Arial 13")
        fare.grid(row=4,column=5,pady=20)
        bus_select=IntVar()
        Radiobutton(root,text='Bus 1',fg='blue2',variable=bus_select,value=1).grid(row=5,column=1)
        cur.execute('select operator_name,bus_type,seat_availabe,capacity,bus_fare,bus_id from operator,bus,route as t ,route as f,runs where operator_id=op_id and t.route_id=r_id and f.route_id=r_id and t.route_id=f.route_id and b_id=bus_id and t.station_name="{}" and f.station_name="{}" and t.station_id<f.station_id'.format(tof.get(),Fromf.get()))                                                                                                                                                                       
        a=cur.fetchall()
       # print(a)
        z1=Label(root,text=a[0][0],fg='blue2',font="Arial 13")
        z1.grid(row=5,column=2)
        z2=Label(root,text=a[0][1],fg='blue2',font="Arial 13")
        z2.grid(row=5,column=3)
        z3=Label(root,text=(str(a[0][2])+'/'+str(a[0][3])),fg='blue2',font="Arial 13")
        z3.grid(row=5,column=4)
        z5=Label(root,text=a[0][4],fg='blue2',font="Arial 13")
        z5.grid(row=5,column=5)
        Radiobutton(root,text='Bus 2',fg='blue2',variable=bus_select,value=2).grid(row=6,column=1)
        y1=Label(root,text=a[2][0],fg='blue2',font="Arial 13")
        y1.grid(row=6,column=2)
        y2=Label(root,text=a[2][1],fg='blue2',font="Arial 13")
        y2.grid(row=6,column=3)
        y3=Label(root,text=(str(a[2][2])+'/'+str(a[2][3])),fg='blue2',font="Arial 13")
        y3.grid(row=6,column=4)
        y5=Label(root,text=a[2][4],fg='blue2',font="Arial 13")
        y5.grid(row=6,column=5) 
        def proceed():
            title1=Label(root,text='Fill Passenger Details to book the bus ticket', bg='SkyBlue3', fg='Red3', font="Arial 20 bold")
            title1.grid(row=7, column=0,columnspan=10, padx=w//3,pady=35)
            name=Label(root,text='Name')
            name.grid(row=8,column=0,sticky=S)
            namef=Entry(root)
            namef.grid(row=8,column=1,sticky=EW)
            gender=Label(root,text='Gender')
            gender.grid(row=8,column=2,sticky=EW)
            gen=StringVar()
            gen.set('Male')
            option=['Male','Female']
            d_menu=OptionMenu(root,gen,*option)
            d_menu.grid(row=8,column=3,sticky=EW)
            no_of_seats=Label(root,text='NO of Seats ')
            no_of_seats.grid(row=8,column=4,sticky=EW)
            nof=Entry(root)
            nof.grid(row=8,column=5,sticky=EW)
            mob=Label(root,text='Mobile No.')
            mob.grid(row=8,column=6,sticky=EW)
            mobf=Entry(root)
            mobf.grid(row=8,column=7,sticky=EW)
            age=Label(root,text='Age')
            age.grid(row=8,column=8,sticky=EW)
            agef=Entry(root)
            agef.grid(row=8,column=9,sticky=W)
            def try1():
                w1=namef.get()
                #dmenu=d_menu.get()
                w2=nof.get()
                w3=mobf.get()
                w4=agef.get()
            
                if bus_select==1:
                    cur.execute('insert into bookinghistory (p_name,p_phone,p_age,travel_date,bid,seat,fare) values("{}","{}","{}","{}","{}","{}","{}")'.format(namef.get(),mobf.get(),agef.get(),jdf.get(),a[0][5],nof.get(),(nof.get()*a[0][4])))
                else:
                    cur.execute('insert into bookinghistory (p_name,p_phone,p_age,travel_date,bid,seat,fare) values("{}","{}","{}","{}","{}","{}","{}")'.format(namef.get(),mobf.get(),agef.get(),jdf.get(),a[2][5],nof.get(),(nof.get()*a[2][4])))
                cur.execute('select * from bookinghistory')
                pp=cur.fetchall()
                print(pp)
            try1()
            def book_seat():
                root.destroy()
                import screen5_BusTicket
            book_seat=Button(root,text='Book Seat', bg='SpringGreen1',command=book_seat)    
            book_seat.grid(row=9,column=8)
        
        pro=Button(root,text='Proceed to Book', bg='SpringGreen1',command=proceed)    
        pro.grid(row=6,column=6)    

sb=Button(root,text='Show Bus', bg='SpringGreen3',command=showbus)    
sb.grid(row=3,column=6)

root.mainloop()


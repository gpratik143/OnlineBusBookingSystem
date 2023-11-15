from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import ImageTk,Image


root=tk.Tk()
root.geometry("400x400")
root.title("First Page")
img=Image.open("python_bus.jpg")
img_resize=img.resize((150,150))
myimg=ImageTk.PhotoImage(img_resize)
label=tk.Label(root,image=myimg)
label.pack(pady=20)
#Label 1 = Online Bus booking system
label1_font=font.Font(weight="bold")
label1=tk.Label(root,text="Online Bus Booking System",font=label1_font,fg="red")
label1.pack(pady=10)
#Label 2 = Name
label2=tk.Label(root,text=" Name: Pratik Gupta",fg="dark blue")
label2.pack(pady=5)
#Label 3= Enrollment 
label3=tk.Label(root,text="Er No: 221B276",fg="dark blue")
label3.pack(pady=5)
#label 4 = Mobile no
label4=tk.Label(root,text="Mobile No: 9340633168",fg="dark blue")
label4.pack(pady=5)
#label 5 = Submitted 
label5=tk.Label(root,text="Submitted To: Dr Mahesh Kumar",fg="dark blue")
label5.pack(pady=8)
#label 6= Project based learning
label5=tk.Label(root,text="Project Based Learning",fg="Red")
label5.pack(pady=3)
root.mainloop()
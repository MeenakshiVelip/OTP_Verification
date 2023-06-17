import tkinter.messagebox as tsmg 
from tkinter import *
import requests 
import random
import json
import smtplib
root=Tk()

rand=random.randint(1,999999)
otp1=rand
otp2=rand
msg=f"Your One Time Password(OTP) is {rand}"

def sms_send1(a,msg):
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"nlwqrxkDOiLP0p8NeQ6YRXcGhvVg7H2JTIMa9s4UBFKyZ5AbzfFT2Esng3ub79vNHDRXoBYktm1hrAUL",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":a
    }
    rs=requests.get(url,params=params)
    
def sms_send2(emailid):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
    server.starttls()
    server.login("meenakshivelip5@gmail.com", "wkgqsqmcykvuggof")

    server.sendmail("&&&&&&&&&&&", emailid, msg)

    server.quit()


def send1():
    a=num1.get()
    if(a==""):
        tsmg.showerror("Error","Enter Your Mobile Number")
       
    elif (len(a)<10):
        tsmg.showerror("Error","Invalid Mobile Number")
        
        num1.set("")
    else:

        b=tsmg.askyesno("Info",f"Your Mobile Number is {a}")
        
        if(b==True):
            sms_send1(a,msg)
        else:
            num1.set("")

def send2():
    a = num2.get()
    if (a == ""):
        Message.showerror("Error", "Enter YOUR EMAIL ID")
    elif (len(a) < 10):
        tsmg.showerror("Error", "Invalid EMAIL ID")
        num2.set("")
    else:

        b = tsmg.askyesno("Info", f"Your EMAIL ID is {a}")
        if (b == True):
            sms_send2(a)
        else:
            num2.set("")
            
def check1():
    c=otp1.get()
    if(c==""):
        tsmg.showerror("Error","Enter OTP")
    else:
        if(str(rand)==c):
            tsmg.showinfo("Info","OTP Verification is Successful")
        else:
            tsmg.showerror("Error","Invalid OTP")
            num1.set("")
            otp1.set("")

def check2():
    c=otp2.get()
    if(c==""):
        tsmg.showerror("Error","Enter OTP")
    else:
        if(str(rand)==c):
            tsmg.showinfo("Info","OTP Verification is Successful")
        else:
            tsmg.showerror("Error","Invalid OTP")
            num2.set("")
            otp2.set("")


root.geometry("500x500")
root.title("KLS VDRIT HALIYAL")

num1=StringVar()
num2=StringVar()
otp1=StringVar()
otp2=StringVar()

f1=Frame(root)
Label(f1,text=" OTP GENERATION AND VERIFICATION SYSTEM",font="SegoeUI 20 bold",fg="BLACK").pack(padx=5,pady=10)
f1.pack(fill=BOTH)

f2=Frame(root)
Label(f2,text="ENTER YOUR MOBILE NUMBER",font="SegoeUI 10 bold",fg="GREEN").pack(padx=5,pady=5)
e1=Entry(f2,textvariable=num1,font="SegoeUI 14 bold",fg="black",bg="grey",relief=SUNKEN,borderwidth=4,justify="center").pack(ipady=5)
f2.pack(fill=BOTH,padx=5,pady=10)

f7=Frame(root)
Button(f7,text="SEND OTP",command=send1,font="SegoeUI 10 bold",fg="Black").pack(padx=20,pady=10,side=LEFT)
f7.pack()

f6=Frame(root)
Label(f6,text="ENTER YOUR EMAIL ID",font="SegoeUI 10 bold",fg="GREEN").pack(padx=5,pady=5)
e3=Entry(f6,textvariable=num2,font="SegoeUI 14 bold",fg="black",bg="grey",relief=SUNKEN,borderwidth=4,justify="center").pack(ipady=5)
f6.pack(fill=BOTH,padx=5,pady=10)

f7=Frame(root)
Button(f7,text="SEND OTP",command=send2,font="SegoeUI 10 bold",fg="Black").pack(padx=20,pady=10,side=LEFT)
f7.pack()

f8=Frame(root)
Label(f8,text="Enter OTP",font="SegoeUI 10 bold",fg="GREEN").pack(padx=5,pady=5)
e4=Entry(f8,textvariable=otp2,font="SegoeUI 14 bold",fg="black",bg="grey",relief=SUNKEN,borderwidth=5,justify="center").pack(ipady=5)
f8.pack(fill=BOTH,padx=5,pady=10)

f9=Frame(root)
Button(f9,text="VERIFY OTP",command=check2,font="SegoeUI 10 bold",fg="Black").pack(padx=40,pady=10,side=LEFT)
f9.pack()

f10=Frame(root)
Label(f10,text=" THANK YOU ",font="SegoeUI 20 bold",fg="navy").pack(padx=5,pady=10)
f10.pack(fill=BOTH)


root.mainloop()

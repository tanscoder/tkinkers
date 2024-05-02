

import tkinter as tk

deftxt="enter your number"


def funct():
    n = enter.get()
    global n1
    global c
    c=0
    n1=""
    for i in n:
        if ord(i) in range (48, 58):
            i=str(i)
            n1+=i
            c+=1
            continue
        else:
            subhead.config(text="Please enter your phone number only ie, numerics only")
            enter.delete(0,tk.END)
    mainfct(n)
k="""def mainfct(num):
       if c==10:
         subhead.config(text="sucessful!")
       else:
           subhead.config(text="Please enter all the numbers")

"""
def mainfct(num):
    global c
    if c == 10:
        subhead.config(text="Successful!")
    else:
        subhead.config(text="Please enter exactly 10 numeric digits")

# ... (rest of your code remains unchanged)


def onclick(n):
    if enter.get()==deftxt:
        enter.delete(0,tk.END)
        enter.config(fg="black")
def noclick(n):
    if enter.get()=="":
        enter.insert(0,deftxt)
        enter.config(fg="grey")


prog=tk.Tk()

title=prog.title("Number guessing program")

geos=prog.geometry("500x500")

head=tk.Label(prog,text="Enter your phone number",bg="#40E0D0")
head.pack(pady=70)

subhead=tk.Label(prog,text="Enter main part of the phone number only")
subhead.pack(pady=10)

enter=tk.Entry(prog,fg="grey")
enter.pack(pady=70)

enter.insert(0,deftxt)
enter.bind("<FocusOut>",noclick)
enter.bind("<FocusIn>",onclick)
buton=tk.Button(text="Enter",command=funct)
buton.pack(pady=50)
prog.mainloop()









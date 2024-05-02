
import tkinter as tk

deftxt=("Enter your value")

def BUTTON():
   global clc
   clc=0
   n=entr.get()
   for i in n:
    if ord(i) in range(48,58): #type(n)==int :
       c=True
       continue
    elif ord(i) not in range(48,58) :
       c=0
       clc=False
       heading.config(text=f"invalid letter {i} found, enter numbers only")
       break
   n=int(n)
   l.config(text=f"Your answer is = {n * 50}", bg="#40E0D0", font=("Times Roman", 20))
   countdown(60)
def countdown(n):
  if clc==True:
    if n>=0:
        heading.config(text=f"This window will close in {n} seconds",bg="light blue")
        win.after(1000,lambda :countdown(n-1))
    else:
        des()
  else:
      return ""
def des():
    win.destroy()

def onclick(event):

  if entr.get()==deftxt:
    entr.delete(0,tk.END)
    entr.config(fg="black")




def notclick(event):
  if entr.get()=="":

    entr.insert(0,deftxt)
    entr.config(fg="grey")



win = tk.Tk()                                                                                                                 # "Window defining"



win.title("Tinkter.window")
win.geometry("5000x3500")

heading = tk.Label(win,text="Welcome to Tkinter test",fg="black",bg="#40E0D9")           #   #40E0D0 Is the hex for turqouise

heading.pack(pady=100)
                                                                                         #   #       Is the hex for turquoise
l = tk.Label(win,text="helo there!",font=("Ariel",20))

l.pack(pady=10)

button = tk.Button(win,text="Click here",command=BUTTON,bg="black",fg="light blue",font=("Times Roman",10))

button.pack(pady=100)#,side=tk.BOTTOM,anchor=tk.CENTER,expand=True)

entr=tk.Entry(win,fg="grey",font=("Ariel",25))

entr.pack(pady=20)

commented2="""entr2=tk.Entry()
entr2.pack()"""



entr.insert(0,deftxt)
entr.bind("<FocusIn>",onclick)
entr.bind("<FocusOut>",notclick)


sym="""symbol=tk.Entry()

symbol.pack(pady=10)"""
                             #side=tk.BOTTOM







win.mainloop()









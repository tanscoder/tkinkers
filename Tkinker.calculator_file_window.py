import tkinter as tk



deftxt="Enter your value here"
def onclick():
     if digit1 == deftxt :
         digit1.delete(0,tk.END)
         digit1.config(fg="black")

def ofclick():
    if digit1 == "":
        digit1.insert(0,deftxt)
        digit1.config(fg="grey")
#digit
global n

def butclick(n):

    if ord(n) in range (48,58):
        n=str(n)
        n1=0
    #row=1
    #column=0
    #for i in keypad:
     #   if column > 3:
      #      return


calci=tk.Tk()
window_title=calci.title("Calculator.userTANS")
background_set=calci.config(bg="#6bb7f0")#"#40E0D0")
calci.geometry("5000x5000")

head1=tk.Label(text="Click enter button after entering your number",bg="pink",fg="black")#6bb7f0")
head1.pack(pady=100)

digit1=tk.Entry(fg="grey")
digit1.bind("<inFocus>",onclick())
digit1.bind("<outFocus>",ofclick())
digit1.pack(pady=100)


but=tk.Button(text="Enter",command=butclick())
but.pack()

key1=tk.button(text="1",command=digit(1))



keypad=[
    "1" , "2" , "3",
    "4" , "5" , "6",
    "7" , "8" , "9",
    "+" , "0" , "-",
    "/" , "x" , ")",
          "(",

      ]




#lbl=tk.Label(text=keypad)
#lbl.pack(pady=10)
calci.mainloop()
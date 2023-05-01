from tkinter import *
from datetime import *
root = Tk()
root.title("My Second app ")
root.geometry("400x200+100+400")
root.configure(bg="azure")
f = ("Simsun",40,"bold")
d = datetime.now().time()
hr = d.hour
if hr<12 :
    msg ="Good Morning "
elif hr<16 :
    msg =" Good afternoon "
else:
    msg = " Good evening "

lab = Label(root,text=msg.title(),font=f , bg="azure")
lab.pack(pady=30)
root.mainloop()
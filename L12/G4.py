from tkinter import *
from random import *


root = Tk()
root.title("Mohe rang de 2 ")
root.geometry("500x300+100+100")

def color():
    names =["red","black","green","pink","blue","yellow"]
    r = randrange(len(names))
    root.configure(bg=names[r])
f = ("Arial",30,"bold")
btn =Button(root,text="Color Me",font=f,command=color)
btn.pack(pady=30)

root.mainloop()

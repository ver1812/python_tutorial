from tkinter import *
from random import *
from time import *


root = Tk()
root.title("Mohe rang de 2 ")
root.geometry("500x300+100+100")

def color():
    names =["red","black","green","pink","blue","yellow"]
    r = randrange(len(names))
    root.configure(bg=names[r])
    root.after(2000,color)

color()
root.mainloop()







root.mainloop()

from tkinter import *
root = Tk()

root.title("My First App ")
root.geometry("800x100+500+300")
f = ("Arial",50,"bold","italic")
lab = Label(root,text="Good evening ",font =f,fg="red")
lab.pack(pady=20)
root.mainloop()
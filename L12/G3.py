from tkinter import *
root =Tk()
root.title("Mohe rang de")
root.geometry("500x500+50+50")
f= ("Calibri",30,"bold")
def f1():
    root.configure(bg="red")
def f2():
    root.configure(bg="green")
def f3():
    root.configure(bg="Blue")
btn_red = Button(root,text="Red",font=f,width=10,bg="azure",fg ="Black",command=f1)
btn_green = Button(root,text="Green",font=f,width=10,bg="azure",fg ="Black",command=f2)
btn_blue = Button(root,text="Blue",font=f,width=10,bg="azure",fg ="Black",command=f3)


btn_red.pack(pady=20)
btn_green.pack(pady=20)
btn_blue.pack(pady=20)

root.mainloop()
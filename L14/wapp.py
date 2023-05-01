from tkinter import * 
from tkinter.messagebox import *
from sqlite3 import *

root =Tk()
root.title("Whats next app ")
root.geometry("900x500+50+50")
f= ("Simsun",30,"bold")

lab_name = Label(root,text="Enter name ",font=f)
ent_name =Entry(root,font=f)
lab_name.place(x=20,y=20)
ent_name.place(x=320,y=20)

s = IntVar()
s.set(1)
lab_select =Label(root,text="Select any one",font=f)
rb_job = Radiobutton(root,text="Job",font=f,variable=s,value=1)
rb_ms = Radiobutton(root,text="MS",font=f,variable=s,value=2)
rb_mba= Radiobutton(root,text="MBA",font=f,variable=s,value=3)
lab_select.place(x=20,y=100)
rb_job.place(x=320,y=100)
rb_ms.place(x=320,y=170)
rb_mba.place(x=320,y=240)

def save():
    con = None
    try:
        con =connect("wn.db")
        cursor =con.cursor()
        sql ="insert into student values('%s','%s')"
        name = ent_name.get()
        choice =""
        if s.get()==1:
            choice="Job"
        elif s.get()==2:
            choice="MS"
        else:
            choice="MBA"
        cursor.execute(sql % (name,choice))
        con.commit()
        showinfo("Success","Thanks")
    except Exception as e:
        showerror("issue ",e)
        con.rollback()
    finally:
        if con is not None:
            con.close()
        ent_name.delete(0,END)
        s.set(1)
        ent_name.focus()
btn_save =Button(root,text="Save",font=f,command=save)
btn_save.place(x=320,y=320)
root.mainloop()


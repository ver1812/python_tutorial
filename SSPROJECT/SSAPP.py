from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *

root = Tk()
root.title("Success Stories ")
root.geometry("500x700+50+50")
f = ("Arial", 30, "bold")

lab_name = Label(root, text="Enter name ", font=f)
ent_name = Entry(root, font=f)
lab_name.pack(pady=10)
ent_name.pack(pady=10)

lab_company = Label(root, text="Enter Company ", font=f)
ent_company = Entry(root, font=f)
lab_company.pack(pady=10)
ent_company.pack(pady=10)

lab_pkg = Label(root, text="Enter pkg", font=f)
ent_pkg = Entry(root, font=f)
lab_pkg.pack(pady=10)
ent_pkg.pack(pady=10)


def save():
    con = None
    try:
        con = connect("v.db")
        cursor = con.cursor()
        sql = "insert into student values ('%s','%s','%d')"
        name = ent_name.get()
        company = ent_company.get()
        pkg = float(ent_pkg.get())
        cursor.execute(sql % (name, company, pkg))
        con.commit()
        showinfo("Success", "Saved")
    except Exception as e:
        con.rollback()
        showinfo("issues ", str(e))
    finally:
        if con is not None:
            con.close()
        ent_name.delete(0,END)
        ent_company.delete(0,END)
        ent_pkg.delete(0,END)
        ent_name.focus()


btn_save = Button(root, text="Save", font=f, command=save)
btn_save.pack(pady=10)
root.mainloop()

# Vighnesh Arun Sadvilkar
# Internship project 
# Employee Record Management System implemented using Python's tkinter
# GUI , SQLite database and matplotlib
# CRUD system



from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import matplotlib.pyplot as plt


try:
    wa = "https://ipinfo.io/"
    res = requests.get(wa)
    data = res.json()
    loc = data["city"]
    a1 = "https://api.openweathermap.org/data/2.5/weather"
    a2 = "?q=" + loc
    a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
    a4 = "&units=" + "metric"
    wb = a1 + a2 + a3 + a4
    r = requests.get(wb)
    x = r.json()
    temp = x["main"]["temp"]

except Exception as e:
    print("issue", e)


def f1():
    mw.withdraw()
    aw.deiconify()


def f2():
    aw.withdraw()
    mw.deiconify()


def f3():
    mw.withdraw()
    vw.deiconify()
    vw_st_data.delete(1.0, END)
    con = None
    try:
        con = connect("er.db")
        cursor = con.cursor()
        sql = "select * from employee"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info + " ID :  " + str(d[0]) + "  |  Name =  " + str(d[1]) + "  | Salary = Rs " + str(d[2]) + "\n"
        vw_st_data.insert(INSERT, info)
    except Exception as e:
        showerror("issue ", e)
    finally:
        if con is not None:
            con.close()


        if con is not None:
            con.close()



def f4():
    vw.withdraw()
    mw.deiconify()


def f5():
    mw.withdraw()
    uw.deiconify()


def f6():
    uw.withdraw()
    mw.deiconify()


def f7():
    mw.withdraw()
    dw.deiconify()


def f8():
    dw.withdraw()
    mw.deiconify()


def f9():
    con = None
    try:
        con = connect("er.db")
        cursor = con.cursor()
        sql = "insert into employee values('%d','%s','%d')"
        ID = aw_ent_ID.get()
        name = aw_ent_name.get()
        salary = aw_ent_salary.get()
        
        if not ID or not ID.isdigit() or int(ID) <= 0:
            showerror("Invalid ID", "ID should not be empty and contain only a positive integer.")
            return

        if not name or not name.isalpha() or len(name) < 2:
            showerror("Invalid Name", "Name should only contain alphabets with a minimum length of 2.")
            return
        if not salary or not salary.isdigit() or float(salary) < 8000:
            showerror("Invalid Salary", "Salary should be a minimum of 8K.")
            return
        ID = int(aw_ent_ID.get())
        salary = float(aw_ent_salary.get())
    
        cursor.execute(sql % (ID, name, salary))
        con.commit()
        showinfo("Success", "info saved")
    except Exception as e:
        showerror("issue ", e)
    finally:
        if con is not None:
            con.close()
        aw_ent_ID.delete(0, END)
        aw_ent_name.delete(0, END)
        aw_ent_salary.delete(0, END)
        aw_ent_ID.focus()

def f10():
    con = None
    try:
        con = connect("er.db")
        cursor = con.cursor()
        
        sql = "update employee set name='%s',salary='%d' where ID='%d'"
        
        ID = uw_ent_ID.get()
        name = uw_ent_name.get()
        salary = uw_ent_salary.get()

        if not ID:
            showerror("Invalid Input", "ID cannot be empty.")
            return
        if not name:
            showerror("Invalid Input", "Name cannot be empty.")
            return
        if not salary:
            showerror("Invalid Input", "Salary cannot be empty.")
            return
        if not ID.isdigit() or int(ID) <= 0:
            showerror("Invalid ID", "ID should not be empty and contain only a positive integer.")
            return

        if  not name.isalpha() or len(name) < 2:
            showerror("Invalid Name", "Name should only contain alphabets with a minimum length of 2.")
            return
        if  not salary.isdigit() or float(salary) < 8000:
            showerror("Invalid Salary", "Salary should be a minimum of 8K.")
            return
        
        ID = int(ID)
        salary = float(salary)

        
        
        cursor.execute(sql % (name,salary,ID))
        if cursor.rowcount == 1:
            con.commit()
            showinfo("Success", "info Updated")
        else:
            showerror("Invalid ID", "ID does not exist.")
            return



    except Exception as e:
        con.rollback()
        print("issue ", e)
    finally:
        if con is not None:
            con.close()
            uw_ent_ID.delete(0, END)
            uw_ent_name.delete(0, END)
            uw_ent_salary.delete(0, END)
            uw_ent_ID.focus()

def f11():
    con = None
    try:
        con = connect("er.db")
        cursor = con.cursor()
        sql = "DELETE FROM employee where ID='%d'"
        ID = dw_ent_ID.get()
        if not ID.isdigit() or int(ID) <= 0:
            showerror("Invalid ID", "ID should not be empty and contain only a positive integer.")
            return
        ID = int(ID)
        cursor.execute("SELECT * FROM employee WHERE ID = ?", (ID,))
        row = cursor.fetchone()
        if row is None:
            showerror("Invalid ID", "ID does not exist.")
            return
        cursor.execute(sql % (ID))
        con.commit()
        showinfo("Success", "info Deleted")
    except Exception as e:
        con.rollback()
        print("issue ", e)
    finally:
        if con is not None:
            con.close()
            dw_ent_ID.delete(0, END)


def f12():
    conn = connect('er.db')
    c = conn.cursor()

    
    c.execute('''SELECT name, salary FROM employee
                ORDER BY salary DESC
                LIMIT 5''')
    data = c.fetchall()

    
    names = [row[0] for row in data]
    salaries = [row[1] for row in data]

    
    plt.bar(names, salaries)
    plt.xlabel('Employee Name')
    plt.ylabel('Salary')
    plt.title('Top 5 Employees by Salary')

    
    plt.show()

    
    conn.close()



mw = Tk()
mw.title("E.M.S")
mw.geometry("700x700+50+50")
f = ("Simsun", 30, "bold")
mw.configure(background="light green")
mw_btn_add = Button(mw, text="Add ", font=f, width=15, command=f1)
mw_btn_view = Button(mw, text="View ", font=f, width=15, command=f3)
mw_btn_update = Button(mw, text="Update ", font=f, width=15, command=f5)
mw_btn_delete = Button(mw, text="Delete ", font=f, width=15, command=f7)
mw_btn_charts = Button(mw, text="Charts ", font=f, width=15, command=f12)
mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_charts.pack(pady=10)
mw_loc = Label(mw, text=(("Location:", loc, "Temp:", temp)), background="light green", font=f)
mw_loc.pack(pady=10)

aw = Toplevel(mw)
aw.title("Add Employee ")
aw.geometry("500x600+50+50")
aw.configure(background="light blue")
aw_lab_ID = Label(aw, text="Enter ID ", font=f)
aw_ent_ID = Entry(aw, font=f)
aw_lab_name = Label(aw, text="Enter Name ", font=f)
aw_ent_name = Entry(aw, font=f)
aw_lab_salary = Label(aw, text="Enter Salary ", font=f)
aw_ent_salary = Entry(aw, font=f)
aw_btn_save = Button(aw, text="save", font=f, command=f9)
aw_btn_back = Button(aw, text="Back ", font=f, command=f2)

aw_lab_ID.pack(pady=10)
aw_ent_ID.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
aw.withdraw()

vw = Toplevel(mw)
vw.title("View Employee ")
vw.geometry("750x550+50+50")
vw.configure(background="light yellow")
vw_st_data = ScrolledText(vw, width=38, height=12, font=f)
vw_btn_back = Button(vw, text="Back", font=f, command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.withdraw()

uw = Toplevel(mw)
uw.title("Update Employee ")
uw.geometry("500x600+50+50")
uw.configure(background="light coral")
uw_lab_ID = Label(uw, text="Enter ID ", font=f)
uw_ent_ID = Entry(uw, font=f)
uw_lab_name = Label(uw, text="Enter Name ", font=f)
uw_ent_name = Entry(uw, font=f)
uw_lab_salary = Label(uw, text="Enter Salary ", font=f)
uw_ent_salary = Entry(uw, font=f)
uw_btn_save = Button(uw, text="save", font=f, command=f10)
uw_btn_back = Button(uw, text="Back ", font=f, command=f6)

uw_lab_ID.pack(pady=10)
uw_ent_ID.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
uw.withdraw()

dw = Toplevel(mw)
dw.title("Delete Employee ")
dw.geometry("500x500+50+50")
dw.configure(background="light blue")
dw_lab_ID = Label(dw, text="Enter ID ", font=f)
dw_ent_ID = Entry(dw, font=f)
dw_btn_save = Button(dw, text="Delete", font=f,command=f11)
dw_btn_back = Button(dw, text="Back ", font=f, command=f8)

dw_lab_ID.pack(pady=10)
dw_ent_ID.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)
dw.withdraw()


def windowclose():
    if askyesno("Quit", "Close ?"):
        mw.destroy()


mw.protocol("WM_DELETE_WINDOW", windowclose)

mw.mainloop()



# Complete Structure
# Create database --
# Add and View functions --
# Update Function  --
# Delete Function  --
# Charts
# Validations 
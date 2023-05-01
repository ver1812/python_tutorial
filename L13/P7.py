from sqlite3 import *
con = None
try:
    con = connect("kc.db")
    cursor = con.cursor()
    sql= "update student set name='%s',marks='%d' where rno='%d'"
    rno = int(input("enter rno "))
    name = input("enter name ")
    marks = int(input("enter marks "))
    cursor.execute(sql%(name,marks,rno))
    if cursor.rowcount==1:
        con.commit()
        print("Updated")
    else:
        print("Does not exists ")


except Exception as e :
    con.rollback()
    print("issue ",e)
finally:
    if con is not None:
        con.close()
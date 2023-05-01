from sqlite3 import *
con = None
try:
    con = connect("kc.db")
    cursor = con.cursor()
    sql= "insert into student values ('%d','%s','%d')"
    rno = int(input("enter rno "))
    name = input("enter name ")
    marks = int(input("enter marks "))
    cursor.execute(sql%(rno,name,marks))
    con.commit()
except Exception as e :
    con.rollback()
    print("issue ",e)
finally:
    if con is not None:
        con.close()
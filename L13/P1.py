#wapp to insert emp record
from sqlite3 import *
con = None
try:
    con = connect("kit.db")
    cursor = con.cursor()
    sql = "insert into emp values ('%d','%s')"
    id = int(input("enter emp id "))
    name = input("enter emp name ")
    cursor.execute(sql % (id,name))
    con.commit()
    print("Record accepted ")
except Exception as e:
    con.rollback()
    print("issue ",e)
finally:
    if con is not None:
        con.close()
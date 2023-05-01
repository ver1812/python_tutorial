#wapp to insert student record

from sqlite3 import *
con = None
try:
    con = connect("kc.db")
    cursor = con.cursor()
    sql= "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data :
        print("rno:",d[0],"name:",d[1],"marks:",d[2])
        

except Exception as e :
    con.rollback()
    print("issue ",e)
finally:
    if con is not None:
        con.close()
#wapp to view emp records
from sqlite3 import *
con = None
try:
    con = connect("kit.db")
    cursor = con.cursor()
    sql = "select * from emp"
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data :
        print("ID= ",d[0],"Name = ",d[1])
except Exception as e :
    print("issues ",e)
finally:
    if con is not None:
        con.close()

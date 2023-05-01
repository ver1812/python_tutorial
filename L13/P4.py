#wapp to view book
from sqlite3 import *
con = None
try:
    con = connect("kb.db")
    cursor = con.cursor()
    sql ="select * from book"
    cursor.execute(sql)
    data = cursor.fetchall()
    print("Record fetched")
    for d in data:
        print("bid",d[0],"title:",d[1],"author:",d[2],"price",d[3])
except Exception as e:
    con.rollback()
    print("issue",e)
finally:
    if con is not None:
        con.close()

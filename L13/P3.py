#wapp to create book records

from sqlite3 import *
con = None
try:
    con = connect("kb.db")
    cursor = con.cursor()
    sql ="insert into book values('%d','%s','%s','%f')"
    bid = int(input("Enter bid "))
    title = input("enterbook title ")
    author = input("enter author name ")
    price = float(input("Enter price "))
    cursor.execute(sql % (bid,title,author,price))
    con.commit()
    print("Record created")
except Exception as e:
    con.rollback()
    print("issue",e)
finally:
    if con is not None:
        con.close()

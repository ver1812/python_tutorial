# wapp to create employee record
from pymongo import *

con = None
try:
    con = MongoClient("localhost", 27017)
    db = con["kit_3feb23"]
    coll = db["employee"]

    i = int(input("Enter emp id "))
    count = coll.count_documents({"_id": i})
    if count == 1:
        print(i, "already exists ")
    else:
        name = input("enter name ")
        salary = float(input("Enter salary "))
        info = {"_id": i, "name": name, "salary": salary}
        coll.insert_one(info)
        print(i, "Created ")


except Exception as e:
    print("issue", e)

finally:
    if con is not None:
        con.close()

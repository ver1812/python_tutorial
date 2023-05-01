#wapp to create dept
from pymongo import *
con = None
try:
    con = MongoClient("127.0.0.1", 27017)
    db = con["kc_3feb23"]
    coll = db["dept"]

    i = int(input("Enter dept id "))
    count = coll.count_documents({"_id": i})
    if count == 1:
        print(i, "already exists ")
    else:
        name = input("enter dept name ")

        info = {"_id": i, "name": name}
        coll.insert_one(info)
        print(i, "Created ")


except Exception as e:
    print("issue", e)

finally:
    if con is not None:
        con.close()
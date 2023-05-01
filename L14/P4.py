from pymongo import *

con = None
try:
    con = MongoClient("127.0.0.1", 27017)
    db = con["kc_3feb23"]
    coll = db["dept"]

    data = coll.find()
    for d in data :
        print(d)


except Exception as e:
    print("issue", e)

finally:
    if con is not None:
        con.close()

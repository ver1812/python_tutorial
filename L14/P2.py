from pymongo import *

con = None
try:
    con = MongoClient("localhost", 27017)
    db = con["kit_3feb23"]
    coll = db["employee"]

    data = coll.find()
    for d in data :
        print(d)


except Exception as e:
    print("issue", e)

finally:
    if con is not None:
        con.close()

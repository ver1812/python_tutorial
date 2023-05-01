# firebase

import pyrebase
from datetime import *

firebaseConfig = {
    "apiKey": "AIzaSyBRj2UFR_ht7IYI-90TW0NiL_2JcOxPkUI",
    "authDomain": "pyfb9thfeb23.firebaseapp.com",
    "databaseURL": "https://pyfb9thfeb23-default-rtdb.firebaseio.com",
    "projectId": "pyfb9thfeb23",
    "storageBucket": "pyfb9thfeb23.appspot.com",
    "messagingSenderId": "235041154933",
    "appId": "1:235041154933:web:88a52c59b918ae5c60953c"
}

fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()
print(db)

name = input("Enter ur name ")
feedback = input("enter ur feedback  ")
info = {"name": name, "feedback":feedback, "dt": str(datetime.now())}
db.child("feedback").push(info)
print("thanks")
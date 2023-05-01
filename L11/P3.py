# append existing file
import os
filename = input(" Enter filename ")
if os.path.exists(filename):
    try:
        with open(filename, "a") as f:
            data = input("enter data ")
            f.write(data +"/n")
    except Exception as e:
        print("issues ",e)
else:
    print(filename,"does not exists ")
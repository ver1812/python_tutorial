#create a new file
import os
filename = input("Enter name ")
if os.path.exists(filename):
    print(filename," Already exists ")
else:
    try:
        with open(filename, "w") as f:
            print(filename," Created ")
    except Exception as e:
        print("issue ",e)
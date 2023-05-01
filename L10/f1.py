#wapp to create new file
import os
filename = input("Enter filename")
if os.path.exists(filename):
    print(filename)
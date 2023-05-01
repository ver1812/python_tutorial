#delete existing file
import os
filename = input("Enter filename ")
if os.path.exists(filename):
    os.remove(filename)
    print(filename,"removed ")
else:
    print(filename," does not exists ")
    
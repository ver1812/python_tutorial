#wapp to copy file
import os
src_filename = input("Enter source filename ")
if os.path.exists(src_filename):
    dest_filename =input("Enter destination filename ")
    try:
        with open(src_filename,"r") as sf:
            with open(dest_filename,"w")as df:
                data = sf.read()
                df.write(data)
                print(" COPY completed ")
    except Exception as e:
        print("issue ",e)
else:
    print(src_filename," filename does not exist ")
email = set()
res = input("Do you want to enter more ? y/n ")
while res=="y" :
    e = input("enter ")
    r1 = len(email)
    email.add(e)
    r2= len(email)
    if r2>r1 :
        print("added")
    else:
        print("already exists ")
    res = input("Do you want to enter more ? y/n ")
print(email)
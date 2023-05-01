# wapp to read email address from user
email = set()
res = input("Do you want to enter more ? y/n ")
while res=="y" :
    e = input("enter ")
    email.add(e)
    res = input("Do you want to enter more ? y/n ")
print(email)

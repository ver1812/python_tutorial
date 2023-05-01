#wapp to read a string and count
data = input("Enter string")
c1,c2 = 0,0

for d in data :
    if d.isupper()     :
        c1= c1+1
    elif d.islower()  :
        c2 = c2 +1
print("C2 = ",c2)
print("C1 = ",c1)
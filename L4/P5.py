data = input("enter a string")
c1,c2 = 0,0

for d in data :
    if d.isalpha()   :
        c1 = c1+1
    elif d.isdigit() :
        c2= c2+1

print("c1 = ",c1)
print("c2 = ",c2)

#wapp to read tuple numbers from user
#print in desc

data =()
res = input("y : yes , n: no ")
while res == "y":
    d = float(input("enter data "))
    data = data + (d,)
    res = input("do you want to enter more y/n ")
# desc order
ndata = tuple(sorted(data , reverse = True))
print(data)
print(ndata)

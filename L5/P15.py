#wapp to sort string
def mysort(s):
    d= sorted(s)
    ns = "".join(d)
    return ns
data = input("enter string")
ndata = mysort(data)
print("org = ",data)
print("sorted = ",ndata)
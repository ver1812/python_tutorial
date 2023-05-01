#wapp to find factorial

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("Enter no"))
if n>= 0:
    f = factorial(n)
    print("fact = ",f)
else:
    print("Invalid")
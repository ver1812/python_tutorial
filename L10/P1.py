#wapp to add two integers
#try with single except
print("good Evening")
try:
    n1 = int(input('enter number '))
    n2 = int(input('enter number '))
    res = n1 + n2
    print(res)
except ValueError :
    print("You need to enter integer only ")
print("Bye")


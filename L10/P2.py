#try with single except and else
print("good Evening")
try:
    n1 = int(input('enter number '))
    n2 = int(input('enter number '))

except ValueError :
    print("You need to enter integer only ")
else :
    res = n1 + n2
    print(res)
print("Bye")

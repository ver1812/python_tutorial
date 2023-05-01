#try with multiple except
print("good Evening")
try:
    n1 = int(input('enter number '))
    n2 = int(input('enter number '))
    ans = a/b
    print(ans)

except ValueError :
    print("You need to enter integer only ")
except ZeroDivisionError :
    print("2 nd integer should not be 0 ")

print("Bye")

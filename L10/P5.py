print("good Evening")
try:
    n1 = int(input('enter number '))
    n2 = int(input('enter number '))
    ans = n1 / n2


except ValueError:
    print("You need to enter integer only ")
except ZeroDivisionError:
    print("2 nd integer should not be 0 ")
else:
    print(ans)
print("Bye")

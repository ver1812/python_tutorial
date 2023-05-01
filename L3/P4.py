#wapp to find sum of N +ve numbers

num = int(input("enter +ve number "))
if num > 0 :
	i=1
	sum = 0
	while i<= num :
		sum = sum + i
		i= i+1
	print("Sum = ",sum)
else :
	print("Invalid")
#wapp factorial
num = int(input("enter +ve number "))
if num > 0 :
	i=1
	fact = 1
	while i<= num :
		fact= fact* i
		i= i+1
	print("fact = ",fact)
else :
	print("Invalid")
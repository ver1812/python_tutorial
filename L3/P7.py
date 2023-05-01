num = int(input("Enter +ve int"))
if num >= 0:
	i,fact = 1,1

	while i<= num :
		fact*=i
		i+=1

	print("fact =", fact)
else :
	print("invalid input")

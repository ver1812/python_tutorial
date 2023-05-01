#wapp to read first three letter day and print if its a weekday or weekend
day = input("Enter day ")
if (day=="mon") or (day=="tue") or (day=="wed") or (day=="thu") or (day=="fri") :
	print("Its weekday")
elif (day=="sat") or (day=="sun"):
	print("Its weekend")
else:
	print("invalid")
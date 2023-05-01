#wapp to check if person can donate blood 
age =float(input("Enter age"))
wt= float(input("Enter weight"))
if (age>24) and(wt>59) :
	print("Person can donate")
else :
	print("person cannot donate ")
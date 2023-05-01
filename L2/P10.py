#wapp to read 3 numbers and print max of 3
n1= int(input("Enter no"))
n2= int(input("Enter no"))
n3= int(input("Enter no"))

if(n1>n2) and(n1>n3):
	print("Biggest number is ",n1)
elif(n2>n1) and (n2>n3):
	print("Biggest number is ",n2)
else :
	print("Biggest number is ",n3)
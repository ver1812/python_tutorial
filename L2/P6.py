#wapp to read amount i dollars and 
#convert in rupees
dollars = float(input("Enter amount in dollars "))
if dollars> 0.0 :
	rupees = dollars * 81.2
	print("amount is ",round(rupees,2) ," in rupees" ,sep="  ")
else:
	print("Invalid")

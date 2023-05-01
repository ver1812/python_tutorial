m= int(input("Enter Marks"))
if (m<0) or(m>100):
	print("invalid marks")
elif m>80:
	print("Grade A ")
elif m>60:
	print("Grade B ")
elif m>40:
	print("Grade C ")
else:
	print("Grade D ")

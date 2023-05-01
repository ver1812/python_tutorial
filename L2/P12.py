rating = int(input("enter rating"))

match rating:
	case 5|4: print("Superb")
	
	case 3|2: print("good ")
	
	case 1: print(" poor ")

	case _ :print("Invalid")
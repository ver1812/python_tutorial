day=input("Enter day")
day = day.ower()

match day:
	case "mon"|"tue"|"wed"|"thu"|"fri" : print("Its a week day ")
	case "sat"|"sun" : print("Its weekend")
	case _ : print("Invalid")
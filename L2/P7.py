#wapp to read length and breadth from user and print area and perimeter 
length =float(input("eNTER Length "))
breadth= float(input("eNTER breadth "))
if( length> 0.0) and (breadth>0.0):
	area =length*breadth
	perimeter= 2* (length +breadth)
	print("area =",area)
	print("perimeter",perimeter)
else:
	print("Invalid")


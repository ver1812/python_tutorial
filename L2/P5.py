radius =float(input("enter radius")) 
if radius > 0.0 :
	pi=22/7
	area = pi*radius*radius
	cir= 2* pi* radius
	print("area =",area)
	print("circumference ", cir)
else :
	print("invalid radius ")
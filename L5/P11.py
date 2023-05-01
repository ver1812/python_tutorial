#wapp to accept radius and print area and circumference
def ac(radius):
    pi=22/7
    area = pi * (radius**2)
    cir =2 * pi * radius
    print("Area = ",area)
    print("circum = ",cir)
radius = float(input("Enter radius"))
if radius >0.0 :
    ac(radius)
else:
    print('invalid')

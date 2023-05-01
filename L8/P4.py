class Circle :
    def __init__(self,radius):
        self.radius = radius
    def show(self):
        print("radius = ",self.radius)
    def area(self):
        ans= 22/7 *self.radius **2
        print("area = ",round(ans,2))
    def circum(self):
        ans= 22/7 *self.radius *2
        print("circum = ",round(ans,2))
r= float(input("enter"))
if r>0.0 :
    c = Circle(r)
    c.show()
    c.area()
    c.circum()
else:
    print("Invalid")

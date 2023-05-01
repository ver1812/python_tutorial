class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def show(self):
        print("length = ",self.length)
        print("breadth = ", self.breadth)
    def area(self):
        ans = self.length * self.breadth
        print("Area is ",ans)
    def perimeter(self):
        ans = 2*(self.length + self.breadth )
        print("Perimeter is ", ans)
length = float(input("Enter length"))
breadth = float(input("Enter breadth"))

if(length >0  )and (breadth>0):
    r=Rectangle(length,breadth)
    r.show()
    r.area()
    r.perimeter()
else:
    print("Invalid")
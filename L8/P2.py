class Square :
    def __init__(self,num):
        self.num = num
    def square(self):
        res = self.num * self.num
        print("Square = ",round(res,2))

num = float(input("enter "))
s = Square(num)
s.square()
class Squareroot :
    def __init__(self,num):
        self.num = num
    def squareroot(self):
        res = self.num ** 0.5
        print("Square = ",round(res,2))

num = float(input("enter "))
s = Squareroot(num)
s.squareroot()
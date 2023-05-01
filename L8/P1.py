#oop
class Evenodd :
    def __init__(self,num):
        self.num = num

    def check(self):
        if self.num % 2 == 0:
            print("even ")
        else :
            print("odd ")

num = int(input("Enter integer "))
e = Evenodd(num)
e.check()
class Employee :
    def __init__(self,id , name , add , salary):
        self.id = id
        self.name = name
        self.add = add
        self.salary = salary
    def show(self):
        print(self.id)
        print(self.name)
        print(self.add)
        print(self.salary)
    def bonus(self):
        amt = self.salary * 0.10
        print("bonus = ",amt)
class JrDev(Employee):
    pass
j = JrDev(10,"a",'thane ',50000)
j.show()
j.bonus()

class SrDev(Employee):
    def bonus(self):
        amt = self.salary * 0.15
        print("bonus = ", amt)

s = SrDev(20,"S","Dadar",100000)
s.show()
s.bonus()
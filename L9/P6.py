class Person:
    def __init__(self,id,name,add):
        self.id = id
        self.name = name
        self.add = add
    def show(self):
        print(self.id)
        print(self.name)
        print(self.add)
class Teacher(Person):
    def __init__(self,id,name,add,salary):
        super().__init__(id,name,add)
        self.salary = salary
    def show(self):
        super().show()
        print(self.salary)
class Hod(Teacher):
    def __init__(self,id,name,add,salary,dept):
        super().__init__(id,name,add,salary)
        self.dept = dept
    def show(self):
        super().show()
        print(self.dept)


p =Person(12,"v","M")
p.show()

t = Teacher(20,"F","N",78)
t.show()

h = Hod(30,"RAJ","KALYAN",600 ,"COMPS")
h.show()
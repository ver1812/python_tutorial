class Person:
    def __init__(self,id, name,location,phone):
        self.name = name
        self.id = id
        self.location = location
        self.phone = phone

    def show(self):
        print(self.name)
        print(self.id)
        print(self.phone)
        print(self.location)
class Student(Person):
    def __init__(self,id,name,location,phone,marks):
        super().__init__(id,name,location,phone)
        self.marks=marks
    def show(self):
        super().show()
        print(self.marks)


s = Student(10,"amit","thane ", 999,45)
s.show()
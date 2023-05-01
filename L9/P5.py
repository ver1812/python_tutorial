class Employee:
    def __init__(self,id , name , salary ):
        self.id = id
        self.name = name
        self.salary = salary
    def show(self):
        print(self.id)
        print(self.name)
        print(self.salary)
class SalesPerson(Employee):
    def __init__(self,id , name , salary, comm):
        super().__init__(id ,name, salary )
        self.comm = comm
    def show(self):
        super().show()
        print(self.comm)
e = Employee(10,"amit",500)
e.show()
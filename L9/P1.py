class Person :
    def __init__(self,id , name , address):
        self.id = id
        self.name = name
        self.address = address
    def display(self):
        print(self.id)
        print(self.name)
        print(self.address)
p1= Person(10,"amit","kalyan")
p1.display()
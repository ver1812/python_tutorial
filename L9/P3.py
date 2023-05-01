class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name)
        print(self.address)

data = {}
while True:
    op = int(input("1.CREATE , 2.READ 3.DELETE 4.EXIT "))
    if op==1:
        id = int(input("Enter id "))
        if data.get(id) is not None:
            print(id,"already exists ")
        else :
            name = input("enter name ")
            add = input("Enter add ")
            data[id] = Person(name,add)
            print("Created ")
    elif op==2:
        for d in data :
            print("id = ",d)
            data[id].display()
    elif op == 3:
        pass
    elif op==4:
        break
    else :
        print("invalid ")

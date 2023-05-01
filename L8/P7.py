class Student:
    def __init__(self,name,marks):

        self.name = name
        self.marks = marks
    def speak(self):

        print(self.name)
        print(self.marks)
data =  {}
while True:
    op = int(input("1.New , 2.view ,3.remove ,4.exit"))
    if op==1:
        rno= int(input('enter rno'))
        if data.get(rno) is not None :
            print(rno," already exists ")
        else:
            name = input("enter name ")
            marks = input("enter marks ")
            data[rno]= Student(name,marks)
            print(rno,"created ")
    elif op==2:
        for d in data:
            print("rno = ",d)
            data[d].speak()
    elif op==3:
        pass
    elif op==4:
        break
    else:
        print("invalid")




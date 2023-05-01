class Student:
    def __init__(self,rno,name,marks):
        self.rno = rno
        self.name = name
        self.marks = marks
    def speak(self):
        print(self.rno)
        print(self.name)
        print(self.marks)

    def find_grade(self):
        if  self.marks >80 :
            print("A")
        elif(self.marks>60):
            print("B")
        else:
            print("c")

rno =float(input("Enter rno "))
name = input("Enter name ")
marks = float(input("Enter marks "))
s = Student(rno, name, marks)
s.speak()
s.find_grade()


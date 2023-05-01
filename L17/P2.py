# queue

class Queue:

    def __init__(self):
        self.data = []

    def enq(self, ele):
        self.data.append(ele)
        print(ele, " is inserted ")

    def deq(self):
        if self.data == 0:
            print("Queue is empty ")
        else:
            ele = self.data.pop(0)
            print("removed element is ", ele)

    def show(self):
        print(self.data)


q = Queue()
while True:
    op = int(input("1.en 2.de 3.show 4.exit "))
    if op == 1:
        ele = int(input("enter element "))
        q.enq(ele)
    elif op == 2:
        q.deq()
    elif op == 3:
        q.show()
    elif op == 4:
        break
    else:
        print("invalid")

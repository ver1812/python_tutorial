# single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            print("added")
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(data)
            print("added")

    def show(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="-->")
            ptr = ptr.next
        print("NULL")


s = SLL()
while True:
    op = int(input("1.add  2.show  3.exit "))
    if op == 1:
        data = int(input("enter data "))
        s.add(data)
    elif op == 2:
        s.show()
    elif op == 3:
        break
    else:
        print("invalid ")

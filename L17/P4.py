# Binary search tree

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.add(data)

        elif data >= self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.add(data)

    def show(self):
        if self.left is not None:
            self.left.show()
        print(self.data)
        if self.right is not None:
            self.right.show()


root = None
while True:
    op = int(input("1.add 2.show 3.exit "))
    if op == 1:
        data = int(input("enter data "))
        if root is None:
            root = Tree(data)
        else:
            root.add(data)

    elif op == 2:
        root.show()

    elif op == 3:
        break

    else:
        print("Invalid ")

# DBEAFCG    IN     17,32,44,48,50,62,78,88
# ABDECFG    PRE    44,17,32,78,50,48,62,88
# DEBFGCA    POST    32,17,48,62,50,88,78,44


# Graph
class Graph:
    def __init__(self):
        self.info = {}

    def add(self, start, end):
        if start in self.info:
            self.info[start].append(end)
        else:
            self.info[start] = [end]

    def show(self):
        for i in self.info:
            print("Node", i)
            for j in self.info[i]:
                print(i, "-", j)


g = Graph()
while True:
    op = int(input("1.add 2.show 3.exit "))
    if op == 1:
        start = input("enter start node ")
        end = input("enter end node ")
        g.add(start, end)

    elif op == 2:
        g.show()

    elif op == 3:
        break

    else:
        print("invalid ")

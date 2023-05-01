#wapp set
#sets are mutable , unordered
s1= set()
print(s1,type(s1))
s1.add(10)
print(s1)
s1.add(20)
s1.update([34,56])
print(s1)
s1.discard(34)
print(s1)

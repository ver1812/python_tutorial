def chant():
    print("Hare Krishna")
    print("Hare rama ")

num = int(input("Enter number"))
if num>0 :
    for i in range (1,num+1):
        chant()
else :
    print("Invalid")
#implement stack
stack = []
while True:
    op= int(input("1:push , 2:pop , 3:show, 4:exit"))
    if op==1:
        ele=int(input("enter element "))
        stack.append(ele)
        print("pushed")
    elif op==2:
        if len(stack)==0:
            print("empty")
        else:
            ele= stack.pop()
            print(ele)
    elif op==3:
        print(stack)
    elif op==4:
        break
    else:
        print("invalid")











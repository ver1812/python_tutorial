#wapp implement queue
q = []
while True:
    op= int(input("1 en , 2 de , 3 show , 4 exit"))
    if op==1:
        ele = int(input("enter"))
        q.append(ele)
    elif op==2:
        if len(q)==0:
            print("empty")
        else:
            ele= q.pop(0)
            print(ele)
    elif op==3:
        print(q)
    elif op==4:
        break
    else:
        print("invalid")
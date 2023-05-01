import requests

try:
    wa = input("enter url ")
    res = requests.get(wa)
    print(res)
    f =open(input("enter file name "),"wb")
    f.write(res.content)
    f.close()
    print("download completed")




except Exception as e:
    print("issue",e)

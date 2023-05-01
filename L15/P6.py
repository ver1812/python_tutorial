import requests

try:
    wa = "https://www.malls2shop.com/admin/malls/42/42.jpg"
    res = requests.get(wa)
    print(res)
    f =open("metro.jpg","wb")
    f.write(res.content)
    f.close()
    print("download completed")




except Exception as e:
    print("issue",e)

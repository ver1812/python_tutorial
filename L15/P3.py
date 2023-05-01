import requests
import time
while True:
    try:
        wa = "https://api.quotable.io/random"
        res = requests.get(wa)
        #print(res)
        data = res.json()
        #print(data)
        msg = data["content"]
        print(msg)
        time.sleep(7)




    except Exception as e:
        print("issue",e)

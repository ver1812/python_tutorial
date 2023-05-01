import requests
import time

try:
    wa = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(wa)
    print(res)
    data = res.json()
    #print(data)
    usd = data["bpi"]["USD"]["rate"]
    print(usd)





except Exception as e:
    print("issue",e)
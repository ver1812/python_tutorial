import requests
import time

try:
    wa = "https://api.exchangerate-api.com/v4/latest/USD"
    res = requests.get(wa)
    print(res)
    data = res.json()
    #print(data)
    usd = data["rates"]["INR"]
    print(usd)

except Exception as e:
    print("issue",e)
#wapp to get current temp
import requests
try :
    a1 = "https://api.openweathermap.org/data/2.5/weather"
    a2 = "?q="+ input("enter city ")
    a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
    a4 = "&units=" + "metric"
    wa = a1+a2+a3+a4
    res = requests.get(wa)
    print(res)
    data = res.json()
    print(data)
    temp = data["main"]["temp"]
    cond = data["weather"][0]["main"]

    print("temperature= ",temp)
    print("weather condition =",cond)




except Exception as e:
    print("issue",e)
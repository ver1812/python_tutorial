import requests

try:
    wa = "https://ipinfo.io/"
    res = requests.get(wa)
    print(res)
    data = res.json()
    print(data)
    city_name = data["city"]
    print("city name is ",city_name)
    state_name =data["region"]
    print("State: ",state_name)
    loc = data["loc"]
    info = loc.split(",")
    lat = info[0]
    lon =info[1]
    print(lat)
    print(lon)



except Exception as e:
    print("issue",e)

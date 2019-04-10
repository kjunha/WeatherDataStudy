import requests
import datetime as d
# Current Weather Data (www.openweathermap.org)

#mytoken = '52c40593fe3f9f62839ef2765f0f8340'
#r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=laie,us&units=imperial&mode=precipitation&appid=52c40593fe3f9f62839ef2765f0f8340')
#print(r.json())
now = d.datetime.now()
y = str(now.year)
m = str(now.month)
d = str(now.day)
sysdate = y + "/" + m + "/" + d
hu = str(now.hour)
mu = str(now.minute)
if len(hu) < 2 :
    while len(hu) < 2:
        hu = "0" + hu
if len(mu) < 2 :
    while len(mu) < 2:
        mu = "0" + mu
systime = hu + ":" + mu

print(sysdate + " " + systime)

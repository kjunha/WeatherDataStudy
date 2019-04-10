import requests
import datetime as d

# Current Weather Data (www.openweathermap.org)
mytoken = '52c40593fe3f9f62839ef2765f0f8340'
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=laie,us&units=imperial&mode=precipitation&appid=52c40593fe3f9f62839ef2765f0f8340')
db = r.json()
ext = str(db['main']['temp']) + "," + str(db['main']['humidity']) + "," + str(db['wind']['speed']) + "," + str(db['clouds']['all']) + "," + str(db['weather'][0]['description'])

#System Time Call
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

f = open("weather_data_daily.csv", "a+")
append = sysdate + "," + systime + "," + ext
f.write(append + "\n")
f.close()
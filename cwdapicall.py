import requests
# Current Weather Data (www.openweathermap.org)


mytoken = '52c40593fe3f9f62839ef2765f0f8340'
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=laie,us&units=imperial&appid=52c40593fe3f9f62839ef2765f0f8340')
print(r.json()['clouds']['all'])
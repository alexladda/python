import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather'

payload = {'lat': -8.663794, 'lon': 115.135669, 'APPID': 'secret'}


r = requests.get(url, params=payload)
print(r)
# print(r.text)
parsed = json.loads(r.text)
pretty = json.dumps(parsed, indent=2)
print(type(parsed))
print(type(pretty))
print(pretty)

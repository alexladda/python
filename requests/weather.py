import requests
import json
from secrets import API_KEY_OPENWEATHER

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = API_KEY_OPENWEATHER

payload = {'lat': -8.663794, 'lon': 115.135669, 'APPID': api_key}


r = requests.get(url, params=payload)
print(type(r))
print(r)
# string
# print(type(r.text))
# print(r.text)

# dict
parsed = json.loads(r.text)
# print(type(parsed))
# print(parsed)

# pretty = json.dumps(parsed, indent=2)
# print(type(parsed))
# print(type(pretty))
# print(pretty)

print('*** dump ***')
for key in parsed:
    print(type(parsed[key]))
    print(key, "->", parsed[key])

print('*** [weather] ***')
for key in parsed['weather'][0]:
    print(key, "->", parsed['weather'][0][key])

print('*** [base] ***')
print('base', "->", parsed['base'])

print('*** [main] ***')
for key in parsed['main']:
    print(key, "->", parsed['main'][key])

print('*** [visibility] ***')
print('visibility', "->", parsed['visibility'])

print('*** [wind] ***')
for key in parsed['wind']:
    print(key, "->", parsed['wind'][key])

print('*** [clouds] ***')
for key in parsed['wind']:
    print(key, "->", parsed['wind'][key])

print('*** [time zone] ***')
print('time zone (Δt in s from UTC)', "->", parsed['dt'])

print('*** [sys] ***')
for key in parsed['sys']:
    print(key, "->", parsed['sys'][key])

print('*** [timezone] ***')
print('timezone', "->", parsed['timezone'])

print('*** [city id] ***')
print('city id', "->", parsed['id'])

print('*** [city name] ***')
print('city name', "->", parsed['name'])

print('*** [city cod] ***')
print('city cod', "->", parsed['cod'])

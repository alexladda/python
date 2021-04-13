import requests

try:
    r = requests.get('https://httpbin.org/delay/6', timeout=3)
    print(r)
except requests.exceptions.Timeout:
    print("the request timed out")
except:
    print("there was an error")

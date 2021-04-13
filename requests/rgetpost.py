import requests


print("### GET REQUESTS ###")

payload = {'page': 2, 'count': 25}

r = requests.get('https://httpbin.org/get', params=payload)

print(r.url)
print(r.text)

print("### POST REQUESTS ###")

payload = {'username': 'alex', 'password': 'simple123'}

r = requests.post('https://httpbin.org/post', data=payload)

print(r.ok)
print(r.url)
print(r.text)
r_dict = r.json()
print(r_dict['form'])

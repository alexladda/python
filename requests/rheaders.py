import requests

r = requests.get('https://instance-0.net')

print(r.status_code)
print(r.ok)

print(r.headers)

print(r.content)
print(r.text)

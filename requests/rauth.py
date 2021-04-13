import requests

url = 'http://httpbin.org/basic-auth/alex/simple123'

print("### CORRECT AUTH ###")

r = requests.get(url, auth=('alex', 'simple123'))
print(r)
print(r.text)

print("### WRONG AUTH ###")

r = requests.get(url, auth=('alex', 's123'))
print(r)

import requests

r = requests.get('https://xkcd.com/353/')

print(dir(r))
print(help(r))
print(r.text)


r = requests.get('https://imgs.xkcd.com/comics/python.png')

#
# with open('xkcd.png', 'wb') as f:
#     f.write(r.content)

print("-> correct adress:")
print(r.status_code)
print(r.ok)

r = requests.get('https://imgs.xkcd.com/comics/asdfaasdfaerae.png')

print("-> wrong adress:")
print(r.status_code)
print(r.ok)

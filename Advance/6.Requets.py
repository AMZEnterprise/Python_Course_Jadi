import requests

r = requests.get('https://www.python.org')

print(r)
print(r.content)
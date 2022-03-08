import re

str = 'Hello ali, how are you ali? I am fine. And you?'

result = re.search(r'ali', str)
print(result)

result = re.sub(r'ali', 'Mahdi', str)
print(result)
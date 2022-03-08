import re

email_reg = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

email = input()

if email_reg.match(email):
    print('OK')
else:
    print('Wrong')
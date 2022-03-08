import datetime

date = input().split('/')

year = int(date[0])
month = int(date[1])
day = int(date[2])

def check_date(year, month, day):
    if year < 0 or month < 0 or day < 0:
        return False
    elif month > 12 or day > 31:
        return False
    else:
        return True

def calculate_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

if check_date(year, month, day):
    print(calculate_age(year, month, day))
else:
    print('Wrong')
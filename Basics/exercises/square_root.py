import math

num_count = int(input())

numbers = []

for i in range(num_count):
    num = int(input())

    frac, whole = math.modf(math.sqrt(num))

    whole_str = str(whole).split('.')[0]
    frac_str = str(frac).split('.')[1][:4]

    if len(frac_str) < 4:
        frac_str = frac_str.ljust(4, '0')

    numbers.append([whole_str, frac_str])

for num in numbers:
    print(num[0] + '.' + num[1])

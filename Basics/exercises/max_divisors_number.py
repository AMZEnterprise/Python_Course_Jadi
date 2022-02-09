def number_of_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def get_inputs():
    n = int(input())
    return n

max_number = 0
max_count = 0

for i in range(20):
    number = get_inputs()
    count = number_of_divisors(number)

    if count > max_count:
        max_count = count
        max_number = number
    elif count == max_count:
        if number > max_number:
            max_number = number

print(str(max_number) + " " + str(max_count))

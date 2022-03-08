def read_input_values(count):
    numbers = []
    for i in range(0,10):
        numbers.append(int(input()))
    
    return numbers

def check_prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def get_number_with_divisers(numbers):
    number_with_divisers_count = []
    for n in numbers:
        divisers = 0
        for i in range(1,n + 1):
            if n % i == 0:
                if check_prime_number(i):
                    divisers += 1
        number_with_divisers_count.append([n,divisers])

    return number_with_divisers_count

def get_number_with_most_divisers(numbers):
    max_divisers = 0
    max_number = 0

    for n in numbers:
        if n[1] > max_divisers:
            max_divisers = n[1]
            max_number = n[0]
    
    for n in numbers:
        if n[1] == max_divisers and n[0] > max_number:
            max_number = n[0]

    return (max_number,max_divisers)

numbers = read_input_values(10)
number_with_divisers_count = get_number_with_divisers(numbers)
result = get_number_with_most_divisers(number_with_divisers_count)

print(str(result[0]) + " " + str(result[1]))
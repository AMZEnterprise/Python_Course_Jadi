number = int(input())

first = number % 10
second = (number // 10) % 10
third = number // 10 // 10

print(2 * int(str(first) + str(second) + str(third)))
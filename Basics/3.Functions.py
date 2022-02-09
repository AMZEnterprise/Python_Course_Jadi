import random

# Built-in Functions
type(5.3)

print('hi')

print(min(2, 5))

print(random.random())


# User-defined Functions
def hello():
    print('Hello')

hello()


def hello_name(name):
    print('Hello ' + name)

hello_name('Ali')

def sum_two_numbers(a, b):
    return a + b

def salary(hours, rate):
    return hours * rate

print(salary(10,30))
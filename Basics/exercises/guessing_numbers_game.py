import random

answer = random.randint(1, 99)

guess = int(input('What is your guess? '))

while guess != answer:
    if guess > answer:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')
    guess = int(input('What is your guess? '))

print('You got it!')
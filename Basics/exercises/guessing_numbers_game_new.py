import random

answer = random.randint(1, 99)

while True:
    print(answer)
    
    inp = input()

    if inp == "k":
        answer = random.randint(1, answer)
    elif inp == "b":
        answer = random.randint(answer, 99)
    elif inp == "d":
        break

total_win, total_lose = 0, 0

for i in range(1, 31):
    number = int(input())

    if number <= 3:
        if number == 0:
            total_lose += 1
        else:
            total_win += number

    else:
        break

print(str(total_win) + " " + str(total_lose))

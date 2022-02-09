players_count = input()

players_inp = input()

players = players_inp.split(" ")

for i in range(len(players)):
    players[i] = int(players[i])

result = []

for i in range(len(players)):
    if players[i] <= 2:
        result.append(players[i])

print(str(len(result)//3))
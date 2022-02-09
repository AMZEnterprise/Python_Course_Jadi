votes_count = int(input())

dic_votes = {}

for i in range(votes_count):
    votes = input()

    if votes in dic_votes:
        dic_votes[votes] += 1

    else:
        dic_votes[votes] = 1

for key, value in sorted(dic_votes.items()):
    print(key, ' ', value)
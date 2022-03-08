import random

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class FootballPlayer(Human):
    def __init__(self, name, age, team):
        super().__init__(name, age)
        self.team = team


players = []
names = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی",
         "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

for name in names:
    team = random.choice(["A","B"])

    if len([p for p in players if p.team == "A"]) == 11:
        team = "B"
    if len([p for p in players if p.team == "B"]) == 11:
        team = "A"

    players.append(FootballPlayer(name, random.randint(18, 40),team))

for player in players:
    print(player.name, player.team)

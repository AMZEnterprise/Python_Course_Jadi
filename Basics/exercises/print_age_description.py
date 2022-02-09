age = int(input())

if age > 0 and age < 6:
    print("khordsal")
elif age >= 6 and age < 10:
    print("koodak")
elif age >= 10 and age < 14:
    print("nojavan")
elif age >= 14 and age < 24:
    print("javan")
elif age >= 24 and age < 40:
    print("bozorgsal")
else:
    print("miansal")

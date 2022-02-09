text = input()

upper_cases_count, lower_cases_count = 0, 0

for character in text:
    if character.isupper():
        upper_cases_count += 1
    elif character.islower():
        lower_cases_count += 1

if upper_cases_count > lower_cases_count:
    print(text.upper())
else:
    print(text.lower())
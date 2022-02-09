
age = int(input())
max_age = age
second_max_age = 0

while age != -1:
    if age >= 10 and age <= 90:
        if age > max_age:
            second_max_age = max_age
            max_age = age
        elif age < max_age and age > second_max_age:
            second_max_age = age

    age = int(input())
    
print(str(max_age) + " " + str(second_max_age))
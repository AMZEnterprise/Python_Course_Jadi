
age = int(input())
max_age = age

while age != -1:
    if age >= 10 and age <= 90:
        if age > max_age:
            max_age = age
    age = int(input())
    
print(max_age)
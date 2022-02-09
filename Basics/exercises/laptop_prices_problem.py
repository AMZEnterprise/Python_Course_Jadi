laptops_count = int(input())

all_laptops = []

for i in range(laptops_count):
    laptop = input()
    laptop_details = laptop.split(" ")

    for i in range(len(laptop_details)):
        laptop_details[i] = int(laptop_details[i])

    all_laptops.append(laptop_details)

flag = False

for i in range(len(all_laptops)):
    for j in range(i, len(all_laptops)):
        if (all_laptops[i][0] > all_laptops[j][0]) and (all_laptops[i][1] < all_laptops[j][1]):
            flag = True
            break

if flag:
    print("happy irsa")
else:
    print("poor irsa")
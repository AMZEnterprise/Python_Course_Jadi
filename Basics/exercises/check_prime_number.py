number = int(input())

flag = False

if number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print("not prime")
else:
    print("prime")

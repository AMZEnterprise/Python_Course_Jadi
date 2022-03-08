people_count = input()

people_list = []

for i in range(0, int(people_count)):
    inp_str = input()
    inp_list = inp_str.split(".")
    inp_list[0] = inp_list[0].lower()
    inp_list[1] = inp_list[1][0].upper() + inp_list[1][1:].lower()
    
    people_list.append(inp_list)



sorted_first = sorted(people_list, key=lambda nested: nested[1])
sorted_second = sorted(sorted_first, key=lambda nested: nested[0])

for i in sorted_second:
    print(i[0] + " " + i[1] + " " + i[2])
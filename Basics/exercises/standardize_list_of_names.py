def get_name():
    return input()

output = ""

for i in range(10):
    name = get_name()

    name = name[0].upper() + name[1:].lower()
    
    output += name + "\n"

print(output)
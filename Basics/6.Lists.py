l1 = [1,2,4,6]

l2 = [l1, 4, 'Ali']

l2[1] = 'Ahmed'

print(l2)

for item in l2:
    print(item)

print(dir(l2))

l3 = [4,2,4,6]

del l3[2]

l3.sort()

l1.extend(l3)

print(l1)

l1.pop()

l1.append(10)

l1.remove(2)

s = 'Hello world some words are here!'

s.split(' ')

l4 = ['Ali','Hasan']

'hello'.join(l4)
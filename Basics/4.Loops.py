n = 5
while n > 5:
    print(n)
    n = n - 1


name = input('Enter your name: ')
while name != 'Ali':
    print('Wrong name')
    name = input('Enter your name: ')

while n >= 0:
    print(n)
    n = n + 1
    if n == 100:
        break


for i in range(1, 10):
    print(i)

for i in range(20):
    if i == 16:
        break
    print(i * i)

friends = ['Ali', 'Ahmad', 'Hassan', 'Sara']

for name in friends:
    print('Hi, ' + name)
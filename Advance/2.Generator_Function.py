def frist():
    yield 1
    yield 2
    yield 3

def second(n):
    num = 0
    while num < n:
        yield num
        num+=1


for i in frist():
    print(i)

for i in second(6):
    print(i)
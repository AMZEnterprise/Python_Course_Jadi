lambda x: x * 2


def myfunc(x): return x * 2


print(myfunc(2))


a = [(3, 4), (5, 6), (7, 8), (2, 1)]

a.sort(key=lambda x: x[1])

print(a)

myList = [1,4,6,1,7,8,3,2]

print(list(map(lambda x: x*3, myList)))

print(list(map(lambda x: 'big' if x> 5 else 'small', myList)))

print(list(filter(lambda x: x%2 == 0, myList)))
inp = input()

points = inp.split(" ")

for i in range(len(points)):
    points[i] = int(points[i])

points.sort()

result = points[len(points) - 1] - points[0]

print(result)
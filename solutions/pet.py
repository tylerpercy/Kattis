largest = 0
index = 0
for i in range(1, 6):
    x = sum([int(x) for x in input().split()])
    if x > largest:
        largest = x
        index = i

print(index, largest)
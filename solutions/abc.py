x, y, z = map(int, input().split())

dict = {
    'A': sorted([x, y, z])[0],
    'B': sorted([x, y, z])[1],
    'C': sorted([x, y, z])[2]
}

for c in list(input()):
    print(dict[c], end=" ")
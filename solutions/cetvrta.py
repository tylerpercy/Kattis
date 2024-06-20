coords = []

for _ in range(0, 3):
    coords.append(tuple([int(x) for x in input().split()]))

print(coords[0][0] ^ coords[1][0] ^ coords[2][0], coords[0][1] ^ coords[1][1] ^ coords[2][1])

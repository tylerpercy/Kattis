n, m = [int(x) for x in input().split()]

loop = {
    '.': 20,
    'O': 10,
    '\\': 25,
    '/': 25,
    'A': 35,
    '^': 5,
    'v': 22
}

sum = 0
for _ in range(0, n):
    w = input()
    for c in w:
        if c in loop.keys():
            sum += loop[c]

print(sum)

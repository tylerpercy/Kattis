l = []
for _ in range(int(input())):
    n, a1, ai = (lambda x: (x[0], float(x[1]), float(x[2])))(input().split())
    l.append([n, a1, ai])

l.sort(key = lambda x: x[2])

print(l)
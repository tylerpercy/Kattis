p = []
for _ in range(int(input())):
    p.append(int(input()))

p.sort(reverse=True)

total = 0
for i in range(len(p)):
    if (i + 1) % 3 != 0:
        total += p[i]

print(total)


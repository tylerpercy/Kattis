c = float(input())
n = int(input())

total = 0
for _ in range(0, n):
    l, w = [float(x) for x in input().split()]
    total += (l * w * c)

print(total)

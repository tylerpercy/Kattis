n, k = [int(x) for x in input().split()]

min = 0
max = 0
for _ in range(0, k):
    x = int(input())
    min += x
    max += x

for _ in range(0, n-k):
    min += -3
    max += 3

print(min / n, max / n)
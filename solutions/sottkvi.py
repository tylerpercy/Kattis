n, k, d = [int(x) for x in input().split()]

counter = 0
for _ in range(0, n):
    if int(input()) + 14 <= k + d:
        counter += 1

print(counter)
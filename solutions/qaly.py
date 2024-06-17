n = int(input())

sum = 0
for i in range(0, n):
    q, y = [float(x) for x in input().split()]
    sum += q * y

print(sum)

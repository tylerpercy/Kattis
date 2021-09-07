
n = int(input())
total = 0

for i in range(n):
    total += int(input())
    if i > 0:
        total -= 1

print(total)

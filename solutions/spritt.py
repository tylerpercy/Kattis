n, x = [int(x) for x in input().split()]

sum = 0
for i in range(0, n):
    sum += int(input())

print("Jebb") if sum <= x else print("Neibb")
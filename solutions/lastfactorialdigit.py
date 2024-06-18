from math import factorial

n = int(input())

ans = []
for _ in range(0, n):
    ans.append(str(factorial(int(input())))[-1:])

for num in ans:
    print(num)
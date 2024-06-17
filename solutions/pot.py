n = int(input())

ans = 0
for _ in range(0, n):
    x = input()
    ans += pow(int(x[:-1]), int(x[-1:]))

print(ans)
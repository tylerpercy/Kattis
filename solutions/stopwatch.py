n = int(input())
m = []

if n % 2 == 0:
    for _ in range(0, n//2):
        x = int(input())
        y = int(input())
        m.append((x, y))
else:
    for _ in range(0, n):
        input()
    
ans = 0
for i in m:
    ans += i[1] - i[0]

print("still running") if n % 2 != 0 else print(ans)
        


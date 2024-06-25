n = int(input())

ans = []

for _ in range(0, n):
    if "Simon says" in (x := input()):
       ans.append(x[11:].strip())

for a in ans:
    print(a)
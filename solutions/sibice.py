from math import sqrt

n, w, h = [int(x) for x in input().split()]

ans = []
for _ in range(0, n):
    x = int(input())
    if w >= x or h >= x or (x <= sqrt((pow(w, 2) + pow(h, 2)))):
        ans.append("DA")
    else:
        ans.append("NE")

for a in ans:
    print(a)
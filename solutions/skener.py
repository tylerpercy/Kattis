r, c, zr, zc = [int(x) for x in input().split()]

lines = []
for _ in range(0, r):
    lines.append([x for x in input()])

ans = []
for line in lines:
    x = ""
    for ch in line:
        x += ch*zc
    for _ in range(0, zr):
        ans.append(x)

for line in ans:
    print(line)

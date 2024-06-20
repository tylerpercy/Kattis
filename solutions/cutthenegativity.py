n = int(input())

chart = []
for _ in range(0, n):
    chart.append([int(x) for x in input().split()])

ans = []
for i in range(0, n):
    for j in range(0, n):
        if chart[i][j] != -1:
           ans.append(f"{i+1} {j+1} {chart[i][j]}")

print(len(ans))
for a in ans:
    print(a)

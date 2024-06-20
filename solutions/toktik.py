n = int(input())

tt = {}

for _ in range(0, n):
    x = input().split(' ')
    if x[0] in tt.keys():
        tt[x[0]] += int(x[1])
    else:
        tt[x[0]] = int(x[1])

largest = 0
ans = ''
for k, v in tt.items():
    if v > largest:
        largest = v
        ans = k

print(ans)

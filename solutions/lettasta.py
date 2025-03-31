N = int(input())
M = int(input())
a = input().split()
l = [list(map(int, input().split())) for _ in range(M)]
m = [0 for _ in range(N)]

for j in range(N):
    m[j] = sum([l[i][j] for i in range(M)])
        
print(a[m.index(max(m))])
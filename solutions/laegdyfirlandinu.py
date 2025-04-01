N, M = map(int, input().split())

l = []
for _ in range(N):
    l.append(list(map(int, input().split())))

found = False

for i in range(N):
    for j in range(M):
        if (i > 0 and i < N-1 and j > 0 and j < M-1):
            if l[i-1][j] > l[i][j] and l[i+1][j] > l[i][j] \
            and l[i][j-1] > l[i][j] and l[i][j+1] > l[i][j]:
                found = True
                break

print("Jebb") if found else print("Neibb")

                           
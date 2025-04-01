N, M, K = map(int, input().split())

coords = set()
for _ in range(K):
    x, y = map(int, input().split())
    coords.add((x, y))

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i, j) in coords:
            print("*", end="")
        else:
            print('.', end="") 
    print()



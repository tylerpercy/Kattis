def find_weak_vertices(n, matrix):
    weak_vertices = []
    
    for i in range(n):
        is_weak = True
        for j in range(n):
            for k in range(n):
                if matrix[i][j] and matrix[i][k] and matrix[j][k]:
                    is_weak = False
                    break
            if not is_weak:
                break
        if is_weak:
            weak_vertices.append(i)
    
    return weak_vertices

grids = []
while True:
    n = int(input())
    if n == -1:
        break

    grid = []
    for _ in range(n):
        grid.append([int(x) for x in input().split()])
    grids.append(grid)

ans = []
for grid in grids:
    ans.append(find_weak_vertices(len(grid), grid))

for a in ans:
    print(' '.join(map(str, a)))

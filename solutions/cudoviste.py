def check_2x2(l, i, j):
    cars = 0
    try:
        if l[i][j] == '#' or l[i+1][j] == '#' or l[i][j+1] == '#' or l[i+1][j+1] == '#':
            return -1
        if l[i][j] == 'X':   
            cars += 1
        if l[i+1][j] == 'X':  
            cars += 1
        if l[i][j+1] == 'X':     
            cars += 1
        if l[i+1][j+1] == 'X':
            cars += 1
    except IndexError:
        return -1

    return cars

N, M = map(int, input().split())

l = []
cars = [0,0,0,0,0]
for _ in range(N):
    l.append(input())

for i in range(N):
    for j in range(M):
        count = check_2x2(l, i, j)
        if count == -1:
            continue
        else:
            cars[count] += 1

for c in cars:
    print(c)



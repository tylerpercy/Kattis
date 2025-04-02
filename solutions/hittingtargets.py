def fill_rect(x1, y1, x2, y2):
    fill = set()
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            fill.add((i, j))

    return fill

def fill_circle(x, y, r):
    fill = set()
    for i in range(x-r, x+r+1):
        for j in range(y-r, y+r+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                fill.add((i, j))

    return fill

fills = []
for _ in range(int(input())):
    tmp = input().split()
    shape = tmp[0]
    coords = [int(x) for x in tmp[1:]]
    if shape == 'rectangle':
        fills.append(fill_rect(*coords))
    else:
        fills.append(fill_circle(*coords))

shots = []
for _ in range(int(input())):
    x, y = (map(int, input().split()))
    shots.append((x, y))

ans = []
for shot in shots:
    counter = 0
    for fill in fills:
        if shot in fill:
            counter += 1
    ans.append(counter)

for a in ans:
    print(a)
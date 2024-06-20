n = [c for c in input()]
x = [1, 0, 0]

for c in n:
    if c == 'A':
        x[0], x[1] = x[1], x[0]
    elif c == 'B':
        x[1], x[2] = x[2], x[1]
    else:
        x[0], x[2] = x[2], x[0]

print(x.index(1)+1)
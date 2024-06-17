
distinct = []
for _ in range(0, 10):
    x = int(input()) % 42
    if x not in distinct:
        distinct.append(x)

print(len(distinct))
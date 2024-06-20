n = input().split(';')

counter = 0
for v in n:
    if '-' in v:
        a, b = v.split('-')
        for _ in range(int(a), int(b)+1):
            counter += 1
    else:
        counter += 1

print(counter)

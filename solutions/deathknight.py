n = int(input())

counter = 0
for _ in range(0, n):
    if "CD" in input():
        continue
    else:
        counter += 1

print(counter)
    

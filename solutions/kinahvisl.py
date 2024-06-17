first = input()
second = input()

counter = 1
for c1, c2 in zip(first, second):
    if c1 != c2:
        counter += 1

print(counter)
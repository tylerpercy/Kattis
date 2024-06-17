from itertools import chain

counter = 0
for c in input():
    if c in list(map(chr, chain(range(65,91), range(97,123)))):
        counter += 1

print(counter)
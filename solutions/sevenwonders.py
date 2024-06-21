from collections import Counter

s = [c for c in input()]
x = Counter(s)

sum = 0
for k,v in x.items():
    sum += pow(v, 2)

if 0 not in x.values() and len(x) == 3:
        sum += min(x.values()) * 7

print(sum)


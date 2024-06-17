from collections import Counter

n, m = [int(x) for x in input().split()]

odds = []
for i in range(1, n+1):
    for j in range(1, m+1):
        odds.append(i+j)

ans = [i for i in set(odds) if odds.count(i)==max([odds.count(i) for i in set(odds)])]

for num in ans:
    print(num)


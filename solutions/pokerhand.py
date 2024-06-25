from collections import Counter
print(max(Counter([x[:1] for x in input().split(' ')]).values()))


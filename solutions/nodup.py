from collections import Counter

if all(value == 1 for value in Counter(input().split()).values()):
    print("yes")
else:
    print("no")
n, m = [int(x) for x in input().split()]

message = ""
for _ in range(0, n):
    for c in input():
        if c in list(map(chr, range(97,123))):
            message += c

print(message)

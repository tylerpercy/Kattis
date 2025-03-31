N = int(input())
W = list(map(int, input().split()))

if sum(W) % 3 == 0:
    print("yes")
else:
    print("no")
W = int(input())
N = int(input())

sum = 0
for i in range(N):
    w, l = map(int, input().split())

    sum += w * l

print(sum // W)

       
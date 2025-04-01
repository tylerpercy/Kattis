N = int(input())

inc = 0
prev = input()
for i in range(N-1):
    cur = input()
    if cur == "sober" and prev == "drunk":
        inc += 1
    prev = cur

print(inc)


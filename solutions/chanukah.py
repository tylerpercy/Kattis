p = int(input())

nums = []
for i in range(0, p):
    _, n = [int(x) for x in input().split()]
    nums.append(y := sum([x for x in range(1, n+2)])-1)

for i in range(0, p):
    print(f"{i+1} {nums[i]}")
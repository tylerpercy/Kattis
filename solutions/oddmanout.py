from collections import Counter

n = int(input())

ans = []
for _ in range(0, n):
    g = int(input())
    x = Counter([int(x) for x in input().split()])

    for num in x:
        if x[num] == 1:
            ans.append(num)

for i in range(0, len(ans)):
    print(f"Case #{i+1}: {ans[i]}")

    


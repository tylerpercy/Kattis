n = int(input())

ans = []
for _ in range(0, n):
    x = [int(x) for x in input().split()]
    sum = 0
    
    for i in range(0, len(x)-1):
        if x[i+1] > 2 * x[i]:
            sum += x[i+1] - (2 * x[i])
    
    ans.append(sum)

for a in ans:
    print(a)
 


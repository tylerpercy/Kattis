# Tyler Percy
# 1/13/21

n = int(input())

for i in range(0, n):
    arr = list(map(int, input().split()))
    arr.pop(0)
    sum = 0
    for i in arr:
        sum += i-1
    sum += 1
    print(sum)
        

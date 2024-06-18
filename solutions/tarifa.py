x = int(input())
n = int(input())

sum = x
for _ in range(0, n):
    sum -= int(input()) 
    sum += x

print(sum)


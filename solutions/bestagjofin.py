n = int(input())

largest = 0
name = ""
for _ in range(0, n):
    x,y = input().split(' ')
    if int(y) > largest:
        largest = int(y)
        name = x

print(name)
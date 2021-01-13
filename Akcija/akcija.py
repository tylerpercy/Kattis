# Tyler Percy
# 1/13/21

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

price = 0
group = []

for i in range(len(arr)):
    group.append(arr.pop())

    if (len(group) == 3):
        price += sum(group) - min(group)
        group = []
        

price += sum(group)
print(price)

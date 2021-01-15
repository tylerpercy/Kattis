# Tyler Percy
# 1/15/21

n = int(input())
seen = []
prizeList = []

for i in range(0, n):
    x = input()
    y = x.split()
    if y[0] not in seen:
        prizeList.append(x)
             
    seen.append(y[0])

while len(prizeList) > 12:
    prizeList.pop(len(prizeList)-1)
        
for school in prizeList:
    print(school)
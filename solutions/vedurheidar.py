v = int(input())
n = int(input())

roads = []
for _ in range(0, n):
    road, speed = input().split()
    if int(speed) >= v:
        safety = "opin"
    else:
        safety = "lokud"
    
    roads.append((road, safety))

for r in roads:
    print(f"{r[0]} {r[1]}")




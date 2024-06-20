n = int(input())

reels = []

for _ in range(0, 3):
    reels.append([int(x) for x in input().split()])

count = 0
for reel in reels:
    if 7 in reel:
        count += 1

print("777") if count == 3 else print("0")
    
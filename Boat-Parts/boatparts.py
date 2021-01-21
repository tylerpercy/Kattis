# Tyler Percy
# 1/21/21

temp = input().split()

p = int(temp[0])
n = int(temp[1])

parts = []
allPartsReplaced = False

for i in range(1, n+1):
    part = input()
    if part not in parts:
        #print("adding part:", part)
        parts.append(part)
    if len(parts) == p:
        p = i
        allPartsReplaced = True
        break

if allPartsReplaced:
    print(p)
else:
    print("paradox avoided")


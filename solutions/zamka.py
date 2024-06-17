l = int(input())
d = int(input())
x = int(input())

valid = []
for i in range(l, d+1):
    if sum(map(int, str(i))) == x:
        valid.append(i)

print(min(valid))
print(max(valid))
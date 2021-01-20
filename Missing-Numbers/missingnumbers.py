# Tyler Percy
# 1/20/21

n = int(input())

ints = []
inp = []

for i in range(0, n):
    inp.append(int(input()))

for i in range(1, int(inp[len(inp)-1]+1)):
    ints.append(i)

for i in inp:
    if i in ints:
        ints.remove(i)

if len(ints) == 0:
    print("good job")
else:
    for i in ints:
        print(i)


_ = input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

l = list(set(a) - set(b))
v = [x for x in a if x not in l]

for n in v:
    print(n, end=" ")


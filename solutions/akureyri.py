l = []
for _ in range(int(input())):
    _ = input()
    l.append(input())

for s in set(l):
    print(f"{s} {l.count(s)}")


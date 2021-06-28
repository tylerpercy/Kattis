_in = [int(i) for i in input().split(' ')]
ans = sorted(_in)

pr = ""

for i in ans:
    pr += f"{i} "

print(pr)

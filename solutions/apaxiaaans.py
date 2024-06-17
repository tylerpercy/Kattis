from itertools import groupby

ans = ""
for (key,group) in groupby(input()):
    ans += key

print(ans)

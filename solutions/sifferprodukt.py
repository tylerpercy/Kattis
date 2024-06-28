ans = int(input())
while len(str(ans)) > 1:
    ans = eval('*'.join(x for x in str(ans) if x != '0'))

print(ans)
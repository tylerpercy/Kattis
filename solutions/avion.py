ans = []
for i in range(1, 6):
    if 'FBI' in input():
        ans.append(i)

print("HE GOT AWAY!") if len(ans) == 0 else [print(a, end=' ') for a in ans]


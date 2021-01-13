
def sum_digits(x):
    ans = 0
    for i in x:
        ans += int(i)

    return ans

L = int(input())
D = int(input())
X = int(input())

ans = []
for i in range(L, D+1):
    tmp = [int(d) for d in str(i)]
    dig = sum_digits(tmp)
    if dig == X:
        ans.append(i)

M = min(ans)
N = max(ans)

print(M)
print(N)
    
     

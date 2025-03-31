X, Y = map(int, input().split())

x = []
for i in range(X):
    n = list(input())
    for j in range(len(n)):
        if n[j] == '*':
            x.append((f"{i+1} {j+1}"))

print(len(x))
for c in x:
    print(c)

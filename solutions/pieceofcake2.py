N, H, V = map(int, input().split())

h = max(N-H, N-(N-H))
v = max(N-V, N-(N-V))

print(h*v*4)





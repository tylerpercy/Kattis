N, K = map(int, input().split())
X = list(map(int, input().split()))

print(*X[K-1::K])
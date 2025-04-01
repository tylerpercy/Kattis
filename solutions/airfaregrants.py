N = int(input())

flights = []
for _ in range(N):
    flights.append(int(input()))

ans = max(min(flights)-(max(flights) // 2), 0)

print(ans)
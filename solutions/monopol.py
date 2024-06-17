n = int(input())
a = [int(x) for x in input().split()]

ans = 0
for num in a:
     count = sum(1 for dice1 in range(1, 7) for dice2 in range(1, 7) if dice1 + dice2 == num)
     ans += count / 36

print(ans)

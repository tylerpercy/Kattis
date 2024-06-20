totals = []
while(int((n := input())) != -1):
    miles = 0
    elapsed = 0
    prev = 0
    for _ in range(0, int(n)):
        s, t = [int(x) for x in input().split()]
        prev = elapsed
        elapsed = t
        miles += s * (elapsed - prev)

    totals.append(miles)

for total in totals:
    print(f"{total} miles")
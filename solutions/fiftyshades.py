n = int(input())

counter = 0
for _ in range(0, n):
    if "pink" in (x := input().lower()) or "rose" in x:
        counter += 1

print("I must watch Star Wars with my daughter") if counter == 0 else print(counter)

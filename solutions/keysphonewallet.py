n = int(input())

items = []
for _ in range(0, n):
    items.append(input())

if set(["phone", "keys", "wallet"]) <= set(items):
    print("ready")
else:
    for item in sorted(set(["phone", "keys", "wallet"]) - set(items)):
        print(item)


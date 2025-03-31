n = int(input())

x = 0
for _ in range(n):
    _ = input()
    x += int(input())

if x < 0:
    print("Nekad")
elif x > 0:
    print("Usch, vinst")
else:
    print("Lagom")
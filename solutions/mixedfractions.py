a, b = (-1, -1)
while (a, b) != (0, 0):
    a, b = map(int, input().split())
    try:
        print(a // b, a % b, "/", b)
    except ZeroDivisionError:
        continue
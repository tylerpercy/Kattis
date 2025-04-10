for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a + b == c or abs(a - b) == c or a * b == c or (a // b == c and a % b == 0) or (b // a == c and b % a == 0):
        print("Possible")
    else:
        print("Impossible")

from math import isqrt

for _ in range(int(input())):
    s = []

    N = int(input())

    if N % 2 != 0:
        s.append('O')
    if N == isqrt(N) ** 2:
        s.append('S')

    print("EMPTY") if not s else print(*s, sep='')
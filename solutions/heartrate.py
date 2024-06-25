n = int(input())

for _ in range(0, n):
    b, p = [float(x) for x in input().split()]

    bpm = (60*b)/p
    abpm = 60/p

    print(f"{bpm-abpm:.6} {bpm:.6} {bpm+abpm:.6}")
   




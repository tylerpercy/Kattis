l, r = [int(x) for x in input().split()]

if l == r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l*2}")
else:
    print(f"Odd {max(l, r)*2}")
ws, l, u, s = 0, 0, 0, 0
for c in (x := input()):
    if c == '_':
        ws += 1
    elif c.islower():
        l += 1
    elif c.isupper():
        u += 1
    else:
        s += 1

print(f"{ws/len(x):.15f}")
print(f"{l/len(x):.15f}")
print(f"{u/len(x):.15f}")
print(f"{s/len(x):.15f}")

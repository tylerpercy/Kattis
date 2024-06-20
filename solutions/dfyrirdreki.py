import math

a = int(input())
b = int(input())
c = int(input())

roots = []
try:
    x = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
except:
    pass
else:
    roots.append(x)

try:
    y = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
except:
    pass
else:
    roots.append(y)

print(len(set(roots)))

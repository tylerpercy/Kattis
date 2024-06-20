from math import sin, radians, pi

h, v = [int(x) for x in input().split()]

print(int(h / sin(radians(v)))+1)
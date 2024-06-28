from math import ceil, floor
x = float(input())
print(ceil(float(x))) if x % 1 >= .5 else print(floor(x))
a, b = [int(x) for x in input().split()]

print(b + (b-a)) if a > b else print(b - (a-b))
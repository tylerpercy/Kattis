correct = [1, 1, 2, 2, 2, 8]
pieces = [int(x) for x in input().split()]
out = [a - b for a, b in zip(correct, pieces)]
[print(f"{i} ") for i in out]


n = int(input())

outputs = []
for _ in range(0, n):
    comp = ""
    x = input()
    y = input()
    for x_c, y_c in zip(x, y):
        if x_c == y_c:
            comp += '.'
        else:
            comp += '*'

    outputs.append((x, y, comp))

for output in outputs:
    print(f"{output[0]}\n{output[1]}\n{output[2]}")
    



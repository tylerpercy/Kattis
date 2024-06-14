words = []

for i in range(1, int(input())+1):
    x = input()
    if not i % 2 == 0:
        words.append(x)

[print(f"{word}") for word in words]
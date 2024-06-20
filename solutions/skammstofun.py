n = int(input())
phrase = input().split(' ')

capital = []

for word in phrase:
    for c in word[0]:
        if c.isupper():
            capital.append(c)

for c in capital:
    print(c, end='')
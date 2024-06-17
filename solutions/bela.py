n, b = input().split()
n = int(n)

cards = {
    'A': 11, 
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0
}

sum = 0
for _ in range(0, n):
    for _ in range(0, 4):
        c = input()
        if c[1] == b:
            cards['J'] = 20
            cards['9'] = 14
        sum += cards[c[0]]
        cards['J'] = 2
        cards['9'] = 0

print(sum)
        

    

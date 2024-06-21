s = [c for c in input()]

counter = 0
changes = 0
for i in range(0, len(s)):
    if counter > 2:
        counter = 0
    match counter:
        case 0:
            if s[i] != 'P':
                s[i] = 'P'
                changes += 1
        case 1:
            if s[i] != 'E':
                s[i] = 'E'
                changes += 1
        case 2:
            if s[i] != 'R':
                s[i] = 'R'
                changes += 1
    counter += 1

print(changes)

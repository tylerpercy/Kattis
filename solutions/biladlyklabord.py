S = list(input())

for i in range(len(S)):
    try:
        if S[i+1] == S[i]:
            continue
        else:
            print(S[i], end='')
    except IndexError:
        print(S[i], end='')



for i in range(0, len(s := input())+1):
    try:
        if s[i] == ':' or s[i] == ';':
            if s[i+1] == '-':
                if s[i+2] == ')':
                    print(i)
            elif s[i+1] == ')':
                print(i)
    except:
        continue
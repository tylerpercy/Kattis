while (True):
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    else:
        print(abs(a-b))
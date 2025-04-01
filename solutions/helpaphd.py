for _ in range(int(input())):
    try:
        n, m = map(int, input().split('+'))
    except:
        print("skipped")
    else:
        print(n+m)

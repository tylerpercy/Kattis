n = int(input())

flag = False
while flag is False:
    if n % sum(map(int, str(n))) == 0:
        print(n)
        break
    else:
        n += 1

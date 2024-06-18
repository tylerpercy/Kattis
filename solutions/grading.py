x = [int(x) for x in input().split()]
n = int(input())

x.append(n)
x.sort(reverse= True)

match n:
    case n if n >= x[0]:
        print('A')
    case n if n < x[4]:
        print('F')
    case n if n < x[3]:
        print('E')
    case n if n < x[2]:
        print('D')
    case n if n < x[1]:
        print('C')
    case n if n < x[0]:
        print('B')
    



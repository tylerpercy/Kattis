n = 0
while n != '0':
    n = input()
    s = []
    for _ in range(int(n)):
        s.append(input())
    s.sort(key=lambda x: (x[0], x[1]))
    for i in s:
        print(i)
    print()
        

 




    
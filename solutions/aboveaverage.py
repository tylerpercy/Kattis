for _ in range(int(input())):
    n, *a = map(int, input().split())
    avg = sum(a) / n
    print(f"{(sum(x > avg for x in a) / n * 100):.3f}%")
from collections import Counter

N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    seen = set()
    found = False
    for x in A:
        if 7777 - x in seen:
            print("Yes")
            found = True
            break
        seen.add(x)
    if not found:
        print("No")
elif t == 2:
    print("Unique" if len(set(A)) == N else "Contains duplicate")
elif t == 3:
    count = Counter(A).most_common(1)[0]
    print(count[0] if count[1] > N // 2 else -1)
elif t == 4:
    A.sort()
    print(A[N//2 - 1], A[N//2]) if N % 2 == 0 else print(A[N//2])
elif t == 5:
    print(*sorted([n for n in A if 100 <= n <= 999]), end=" ")
N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print("7")
elif t == 2:
    print("Bigger") if A[0] > A[1] else print("Smaller") if A[0] < A[1] else print("Equal")
elif t == 3:
    print(sorted(A[:3])[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    print(sum(n for n in A if n % 2 == 0))
elif t == 6:
    print(''.join(chr((c % 26) + ord('a')) for c in A))
elif t == 7:
    visited = set()
    cur = 0
    while True:
        if cur < 0 or cur >= len(A):
            print("Out")
            break
        if cur in visited:
            print("Cyclic")
            break
        if cur == N-1:
            print("Done")
            break

        visited.add(cur)
        cur = A[cur]


        

def sum_pos(N):
    return (N * (N + 1)) // 2

def sum_odd(N):
    return N * N

def sum_even(N):
    return N * (N + 1)

P = int(input())

for i in range(P):
    _, N = map(int, input().split())

    print(i+1, sum_pos(N), sum_odd(N), sum_even(N))

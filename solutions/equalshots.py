A, B = map(int, input().split())

a = 0
b = 0

for i in range(A):
    v, c = map(int, input().split())
    a += v*c
for i in range(B):
    v, c = map(int, input().split())
    b += v*c

if a == b:
    print("same")
else:
    print("different")


n = int(input())

answers = []
for _ in range(0, n):
    r, e, c = [int(x) for x in input().split()]
    if e - c == r:
        answers.append("does not matter")
    elif e - c > r:
        answers.append("advertise")
    else:
        answers.append("do not advertise")

for answer in answers:
    print(answer)
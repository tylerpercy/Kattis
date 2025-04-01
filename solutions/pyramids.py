N = int(input())

i = 0
j = 0
l = []

while j < N:
    if i ** 2 > N:
        break
    if i % 2 != 0:
        l.append(i**2)
    j = i ** 2
    i += 1

sum = 0
for i in range(len(l)):
    if sum + l[i] > N:
        print(i)
        break
    else:
        sum += l[i]


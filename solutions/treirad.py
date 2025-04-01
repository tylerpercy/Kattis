N = int(input()) 

i = 0
j = 1
k = 2
count = -1

while i*j*k < N:
    if i*j*k > N:
        break
    else:
        i += 1
        j += 1
        k += 1
        count += 1

print(count)

       
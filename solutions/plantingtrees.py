N = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)

counter = 0

for i in range(N):
    finished = (i + 1) + trees[i]  
    counter = max(counter, finished)

print(counter+1)
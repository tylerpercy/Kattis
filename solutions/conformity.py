N = int(input())  
courses = {}  

for _ in range(N):
    c = tuple(sorted(map(int, input().split())))
    if c in courses:
        courses[c] += 1
    else:
        courses[c] = 1

ans = sum(c for c in courses.values() if c == max(courses.values()))

print(ans)
# Tyler Percy
# 1/20/21

n = int(input())

counter = 0
valid = ["pink", "rose"]
labels = []

for _ in range(0, n):
    labels.append(input().lower())

for i in labels:
    if any([c in i for c in valid]):
        counter+=1

if counter > 0:
    print(counter)
else:
    print("I must watch Star Wars with my daughter")

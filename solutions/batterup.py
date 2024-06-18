n = int(input())
bats = [int(x) for x in input().split() if int(x) >= 0]
print(sum(bats)/len(bats))

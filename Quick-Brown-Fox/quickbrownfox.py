# Tyler Percy
# 1/14/21

n = int(input())

alphaList = [char for char in "abcdefghijklmnopqrstuvwxyz"]
charsToRemove = [char for char in "0123456789.,?!'\""]
alphaSet = set(alphaList)

ansList = []

for _ in range(0, n):
    inputSet = set([char.lower() for char in input()])
    inputList = sorted(inputSet)
    
    if " " in inputList:
        inputList.pop(0)

    for i in charsToRemove:
        if i in inputList:
            inputList.remove(i)
    ans = inputList

    if ans == alphaList:
        ansList.append("pangram")
    else:
        ans = [i for i in alphaList + ans if i not in alphaList or i not in ans]
        ansStr = "".join(ans)
        ansList.append("missing %s" % (ansStr))

for i in ansList:
    print(i)

# Tyler Percy
# 1/14/21

n = int(input())
board = []
ans = 1

for _ in range (0, n):
    board.append(input())

for i in range (0, n):
    bCount = 0
    wCount = 0
    for j in range(0, n):
        currentLoc = board[i][j]
        if j == 0:
            prevLoc = 'X'
        else:
            prevLoc = board[i][j-1]
        try:
            nextLoc = board[i][j+1]
        except IndexError:
            nextLoc = 'X'

        if currentLoc == 'B':
            bCount+=1
        elif currentLoc == 'W':
            wCount+=1
        else:
            pass

        if prevLoc == currentLoc and currentLoc == nextLoc:
            ans = 0

    if bCount != wCount:
        ans = 0

for i in range(0, n):
    bCount = 0
    wCount = 0
    for j in range(0, n):
        currentLoc = board[j][i]
        if j == 0:
            prevLoc = 'X'
        else:
            prevLoc = board[j-1][i]
        try:
            nextLoc = board[j+1][i]
        except IndexError:
            nextLoc = 'X'
        
        if currentLoc == 'B':
            bCount+=1
        elif currentLoc == 'W':
            wCount+=1
        else:
            pass

        if prevLoc == currentLoc and currentLoc == nextLoc:
            ans = 0
    
    if bCount != wCount:
        ans = 0
        
print(ans)



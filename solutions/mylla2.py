grid = [input() for _ in range(3)]

win = False

for row in grid:
    if row == "OOO":
        win = True

for col in range(3):
    if grid[0][col] == grid[1][col] == grid[2][col] == "O":
        win = True

if grid[0][0] == grid[1][1] == grid[2][2] == "O":
    win = True
if grid[0][2] == grid[1][1] == grid[2][0] == "O":
    win = True

print("Jebb") if win else print("Neibb")                    
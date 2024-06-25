l, x = [int(i) for i in input().split()]

people = 0
denied = 0
for _ in range(0, x):
    word, num = input().split(' ')
    match word:
        case "enter":
            people += int(num)
            if people > l:
                people -= int(num) 
                denied += 1
        case "leave":
            people -= int(num)

print(denied)

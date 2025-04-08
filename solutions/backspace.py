n = list(input())

stack = []
for char in n:
    if char == "<":
        if stack:
            stack.pop()
    else:
        stack.append(char)

print(*stack, sep="")

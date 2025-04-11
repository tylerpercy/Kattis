import sys
from collections import deque

s = sys.stdin.read().splitlines()

left = deque()
right = deque()

for i in range(1, int(s[0]) + 1):
    instr, num = s[i].split()
    num = int(num)

    match instr:
        case "push_front":
            left.appendleft(num)
        case "push_back":
            right.append(num)
        case "push_middle":
            left.append(num)
        case "get":
            if num < len(left):
                print(left[num])
            else:
                print(right[num - len(left)])

    if instr != "get":
        while len(left) > len(right) + 1:
            right.appendleft(left.pop())
        while len(left) < len(right):
            left.append(right.popleft())

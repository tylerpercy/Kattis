# Tyler Percy
# 1/15/21

def evalRange(s):
    nums = [int(c) for c in s.split('-') if c.isdigit()]
    return (nums[1] - nums[0]) + 1

hw = input()
hwList = hw.split(';')

sum = 0

for i in hwList:
    if i.isdigit():
        sum += 1
    else:
        sum += evalRange(i)

print(sum)
def prev(nums, i):
    if i > 0:
        return nums[i - 1]
    return None

_ = input()
nums = sorted(list(map(int, input().split())))

cons = []
cur = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        cur.append(nums[i])
    else:
        if len(cur) >= 3:
            cons.append(cur)
        cur = [nums[i]]

if len(cur) >= 3:
    cons.append(cur)

sets = set(n for group in cons for n in group)
rest = [n for n in nums if n not in sets]

for group in cons:
    rest.append(group)

rest.sort(key=lambda x: x[0] if isinstance(x, list) else x)

for i in rest:
    if isinstance(i, list):
        print(f"{i[0]}-{i[-1]}", end=" ")
    else:
        print(i, end=" ")

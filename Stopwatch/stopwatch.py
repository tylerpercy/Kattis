
n = int(input())

nums = []
ans = 0

for i in range(0, n):
    nums.append(int(input()))
    if len(nums) == 2:
        ans += nums[1] - nums[0]
        nums = []

if n % 2 == 0:
    print(ans)
else:
    print("still running")

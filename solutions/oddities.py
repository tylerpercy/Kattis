n = int(input())

nums = []
for _ in range(0, n):
    nums.append(int(input()))

for num in nums:
    print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")
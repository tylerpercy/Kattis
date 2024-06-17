nums = []
for _ in range(0, int(input())):
    cities = []
    for _ in range(0, int(input())):
        cities.append(input())
    nums.append(len(set(cities)))

for num in nums:
    print(num)




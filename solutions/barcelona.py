_, x = [int(i) for i in input().split()]
bags = [int(i) for i in input().split()]
print("fyrst") if bags.index(x) == 0 else print("naestfyrst") if bags.index(x) == 1 else print(f"{bags.index(x)+1} fyrst")
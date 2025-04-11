low = 1
high = 1000

while low <= high:

    mid = (low + high) // 2

    print(mid, flush=True)

    response = input()

    if response == "correct":
        break
    elif response == "lower":
        high = mid - 1
    else:
        low = mid + 1
    

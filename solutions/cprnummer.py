print(int(sum([int(x) * int(y) for x, y in zip(list(input().replace("-","")), list("4327654321"))]) % 11 == 0))
g, s, c = [int(x) for x in input().split()]

sum = g*3+s*2+c

if 0 <= sum <= 1:
    print("Copper")
elif sum == 2:
    print("Estate or Copper")
elif 3 <= sum <= 4:
    print("Estate or Silver")
elif sum == 5:
    print("Duchy or Silver")
elif 6 <= sum <= 7:
    print("Duchy or Gold")
elif sum >= 8:
    print("Province or Gold")



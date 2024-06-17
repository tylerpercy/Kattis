n = input()

if n.count('b') > n.count('k'):
    print("boba")
elif n.count('b') < n.count('k'):
    print("kiki")
elif n.count('b') == 0 and n.count('k') == 0:
    print("none")
elif n.count('b') == n.count('k'):
    print("boki")

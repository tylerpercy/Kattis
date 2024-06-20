s = input()

if ":(" in s and ":)" in s:
    print("double agent")
elif ":(" in s:
    print("undead")
elif ":)" in s:
    print("alive")
else:
    print("machine")

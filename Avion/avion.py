# Tyler Percy
# 1/20/21

s = ""
for i in range(1, 6):
    if "FBI" in input():
        s += "%d " % i

if len(s) == 0:
    print("HE GOT AWAY!")
else:
    print(s)
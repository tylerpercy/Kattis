s = input()
l = input()
l = [l[i:i+3] for i in range(0, len(l), 3)]

string = ""
for val in l:
    string += s[int(val)-1]

print(string)
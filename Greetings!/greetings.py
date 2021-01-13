# Tyler Percy
# 1/13/21

greet = input()
new = greet.translate({ord(i): None for i in 'hy'})
print("h%sy" % (new*2))

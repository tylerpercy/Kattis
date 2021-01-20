# Tyler Percy
# 1/19/21

name = input().split(' ')
extra_vowels = ['a','i','o','u']

if name[0][len(name[0])-1] == 'e':
    print("%sx%s" % (name[0], name[1]))
elif (name[0][len(name[0])-2] == 'e' and name[0][len(name[0])-1] == 'x'):
    print("%s%s" % (name[0], name[1]))
elif (name[0][len(name[0])-1] in extra_vowels):
    name[0] = name[0][:-1]
    print("%sex%s" % (name[0], name[1]))
elif (name[0][len(name[0])-1] not in extra_vowels and name[0][len(name[0])-1] != 'e'):
     print("%sex%s" % (name[0], name[1]))
else:
    pass

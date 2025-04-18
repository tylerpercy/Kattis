nums = {
    'a' : '2',
    'b' : '22',
    'c' : '222',
    'd' : '3',
    'e' : '33',
    'f' : '333',
    'g' : '4',
    'h' : '44',
    'i' : '444',
    'j' : '5',
    'k' : '55',
    'l' : '555',
    'm' : '6',
    'n' : '66',
    'o' : '666',
    'p' : '7',
    'q' : '77',
    'r' : '777',
    's' : '7777',
    't' : '8',
    'u' : '88',
    'v' : '888',
    'w' : '9',
    'x' : '99',
    'y' : '999',
    'z' : '9999',
    ' ' : '0'  
}

for i in range(int(input())):
    s = input()
    result = ''
    for char in s:
        if char == ' ':
            if result and result[-1] == '0':
                result += ' '
            result += '0'
        else:
            if result and result[-1] == nums[char][0]:
                result += ' '
            result += nums[char]
    print(f"Case #{i+1}: {result}")
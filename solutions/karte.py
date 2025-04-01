S = input()
s = [S[i:i+3] for i in range(0, len(S), 3)]

if any(s.count(c) > 1 for c in set(s)):
    print("GRESKA")
else:
    print(f"{13 - sum(word.startswith('P') for word in s)} {13 - sum(word.startswith('K') for word in s)} {13 - sum(word.startswith('H') for word in s)} {13 - sum(word.startswith('T') for word in s)}")




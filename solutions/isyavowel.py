n = input()
print(f"{len([vowel for vowel in n if vowel in 'aeiou'])} {len([vowel for vowel in n if vowel in 'aeiouy'])}")
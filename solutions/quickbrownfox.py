for _ in range(int(input())):
    s = sorted(list(set('abcdefghijklmnopqrstuvwxyz') - set(input().lower())))
    print(f"missing {''.join(s)}") if len(s) > 0 else print("pangram")
    



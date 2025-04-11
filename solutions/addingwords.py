import sys

s = sys.stdin.read().splitlines()

words = {}

for line in s:
    tok = line.split()
    if not tok:
        continue

    if tok[0] == "def":
        try:
            int(tok[2])  
            for k, v in list(words.items()):
                if v == tok[2]:
                    del words[k]
            words[tok[1]] = tok[2]
        except (IndexError, ValueError):
            continue

    elif tok[0] == "calc":
        expr = []
        unknown = False
        for t in tok[1:]:
            if t == "=":
                break
            elif t in ['+', '-']:
                expr.append(t)
            elif t in words:
                expr.append(words[t])
            else:
                unknown = True
                break

        if unknown or not expr:
            result = "unknown"
        else:
            try:
                result = eval(" ".join(expr))
            except Exception:
                result = "unknown"

        try:
            match = [(k, v) for k, v in words.items() if result != "unknown" and int(v) == result]
        except ValueError:
            match = []

        print(" ".join(tok[1:]), match[0][0] if match else "unknown")

    elif tok[0] == "clear":
        words = {}
    else:
        continue

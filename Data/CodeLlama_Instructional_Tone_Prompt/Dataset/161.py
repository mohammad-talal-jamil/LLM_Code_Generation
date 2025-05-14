def solve(s):
    res = ""
    for c in s:
        if c.isalpha():
            res += c.lower() if c.isupper() else c.upper()
        else:
            res += c
    return res[::-1] if not any(c.isalpha() for c in s) else res

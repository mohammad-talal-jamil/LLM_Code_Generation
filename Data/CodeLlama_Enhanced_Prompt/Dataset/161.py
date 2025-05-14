def solve(s):
    return "".join(c.swapcase() if c.isalpha() else c for c in s)[::-1] if not any(c.isalpha() for c in s) else "".join(c.swapcase() if c.isalpha() else c for c in s)

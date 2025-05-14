def solve(s):
    # Write your code here
    return "".join([c.lower() if c.isalpha() and c.isupper() else c.upper() if c.isalpha() and c.islower() else c for c in s][::-1]) if any(c.isalpha() for c in s) else s[::-1]

def simplify(x, n):
    a, b = map(int, x.split("/"))
    c, d = map(int, n.split("/"))
    return (a * c) % d == 0 and (b * d) % c == 0

import math


def poly(xs, x):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    if len(xs) % 2 == 1:
        xs = xs[:-1]
    x = 0
    while poly(xs, x) != 0:
        x += 1e-5
    return x

import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients and the largest non-zero coefficient as it guarantees a solution.
    """
    import math
    n = len(xs)
    if n % 2 == 1:
        return None
    for i in range(n // 2):
        if xs[i] != 0 and xs[-i-1] != 0:
            x = -xs[i] / xs[-i-1]
            if math.fabs(poly(xs, x)) < 1e-4:
                return x
    return None

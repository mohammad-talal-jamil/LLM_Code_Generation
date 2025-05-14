def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Convert all arguments to floats and compare
    a_float = float(a.replace(",", "."))
    b_float = float(b.replace(",", "."))
    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None

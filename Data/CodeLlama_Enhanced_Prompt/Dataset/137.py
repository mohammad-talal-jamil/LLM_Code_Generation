def compare_one(a, b):
    def convert_to_float(x):
        if isinstance(x, str):
            x = x.replace(',', '.')
        return float(x)
    a, b = convert_to_float(a), convert_to_float(b)
    if a == b:
        return None
    return a if a > b else b

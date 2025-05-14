def closest_integer(value):
    try:
        num = float(value)
        return int(round(num))
    except ValueError:
        return 0

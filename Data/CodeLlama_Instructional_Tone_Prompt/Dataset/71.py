def triangle_area(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        area = (a + b + c) / 2
        return round(math.sqrt(area), 2)
    else:
        return -1

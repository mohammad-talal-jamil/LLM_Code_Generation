def Strongest_Extension(class_name, extensions):
    strengths = []
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strengths.append((cap - sm, extension))
    return class_name + '.' + sorted(strengths, reverse=True)[0][1]

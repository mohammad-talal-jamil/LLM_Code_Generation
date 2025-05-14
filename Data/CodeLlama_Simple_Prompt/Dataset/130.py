def tri(n):
    if n == 1:
        return [3]
    else:
        d = tri(n-1)
        d.append(d[n-2] + d[n-3] + d[n])
        return d

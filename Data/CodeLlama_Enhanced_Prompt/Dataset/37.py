def sort_even(l):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    return [e if i % 2 == 0 else o for i, (e, o) in enumerate(zip(evens, odds))]

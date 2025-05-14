def exchange(lst1, lst2):
    odd = sum(x % 2 for x in lst1)
    even = sum(not x % 2 for x in lst2)
    return "YES" if even >= odd else "NO"

def reverse_delete(s, c):
    new_str = ""
    for char in s:
        if char not in c:
            new_str = char + new_str
    return (new_str, new_str == new_str[::-1])

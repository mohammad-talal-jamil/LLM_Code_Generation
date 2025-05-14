def match_parens(lst):
    open_count = 0
    for char in lst[0]:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        if open_count < 0:
            return 'No'
    return 'Yes' if open_count == 0 else 'No'

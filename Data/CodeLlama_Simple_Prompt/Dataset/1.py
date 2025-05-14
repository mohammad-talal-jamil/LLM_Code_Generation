def separate_paren_groups(paren_string):
    open_brace = 0
    start = 0
    result = []
    for i, char in enumerate(paren_string):
        if char == '(':
            if open_brace == 0:
                start = i
            open_brace += 1
        elif char == ')':
            open_brace -= 1
            if open_brace == 0:
                result.append(paren_string[start:i+1])
    return result

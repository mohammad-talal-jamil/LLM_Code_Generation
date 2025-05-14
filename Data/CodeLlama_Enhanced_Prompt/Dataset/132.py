def is_nested(string):
    return any(string.count(bracket) > 1 for bracket in ['[]', '()', '{}'])

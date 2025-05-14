def match_parens(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """
    # Initialize a dictionary to keep track of the count of open and close parentheses
    parens = {
        "(": 0,
        ")": 0
    }

    # Iterate through each character in the first string and update the count in the dictionary
    for char in lst[0]:
        parens[char] += 1

    # Iterate through each character in the second string and update the count in the dictionary
    for char in lst[1]:
        parens[char] += 1

    # Check if the counts of open and close parentheses are equal
    if parens["("] == parens[")"]:
        return "Yes"
    else:
        return "No"

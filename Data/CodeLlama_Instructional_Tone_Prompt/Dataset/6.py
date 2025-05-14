def parse_nested_parens(paren_string):
    # Initialize a stack to keep track of opening parentheses
    stack = []
    # Initialize a list to store the maximum nesting level for each group
    max_levels = []
    # Iterate through each character in the string
    for char in paren_string:
        # If we encounter an opening parenthesis, add it to the stack
        if char == '(':
            stack.append(char)
        # If we encounter a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            # Check if the stack is empty, if it is, this is an invalid string
            if not stack:
                return []
            stack.pop()
        # If we encounter a space, calculate the maximum nesting level for the previous group
        elif char == ' ':
            # Check if the stack is empty, if it is, the maximum nesting level is 1
            if not stack:
                max_levels.append(1)
            else:
                # The maximum nesting level is the length of the stack
                max_levels.append(len(stack))
    # If the string ends with a group, calculate its maximum nesting level
    if stack:
        max_levels.append(len(stack))
    return max_levels

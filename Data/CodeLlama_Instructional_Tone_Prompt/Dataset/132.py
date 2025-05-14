def is_nested(string):
    # Initialize a stack to keep track of opening brackets
    stack = []
    # Loop through each character in the string
    for char in string:
        # If the current character is an opening bracket, push it onto the stack
        if char == "[":
            stack.append(char)
        # If the current character is a closing bracket, pop the last opening bracket from the stack
        elif char == "]":
            if len(stack) == 0:
                return False
            stack.pop()
    # If there are any opening brackets left in the stack, the brackets are not nested
    if len(stack) != 0:
        return False
    # If there are no opening brackets left in the stack, the brackets are nested
    return True

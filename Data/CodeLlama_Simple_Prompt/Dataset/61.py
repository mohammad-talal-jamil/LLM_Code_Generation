def correct_bracketing(brackets: str) -> bool:
    # Initialize a stack to keep track of the opening brackets
    stack = []
    # Iterate through each bracket in the input string
    for char in brackets:
        # If we encounter an opening bracket, push it onto the stack
        if char == "(":
            stack.append(char)
        # If we encounter a closing bracket, pop the corresponding opening bracket from the stack
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    # If all opening brackets have a corresponding closing bracket, the stack should be empty
    return len(stack) == 0

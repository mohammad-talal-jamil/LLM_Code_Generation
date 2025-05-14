def correct_bracketing(brackets: str) -> bool:
    # Initialize a stack to keep track of the opening brackets
    stack = []
    # Iterate through each bracket in the input string
    for bracket in brackets:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket == "<":
            stack.append(bracket)
        # If the bracket is a closing bracket, pop the corresponding opening bracket from the stack
        elif bracket == ">":
            if len(stack) == 0:  # If the stack is empty, there is no corresponding opening bracket
                return False
            stack.pop()
    # If the stack is not empty at the end of the iteration, there are more opening brackets than closing brackets
    return len(stack) == 0

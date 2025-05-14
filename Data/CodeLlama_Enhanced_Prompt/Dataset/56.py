def correct_bracketing(brackets: str) -> bool:
    """
    Returns True if every opening bracket has a corresponding closing bracket.
    """
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

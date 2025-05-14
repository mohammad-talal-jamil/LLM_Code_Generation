from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    """
    # split the input string into separate groups
    groups = paren_string.split(" ")
    # initialize a list to store the output
    output = []

    for group in groups:
        # initialize variables to keep track of the current level and max level
        current_level = 0
        max_level = 0

        # iterate through each character in the group
        for char in group:
            # if the character is an opening parenthesis, increase the current level
            if char == "(":
                current_level += 1
            # if the character is a closing parenthesis, decrease the current level
            elif char == ")":
                current_level -= 1
            # update the max level if the current level is greater than it
            if current_level > max_level:
                max_level = current_level

        # add the max level to the output list
        output.append(max_level)

    return output

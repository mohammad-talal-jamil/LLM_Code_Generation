def will_it_fly(q, w):
    """
    Returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    """
    # Check if the object is balanced
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to the maximum possible weight
        if sum(q) <= w:
            return True
    return False

def next_smallest(lst):
    """
    Returns the second smallest element of the list, or None if there is no such element.
    """
    # Sort the list and remove duplicates
    srt_list = sorted(set(lst))

    # Return the second element if it exists, otherwise return None
    return srt_list[1] if len(srt_list) > 1 else None

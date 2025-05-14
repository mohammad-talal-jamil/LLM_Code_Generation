def find_max(words):
    """
    Returns the word with the maximum number of unique characters.
    If there are multiple words with maximum number of unique characters,
    returns the first one in lexicographical order.
    """
    return max(words, key=lambda x: (len(set(x)), x))

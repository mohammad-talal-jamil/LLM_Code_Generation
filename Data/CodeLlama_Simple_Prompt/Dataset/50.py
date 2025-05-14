def encode_shift(string):
    """
    Returns a encoded string where every character is shifted by 5 in the alphabet.
    """
    return "".join([chr((ord(char) + 5 - ord("a")) % 26 + ord("a")) for char in string])

def decode_shift(string):
    """
    Takes as input a string encoded with the encode_shift function.
    Returns the decoded string.
    """
    return "".join([chr((ord(char) - 5 - ord("a")) % 26 + ord("a")) for char in string])
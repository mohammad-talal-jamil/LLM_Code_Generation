def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = str.maketrans(vowels, vowels[2:] + vowels[:2])
    return message.swapcase().translate(vowels_replace)

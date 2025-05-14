def vowels_count(word):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in word)
    if word[-1] == 'y' or word[-1] == 'Y':
        n_vowels += 1
    return n_vowels

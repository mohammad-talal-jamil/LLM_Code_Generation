def get_closest_vowel(word):
    for i in range(len(word) - 1, 0, -1):
        if word[i].lower() in "aeiou":
            return word[i]
    return ""

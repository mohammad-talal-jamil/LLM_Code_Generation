def anti_shuffle(s):
    words = s.split()
    ordered_words = []
    for word in words:
        ascending = sorted(word)
        ordered_words.append(''.join(ascending))
    return ' '.join(ordered_words)
